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
from app.db.models import Account, ProgressEvent
from app.db.session import get_db

router = APIRouter(prefix="/v1/learner", tags=["content"])

BADGE_TEMPLATE = "unit_{unit}_complete"


# ── Response schemas ──────────────────────────────────────────────────────────


class ExampleOut(BaseModel):
    code: str
    explanation: str
    output: str


class FinalChallengeOut(BaseModel):
    prompt: str
    code_starter: str
    hints: list[str]
    test_count: int


class PredictCardOut(BaseModel):
    code: str


class BreakAndFixOut(BaseModel):
    broken_code: str
    hint: str
    test_count: int


class LessonOut(BaseModel):
    unit: int
    lesson: int
    title: str
    setup: str
    example: ExampleOut
    code_starter: str
    hints: list[str]
    xp: int
    test_count: int
    total_lessons: int
    final_challenge: FinalChallengeOut
    predict: PredictCardOut | None = None
    break_and_fix: BreakAndFixOut | None = None


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


class PredictCheckRequest(BaseModel):
    answer: str


class PredictCheckOut(BaseModel):
    correct: bool
    actual_output: str
    explanation: str


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
        setup=content.setup,
        example=ExampleOut(
            code=content.example.code,
            explanation=content.example.explanation,
            output=content.example.output,
        ),
        code_starter=content.code_starter,
        hints=content.hints,
        xp=content.xp,
        test_count=len(content.tests),
        total_lessons=content.total_lessons,
        final_challenge=FinalChallengeOut(
            prompt=content.final_challenge.prompt,
            code_starter=content.final_challenge.code_starter,
            hints=content.final_challenge.hints,
            test_count=len(content.final_challenge.tests),
        ),
        predict=PredictCardOut(code=content.predict.code) if content.predict else None,
        break_and_fix=BreakAndFixOut(
            broken_code=content.break_and_fix.broken_code,
            hint=content.break_and_fix.hint,
            test_count=len(content.break_and_fix.tests),
        ) if content.break_and_fix else None,
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


@router.post("/final/submit")
async def submit_final(
    body: SubmitRequest,
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> SubmitOut:
    if account.role != "learner":
        raise forbidden("Only learner accounts can submit")
    if len(body.code) > 10_000:
        raise bad_request("Code submission too large")

    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before submitting")

    content = load_lesson(profile.current_unit, profile.current_lesson, profile.world)
    if content is None:
        raise bad_request("Lesson content not found")

    tests = [{"code": t.code, "message": t.message} for t in content.final_challenge.tests]
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


@router.post("/predict/check")
async def check_predict(
    body: PredictCheckRequest,
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> PredictCheckOut:
    if account.role != "learner":
        raise forbidden("Only learner accounts can check predictions")

    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before checking predictions")

    content = load_lesson(profile.current_unit, profile.current_lesson, profile.world)
    if content is None or content.predict is None:
        raise bad_request("No predict card for this lesson")

    result = run_challenge(content.predict.code, [])
    actual = result.stdout.strip()
    correct = actual == body.answer.strip()
    return PredictCheckOut(
        correct=correct,
        actual_output=actual,
        explanation=content.predict.explanation,
    )


@router.post("/fix/submit")
async def submit_fix(
    body: SubmitRequest,
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> SubmitOut:
    if account.role != "learner":
        raise forbidden("Only learner accounts can submit fixes")
    if len(body.code) > 10_000:
        raise bad_request("Code submission too large")

    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before submitting")

    content = load_lesson(profile.current_unit, profile.current_lesson, profile.world)
    if content is None or content.break_and_fix is None:
        raise bad_request("No break-and-fix card for this lesson")

    tests = [{"code": t.code, "message": t.message} for t in content.break_and_fix.tests]
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
    """Advance to the next lesson. Must complete the final challenge first."""
    if account.role != "learner":
        raise forbidden("Only learner accounts can advance lessons")

    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before advancing lessons")

    completed_lesson = profile.current_lesson
    if profile.current_lesson < LESSONS_PER_UNIT:
        profile.current_lesson += 1
    else:
        raise bad_request("Complete the unit capstone to advance to the next unit")

    db.add(ProgressEvent(
        account_id=account.id,
        event_type="lesson_complete",
        unit=profile.current_unit,
        lesson=completed_lesson,
        created_at=datetime.now(UTC),
    ))
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

    db.add(ProgressEvent(
        account_id=account.id,
        event_type="unit_complete",
        unit=current_unit,
        created_at=datetime.now(UTC),
    ))
    account.updated_at = datetime.now(UTC)
    await db.commit()

    out = _profile_out(account)
    if out is None:
        raise bad_request("Profile unavailable after advance")
    return out
