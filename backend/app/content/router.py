"""Lesson content and challenge submission routes (§8)."""

import json
from datetime import UTC, datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_account, require_csrf
from app.auth.schemas import LearnerProfileOut
from app.auth.service import _profile_out
from app.content.service import LESSONS_PER_UNIT, MAX_UNITS, load_capstone, load_lesson
from app.core.errors import bad_request, forbidden
from app.core.sandbox import run_challenge
from app.db.models import Account
from app.db.session import get_db

router = APIRouter(prefix="/v1/learner", tags=["content"])

BADGE_TEMPLATE = "unit_{unit}_complete"


# ── Response schemas ──────────────────────────────────────────────────────────


class LessonOut(BaseModel):
    unit: int
    lesson: int
    title: str
    narrative: str
    code_starter: str
    hints: list[str]
    xp: int
    test_count: int
    total_lessons: int


class TestResultOut(BaseModel):
    passed: bool
    message: str


class SubmitOut(BaseModel):
    all_passed: bool
    exec_error: str | None
    stdout: str
    tests: list[TestResultOut]


class SubmitRequest(BaseModel):
    code: str


class CapstonOut(BaseModel):
    unit: int
    title: str
    narrative: str
    story_beat: str
    code_starter: str
    hints: list[str]
    plan_prompts: list[str]
    xp: int
    test_count: int


# ── Endpoints ─────────────────────────────────────────────────────────────────


@router.get("/lesson")
async def get_lesson(
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
) -> LessonOut:
    if account.role != "learner":
        raise forbidden("Only learner accounts have lessons")
    if account.profile is None:
        await db.refresh(account, ["profile"])
    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before accessing lessons")

    content = load_lesson(profile.current_unit, profile.current_lesson, profile.world)
    if content is None:
        raise bad_request(
            f"Lesson content not found for unit {profile.current_unit} "
            f"lesson {profile.current_lesson}"
        )
    return LessonOut(
        unit=content.unit,
        lesson=content.lesson,
        title=content.title,
        narrative=content.narrative,
        code_starter=content.code_starter,
        hints=content.hints,
        xp=content.xp,
        test_count=len(content.tests),
        total_lessons=content.total_lessons,
    )


@router.post("/challenge/submit")
async def submit_challenge(
    body: SubmitRequest,
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> SubmitOut:
    if account.role != "learner":
        raise forbidden("Only learner accounts can submit challenges")
    if len(body.code) > 10_000:
        raise bad_request("Code submission too large")

    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before submitting challenges")

    content = load_lesson(profile.current_unit, profile.current_lesson, profile.world)
    if content is None:
        raise bad_request("Lesson content not found")

    tests = [{"code": t.code, "message": t.message} for t in content.tests]
    result = run_challenge(body.code, tests)
    return SubmitOut(
        all_passed=result.all_passed,
        exec_error=result.exec_error,
        stdout=result.stdout,
        tests=[
            TestResultOut(passed=bool(t["passed"]), message=str(t["message"]))
            for t in result.tests
        ],
    )


@router.post("/lesson/advance")
async def advance_lesson(
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> LearnerProfileOut:
    """Advance to the next lesson (or next unit). Must have completed the challenge first."""
    if account.role != "learner":
        raise forbidden("Only learner accounts can advance lessons")

    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before advancing lessons")

    current_unit = profile.current_unit
    current_lesson = profile.current_lesson

    if current_lesson < LESSONS_PER_UNIT:
        profile.current_lesson += 1
    else:
        raise bad_request("Complete the unit capstone to advance to the next unit")

    account.updated_at = datetime.now(UTC)
    await db.commit()

    result = _profile_out(account)
    if result is None:
        raise bad_request("Profile unavailable after advance")
    return result


# ── Capstone endpoints ────────────────────────────────────────────────────────


@router.get("/capstone")
async def get_capstone(
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
) -> CapstonOut:
    if account.role != "learner":
        raise forbidden("Only learner accounts have capstones")
    if account.profile is None:
        await db.refresh(account, ["profile"])
    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before accessing capstones")

    content = load_capstone(profile.current_unit, profile.world)
    if content is None:
        raise bad_request(f"Capstone not found for unit {profile.current_unit}")
    return CapstonOut(
        unit=content.unit,
        title=content.title,
        narrative=content.narrative,
        story_beat=content.story_beat,
        code_starter=content.code_starter,
        hints=content.hints,
        plan_prompts=content.plan_prompts,
        xp=content.xp,
        test_count=len(content.tests),
    )


@router.post("/capstone/submit")
async def submit_capstone(
    body: SubmitRequest,
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> SubmitOut:
    if account.role != "learner":
        raise forbidden("Only learner accounts can submit capstones")
    if len(body.code) > 10_000:
        raise bad_request("Code submission too large")

    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before submitting")

    content = load_capstone(profile.current_unit, profile.world)
    if content is None:
        raise bad_request("Capstone content not found")

    tests = [{"code": t.code, "message": t.message} for t in content.tests]
    result = run_challenge(body.code, tests)
    return SubmitOut(
        all_passed=result.all_passed,
        exec_error=result.exec_error,
        stdout=result.stdout,
        tests=[
            TestResultOut(passed=bool(t["passed"]), message=str(t["message"]))
            for t in result.tests
        ],
    )


@router.post("/capstone/advance")
async def advance_capstone(
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> LearnerProfileOut:
    """Award unit badge and advance to the next unit after passing the capstone."""
    if account.role != "learner":
        raise forbidden("Only learner accounts can advance capstones")

    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before advancing")

    current_unit = profile.current_unit

    # Award the unit-completion badge
    badge = BADGE_TEMPLATE.format(unit=current_unit)
    try:
        badges: list[str] = json.loads(profile.badges_json)
    except Exception:
        badges = []
    if badge not in badges:
        badges.append(badge)
    profile.badges_json = json.dumps(badges)

    if current_unit < MAX_UNITS:
        profile.current_unit += 1
        profile.current_lesson = 1
    else:
        raise bad_request("You have completed all available units!")

    account.updated_at = datetime.now(UTC)
    await db.commit()

    out = _profile_out(account)
    if out is None:
        raise bad_request("Profile unavailable after advance")
    return out
