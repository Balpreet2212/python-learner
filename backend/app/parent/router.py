from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_account, require_csrf
from app.core.errors import forbidden
from app.db.models import Account
from app.db.session import get_db
from app.parent import service
from app.parent.schemas import LinkLearnerRequest, LinkOut, LearnerSummaryOut

router = APIRouter(prefix="/v1/parent", tags=["parent"])


async def _require_parent(
    account: Account = Depends(get_current_account),
) -> Account:
    if account.role != "parent":
        raise forbidden("Parent account required")
    return account


@router.get("/learners", response_model=list[LearnerSummaryOut])
async def list_learners(
    account: Account = Depends(_require_parent),
    db: AsyncSession = Depends(get_db),
) -> list[LearnerSummaryOut]:
    return await service.get_linked_learners(db, account.id)


@router.post("/link", response_model=LinkOut, status_code=201)
async def link_learner(
    body: LinkLearnerRequest,
    account: Account = Depends(_require_parent),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> LinkOut:
    status = await service.link_learner(db, account.id, body.email)
    return LinkOut(status=status)
