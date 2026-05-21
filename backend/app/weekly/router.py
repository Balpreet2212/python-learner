"""Weekly challenge routes."""

from datetime import UTC, datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_account, require_csrf
from app.content.service import load_weekly_challenge
from app.core.errors import bad_request, forbidden
from app.core.sandbox import run_challenge
from app.db.models import Account, WeeklyAttempt
from app.db.session import get_db

router = APIRouter(prefix="/v1/weekly", tags=["weekly"])


# ── Schemas ───────────────────────────────────────────────────────────────────


class WeeklyChallengeOut(BaseModel):
    challenge_index: int
    week_key: str
    title: str
    description: str
    code_starter: str
    hints: list[str]
    xp: int
    difficulty: str
    test_count: int
    already_passed: bool


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


# ── Endpoints ─────────────────────────────────────────────────────────────────


@router.get("/challenge")
async def get_weekly_challenge(
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
) -> WeeklyChallengeOut:
    if account.role != "learner":
        raise forbidden("Only learner accounts have weekly challenges")
    if account.profile is None:
        await db.refresh(account, ["profile"])
    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before accessing weekly challenges")

    content = load_weekly_challenge(profile.world)
    if content is None:
        raise bad_request("No weekly challenge available")

    stmt = select(WeeklyAttempt).where(
        WeeklyAttempt.account_id == account.id,
        WeeklyAttempt.week_key == content.week_key,
        WeeklyAttempt.passed.is_(True),
    )
    already_passed = (await db.execute(stmt)).scalar_one_or_none() is not None

    return WeeklyChallengeOut(
        challenge_index=content.challenge_index,
        week_key=content.week_key,
        title=content.title,
        description=content.description,
        code_starter=content.code_starter,
        hints=content.hints,
        xp=content.xp,
        difficulty=content.difficulty,
        test_count=len(content.tests),
        already_passed=already_passed,
    )


@router.post("/submit")
async def submit_weekly(
    body: SubmitRequest,
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> SubmitOut:
    if account.role != "learner":
        raise forbidden("Only learner accounts can submit weekly challenges")
    if len(body.code) > 10_000:
        raise bad_request("Code submission too large")

    profile = account.profile
    if profile is None or not profile.track:
        raise bad_request("Complete onboarding before submitting")

    content = load_weekly_challenge(profile.world)
    if content is None:
        raise bad_request("No weekly challenge available")

    tests = [{"code": t.code, "message": t.message} for t in content.tests]
    result = run_challenge(body.code, tests)

    if result.all_passed:
        # Record attempt only if not already passed this week
        stmt = select(WeeklyAttempt).where(
            WeeklyAttempt.account_id == account.id,
            WeeklyAttempt.week_key == content.week_key,
            WeeklyAttempt.passed.is_(True),
        )
        existing = (await db.execute(stmt)).scalar_one_or_none()
        if existing is None:
            db.add(WeeklyAttempt(
                account_id=account.id,
                challenge_index=content.challenge_index,
                week_key=content.week_key,
                passed=True,
                created_at=datetime.now(UTC),
            ))
            await db.commit()

    return SubmitOut(
        all_passed=result.all_passed,
        exec_error=result.exec_error,
        stdout=result.stdout,
        tests=[
            TestResultOut(passed=bool(t["passed"]), message=str(t["message"]))
            for t in result.tests
        ],
    )
