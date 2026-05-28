"""Load lesson and capstone content from YAML files."""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Union

import yaml

CONTENT_DIR = Path(__file__).parents[3] / "content"
LESSONS_PER_UNIT = 5
MAX_UNITS = 7


@dataclass
class LessonTest:
    code: str
    message: str
    stdin: str | None = None


# ── Exercise types ────────────────────────────────────────────────────────────


@dataclass
class ConceptExercise:
    type: str
    code: str
    output: str
    explanation: str
    story_before: str | None = None
    story_after: str | None = None


@dataclass
class McqExercise:
    type: str
    question: str
    code: str
    choices: list[str]
    correct: str
    explanation: str
    story_before: str | None = None
    story_after: str | None = None


@dataclass
class ArrangeExercise:
    type: str
    instruction: str
    blocks: list[str]
    correct: list[str]
    explanation: str
    story_before: str | None = None
    story_after: str | None = None


@dataclass
class FillBlankExercise:
    type: str
    prompt: str
    before: str
    after: str
    choices: list[str]
    answer: str
    explanation: str
    story_before: str | None = None
    story_after: str | None = None


@dataclass
class MiniCodeExercise:
    type: str
    prompt: str
    starter: str
    tests: list[LessonTest]
    story_before: str | None = None
    story_after: str | None = None


@dataclass
class BreakFixExercise:
    type: str
    prompt: str
    broken_code: str
    hint: str
    tests: list[LessonTest]
    explanation: str
    story_before: str | None = None
    story_after: str | None = None


Exercise = Union[ConceptExercise, McqExercise, ArrangeExercise, FillBlankExercise, MiniCodeExercise, BreakFixExercise]


def _parse_exercise(raw: dict[str, Any]) -> Exercise:
    t = raw.get("type", "")
    if t == "concept":
        return ConceptExercise(
            type="concept",
            code=raw.get("code", "").rstrip(),
            output=raw.get("output", "").strip(),
            explanation=raw.get("explanation", "").strip(),
            story_before=raw.get("story_before") or None,
            story_after=raw.get("story_after") or None,
        )
    if t == "mcq":
        return McqExercise(
            type="mcq",
            question=raw.get("question", "").strip(),
            code=raw.get("code", "").rstrip(),
            choices=raw.get("choices", []),
            correct=str(raw.get("correct", "")),
            explanation=raw.get("explanation", "").strip(),
            story_before=raw.get("story_before") or None,
            story_after=raw.get("story_after") or None,
        )
    if t == "arrange":
        return ArrangeExercise(
            type="arrange",
            instruction=raw.get("instruction", "").strip(),
            blocks=raw.get("blocks", []),
            correct=raw.get("correct", []),
            explanation=raw.get("explanation", "").strip(),
            story_before=raw.get("story_before") or None,
            story_after=raw.get("story_after") or None,
        )
    if t == "fill_blank":
        return FillBlankExercise(
            type="fill_blank",
            prompt=raw.get("prompt", "").strip(),
            before=raw.get("before", ""),
            after=raw.get("after", ""),
            choices=raw.get("choices", []),
            answer=str(raw.get("answer", "")),
            explanation=raw.get("explanation", "").strip(),
            story_before=raw.get("story_before") or None,
            story_after=raw.get("story_after") or None,
        )
    if t == "mini_code":
        raw_tests: list[dict[str, str]] = raw.get("tests", [])
        return MiniCodeExercise(
            type="mini_code",
            prompt=raw.get("prompt", "").strip(),
            starter=raw.get("starter", "").rstrip(),
            tests=[LessonTest(code=r["code"], message=r["message"], stdin=r.get("stdin")) for r in raw_tests],
            story_before=raw.get("story_before") or None,
            story_after=raw.get("story_after") or None,
        )
    if t == "break_fix":
        raw_tests2: list[dict[str, str]] = raw.get("tests", [])
        return BreakFixExercise(
            type="break_fix",
            prompt=raw.get("prompt", "").strip(),
            broken_code=raw.get("broken_code", "").rstrip(),
            hint=raw.get("hint", "").strip(),
            tests=[LessonTest(code=r["code"], message=r["message"], stdin=r.get("stdin")) for r in raw_tests2],
            explanation=raw.get("explanation", "").strip(),
            story_before=raw.get("story_before") or None,
            story_after=raw.get("story_after") or None,
        )
    raise ValueError(f"Unknown exercise type: {t!r}")


# ── Lesson ────────────────────────────────────────────────────────────────────


@dataclass
class LessonContent:
    unit: int
    lesson: int
    title: str
    xp: int
    total_lessons: int
    exercises: list[Exercise] = field(default_factory=list)


def _resolve_world(data: dict[str, Any], world: str) -> dict[str, Any]:
    worlds: dict[str, Any] = data.get("worlds", {})
    return worlds.get(world) or worlds.get("fantasy") or {}


def load_lesson(unit: int, lesson: int, world: str) -> LessonContent | None:
    path = CONTENT_DIR / "units" / f"unit_{unit}" / f"lesson_{lesson}.yaml"
    if not path.exists():
        return None
    data: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    world_data = _resolve_world(data, world)

    raw_exercises: list[dict[str, Any]] = world_data.get("exercises") or data.get("exercises", [])
    exercises = [_parse_exercise(e) for e in raw_exercises]

    return LessonContent(
        unit=unit,
        lesson=lesson,
        title=world_data.get("title", data.get("title", f"Unit {unit} · Lesson {lesson}")),
        xp=data.get("xp", 10),
        total_lessons=LESSONS_PER_UNIT,
        exercises=exercises,
    )


# ── Capstone ──────────────────────────────────────────────────────────────────


@dataclass
class CapstoneContent:
    unit: int
    title: str
    narrative: str
    story_beat: str
    code_starter: str
    hints: list[str]
    tests: list[LessonTest]
    plan_prompts: list[str]
    xp: int


def load_capstone(unit: int, world: str) -> CapstoneContent | None:
    path = CONTENT_DIR / "units" / f"unit_{unit}" / "capstone.yaml"
    if not path.exists():
        return None
    data: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    world_data = _resolve_world(data, world)
    raw_tests: list[dict[str, str]] = data.get("tests", [])
    return CapstoneContent(
        unit=unit,
        title=world_data.get("title", f"Unit {unit} Capstone"),
        narrative=world_data.get("narrative", "").strip(),
        story_beat=world_data.get("story_beat", "").strip(),
        code_starter=data.get("code_starter", "").rstrip(),
        hints=data.get("hints", []),
        tests=[LessonTest(code=t["code"], message=t["message"], stdin=t.get("stdin")) for t in raw_tests],
        plan_prompts=data.get("plan_prompts", []),
        xp=data.get("xp", 150),
    )


# ── Weekly challenge ──────────────────────────────────────────────────────────


@dataclass
class WeeklyChallengeContent:
    challenge_index: int
    week_key: str
    title: str
    description: str
    code_starter: str
    hints: list[str]
    tests: list[LessonTest]
    xp: int
    difficulty: str


def _week_key(dt: datetime) -> str:
    iso = dt.isocalendar()
    return f"{iso.year}-W{iso.week:02d}"


def _current_challenge_index() -> int:
    files = sorted((CONTENT_DIR / "weekly").glob("challenge_*.yaml"))
    total = len(files)
    if total == 0:
        return 1
    iso_week = datetime.now(UTC).isocalendar().week
    return (iso_week - 1) % total + 1


def load_weekly_challenge(world: str) -> WeeklyChallengeContent | None:
    idx = _current_challenge_index()
    path = CONTENT_DIR / "weekly" / f"challenge_{idx}.yaml"
    if not path.exists():
        return None
    data: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    world_data = _resolve_world(data, world)
    raw_tests: list[dict[str, str]] = data.get("tests", [])
    return WeeklyChallengeContent(
        challenge_index=idx,
        week_key=_week_key(datetime.now(UTC)),
        title=world_data.get("title", data.get("title", "Weekly Challenge")),
        description=world_data.get("description", data.get("description", "")).strip(),
        code_starter=data.get("code_starter", "").rstrip(),
        hints=data.get("hints", []),
        tests=[LessonTest(code=t["code"], message=t["message"], stdin=t.get("stdin")) for t in raw_tests],
        xp=data.get("xp", 50),
        difficulty=data.get("difficulty", "medium"),
    )
