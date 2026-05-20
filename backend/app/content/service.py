"""Load lesson content from YAML files in content/units/."""

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

CONTENT_DIR = Path(__file__).parents[3] / "content"
LESSONS_PER_UNIT = 5
MAX_UNITS = 6


@dataclass
class LessonTest:
    code: str
    message: str


@dataclass
class ExampleContent:
    code: str
    explanation: str
    output: str


@dataclass
class FinalChallengeContent:
    prompt: str
    code_starter: str
    hints: list[str]
    tests: list[LessonTest]


@dataclass
class LessonContent:
    unit: int
    lesson: int
    title: str
    setup: str
    example: ExampleContent
    code_starter: str
    hints: list[str]
    tests: list[LessonTest]
    final_challenge: FinalChallengeContent
    xp: int
    total_lessons: int = LESSONS_PER_UNIT


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


def _resolve_world(data: dict[str, Any], world: str) -> dict[str, Any]:
    worlds: dict[str, Any] = data.get("worlds", {})
    return worlds.get(world) or worlds.get("fantasy") or {}


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
        tests=[LessonTest(code=t["code"], message=t["message"]) for t in raw_tests],
        plan_prompts=data.get("plan_prompts", []),
        xp=data.get("xp", 150),
    )


def load_lesson(unit: int, lesson: int, world: str) -> LessonContent | None:
    path = CONTENT_DIR / "units" / f"unit_{unit}" / f"lesson_{lesson}.yaml"
    if not path.exists():
        return None
    data: dict[str, Any] = yaml.safe_load(path.read_text(encoding="utf-8"))
    world_data = _resolve_world(data, world)
    raw_example: dict[str, Any] = data.get("example", {})
    raw_tests: list[dict[str, str]] = data.get("tests", [])
    raw_fc: dict[str, Any] = data.get("final_challenge", {})
    raw_fc_tests: list[dict[str, str]] = raw_fc.get("tests", [])
    return LessonContent(
        unit=unit,
        lesson=lesson,
        title=world_data.get("title", f"Unit {unit} · Lesson {lesson}"),
        setup=world_data.get("setup", "").strip(),
        example=ExampleContent(
            code=raw_example.get("code", "").rstrip(),
            explanation=raw_example.get("explanation", "").strip(),
            output=raw_example.get("output", "").strip(),
        ),
        code_starter=data.get("code_starter", "").rstrip(),
        hints=data.get("hints", []),
        tests=[LessonTest(code=t["code"], message=t["message"]) for t in raw_tests],
        final_challenge=FinalChallengeContent(
            prompt=world_data.get("final_challenge_prompt", "").strip(),
            code_starter=raw_fc.get("code_starter", "").rstrip(),
            hints=raw_fc.get("hints", []),
            tests=[LessonTest(code=t["code"], message=t["message"]) for t in raw_fc_tests],
        ),
        xp=data.get("xp", 10),
    )
