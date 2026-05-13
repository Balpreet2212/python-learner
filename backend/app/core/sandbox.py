"""Run learner code in an isolated subprocess and return structured results."""

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

TIMEOUT_SECONDS = 10
MAX_OUTPUT_CHARS = 2000

# Runner template: injected into a temp .py file and executed as a subprocess.
# User code and test specs are embedded as Python repr() literals — never interpolated raw.
_RUNNER = """\
import json as _j, sys as _s, io as _io

_code = {user_code!r}
_tests = {tests!r}

_ns: dict = {{"__builtins__": __builtins__}}
_buf = _io.StringIO()
_s.stdout = _buf
_exec_err = None
try:
    exec(compile(_code, "<learner>", "exec"), _ns)
except Exception as _e:
    _exec_err = f"{{type(_e).__name__}}: {{_e}}"
finally:
    _s.stdout = _s.__stdout__
    _out = _buf.getvalue()[:{max_output}]

_results = []
for _t in _tests:
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
    "all_passed": _exec_err is None and all(r["passed"] for r in _results),
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
