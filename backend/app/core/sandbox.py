"""Run learner code in an isolated subprocess and return structured results."""

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

TIMEOUT_SECONDS = 10
MAX_OUTPUT_CHARS = 2000

# Safe subset of builtins available to learner code — no file I/O, no exec/eval, no imports.
_SAFE_BUILTINS = (
    "abs all any bin bool breakpoint callable chr delattr dict dir divmod "
    "enumerate filter float format frozenset getattr hasattr hash hex "
    "id input int isinstance issubclass iter len list map max min next "
    "object oct ord pow print range repr reversed round set setattr "
    "slice sorted str sum tuple type vars zip "
    "ArithmeticError AssertionError AttributeError EOFError Exception "
    "FileNotFoundError FloatPoint GeneratorExit IOError ImportError "
    "IndexError KeyError KeyboardInterrupt LookupError MemoryError "
    "NameError NotImplementedError OSError OverflowError RecursionError "
    "RuntimeError StopIteration SyntaxError SystemExit TypeError "
    "UnicodeDecodeError UnicodeEncodeError UnicodeError ValueError "
    "ZeroDivisionError True False None"
)

# Runner template: injected into a temp .py file and executed as a subprocess.
# User code and test specs are embedded as Python repr() literals — never interpolated raw.
# Tests may include a "stdin" key; those tests re-execute the user code with a mocked
# input() that returns lines from the provided string. This prevents hardcoding answers
# because different test cases supply different inputs.
_RUNNER = """\
import json as _j, sys as _s, io as _io, builtins as _b

_code = {user_code!r}
_tests = {tests!r}
_MAX = {max_output}

_safe = {{k: getattr(_b, k) for k in dir(_b) if k in (
    "abs", "all", "any", "bin", "bool", "callable", "chr", "dict",
    "divmod", "enumerate", "filter", "float", "format", "frozenset",
    "getattr", "hasattr", "hash", "hex", "id", "int", "isinstance",
    "issubclass", "iter", "len", "list", "map", "max", "min", "next",
    "object", "oct", "ord", "pow", "print", "range", "repr", "reversed",
    "round", "set", "setattr", "slice", "sorted", "str", "sum", "tuple",
    "type", "vars", "zip",
    "__build_class__", "__name__",
    "ArithmeticError", "AssertionError", "AttributeError", "EOFError",
    "Exception", "IndexError", "KeyError", "NameError", "NotImplementedError",
    "OSError", "OverflowError", "RecursionError", "RuntimeError",
    "StopIteration", "SyntaxError", "TypeError", "ValueError",
    "ZeroDivisionError", "True", "False", "None",
)}}

def _exec_code(stdin_str):
    builtins = dict(_safe)
    if stdin_str is not None:
        _lines = stdin_str.strip().split("\\n")
        _idx = [0]
        def _input(_prompt=""):
            val = _lines[_idx[0]] if _idx[0] < len(_lines) else ""
            _idx[0] += 1
            return val
        builtins["input"] = _input
    ns = {{"__builtins__": builtins}}
    buf = _io.StringIO()
    _s.stdout = buf
    err = None
    try:
        exec(compile(_code, "<learner>", "exec"), ns)
    except Exception as _e:
        err = f"{{type(_e).__name__}}: {{_e}}"
    finally:
        _s.stdout = _s.__stdout__
    out = buf.getvalue()[:_MAX]
    ns["_stdout"] = out
    ns["_code"] = _code
    return ns, out, err

# For the display output, use the first stdin-bearing test's input if one exists,
# otherwise run with no stdin (backward-compatible with exercises that don't use input()).
_display_stdin = next((_t.get("stdin") for _t in _tests if _t.get("stdin") is not None), None)
_ns, _out, _exec_err = _exec_code(_display_stdin)

_results = []
for _t in _tests:
    _stdin = _t.get("stdin")
    if _stdin is not None:
        _tns, _tout, _terr = _exec_code(_stdin)
        if _terr:
            _results.append({{"passed": False, "message": _terr}})
        else:
            try:
                exec(compile(_t["code"], "<test>", "exec"), _tns)
                _results.append({{"passed": True, "message": _t["message"]}})
            except AssertionError as _ae:
                _results.append({{"passed": False, "message": str(_ae) or _t["message"]}})
            except Exception as _e:
                _results.append({{"passed": False, "message": f"Error: {{_e}}"}})
    else:
        if _exec_err:
            _results.append({{"passed": False, "message": _t["message"]}})
        else:
            try:
                exec(compile(_t["code"], "<test>", "exec"), _ns)
                _results.append({{"passed": True, "message": _t["message"]}})
            except AssertionError as _ae:
                _results.append({{"passed": False, "message": str(_ae) or _t["message"]}})
            except Exception as _e:
                _results.append({{"passed": False, "message": f"Error: {{_e}}"}})

print(_j.dumps({{
    "exec_error": _exec_err,
    "stdout": _out,
    "tests": _results,
    "all_passed": all(r["passed"] for r in _results),
}}))
"""


@dataclass
class RunResult:
    all_passed: bool
    exec_error: str | None
    stdout: str
    tests: list[dict[str, object]]  # [{passed, message}]


def run_challenge(user_code: str, tests: list[dict[str, str]]) -> RunResult:
    """Execute user_code then evaluate each test assertion. Returns structured result."""
    script = _RUNNER.format(
        user_code=user_code,
        tests=tests,
        max_output=MAX_OUTPUT_CHARS,
    )
    tmp = Path(tempfile.mktemp(suffix=".py"))
    try:
        tmp.write_text(script, encoding="utf-8")
        proc = subprocess.run(
            [sys.executable, str(tmp)],
            capture_output=True,
            text=True,
            timeout=TIMEOUT_SECONDS,
        )
        if proc.returncode != 0 and not proc.stdout.strip():
            return RunResult(
                all_passed=False,
                exec_error=proc.stderr.strip()[:MAX_OUTPUT_CHARS] or "Unknown error",
                stdout="",
                tests=[{"passed": False, "message": t["message"]} for t in tests],
            )
        data: dict[str, object] = json.loads(proc.stdout)
        raw_exec_err = data.get("exec_error")
        raw_tests = data.get("tests")
        test_list: list[dict[str, object]] = (
            [t for t in raw_tests if isinstance(t, dict)]
            if isinstance(raw_tests, list)
            else []
        )
        return RunResult(
            all_passed=bool(data.get("all_passed")),
            exec_error=str(raw_exec_err) if raw_exec_err else None,
            stdout=str(data.get("stdout", "")),
            tests=test_list,
        )
    except subprocess.TimeoutExpired:
        return RunResult(
            all_passed=False,
            exec_error=f"Code timed out after {TIMEOUT_SECONDS} seconds",
            stdout="",
            tests=[{"passed": False, "message": t["message"]} for t in tests],
        )
    finally:
        tmp.unlink(missing_ok=True)
