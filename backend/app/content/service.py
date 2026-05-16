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
class LessonContent:
    unit: int
    lesson: int
    title: str
    narrative: str
    code_starter: str
    hints: list[str]
    tests: list[LessonTest]
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
    # Fall back to fantasy if requested world not found
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
    raw_tests: list[dict[str, str]] = data.get("tests", [])
    return LessonContent(
        unit=unit,
        lesson=lesson,
        title=world_data.get("title", f"Unit {unit} · Lesson {lesson}"),
        narrative=world_data.get("narrative", "").strip(),
        code_starter=data.get("code_starter", "").rstrip(),
        hints=data.get("hints", []),
        tests=[LessonTest(code=t["code"], message=t["message"]) for t in raw_tests],
        xp=data.get("xp", 10),
    )
