"""Stripe billing routes — checkout, webhook, portal, status."""

import uuid
from datetime import UTC, datetime

import stripe
from fastapi import APIRouter, Depends, Header, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.dependencies import get_current_account, require_csrf
from app.config import settings
from app.core.errors import bad_request, forbidden
from app.db.models import Account, Subscription
from app.db.session import get_db

router = APIRouter(prefix="/v1/billing", tags=["billing"])

# Free tier: unit 1 lessons 1 and 2 + daily challenge only
FREE_UNIT = 1
FREE_LESSONS = {1, 2}


def has_full_access(account: Account) -> bool:
    """True if the account has an active paid subscription."""
    if account.subscription is None:
        return False
    return account.subscription.status in ("active", "past_due")


def is_free_lesson(unit: int, lesson: int) -> bool:
    return unit == FREE_UNIT and lesson in FREE_LESSONS


# ── Schemas ───────────────────────────────────────────────────────────────────


class BillingStatusOut(BaseModel):
    status: str          # "none" | "active" | "past_due" | "cancelled" | "trial"
    has_full_access: bool
    trial_ends_at: datetime | None = None
    current_period_end: datetime | None = None


class CheckoutOut(BaseModel):
    checkout_url: str


class PortalOut(BaseModel):
    portal_url: str


# ── Endpoints ─────────────────────────────────────────────────────────────────


@router.get("/status")
async def get_billing_status(
    account: Account = Depends(get_current_account),
) -> BillingStatusOut:
    if account.subscription is None:
        return BillingStatusOut(status="none", has_full_access=False)
    sub = account.subscription
    return BillingStatusOut(
        status=sub.status,
        has_full_access=sub.status in ("active", "past_due"),
        trial_ends_at=sub.trial_ends_at,
        current_period_end=sub.current_period_end,
    )


@router.post("/checkout")
async def create_checkout_session(
    account: Account = Depends(get_current_account),
    db: AsyncSession = Depends(get_db),
    _csrf: None = Depends(require_csrf),
) -> CheckoutOut:
    if not settings.stripe_secret_key:
        raise bad_request("Billing not configured")
    if has_full_access(account):
        raise bad_request("You already have an active subscription")

    stripe.api_key = settings.stripe_secret_key
    session = stripe.checkout.Session.create(
        customer_email=account.email,
        payment_method_types=["card"],
        line_items=[{"price": settings.stripe_price_id, "quantity": 1}],
        mode="subscription",
        success_url=f"{settings.public_url}/dashboard/billing?success=1",
        cancel_url=f"{settings.public_url}/dashboard/billing",
        client_reference_id=str(account.id),
        metadata={"account_id": str(account.id)},
    )
    return CheckoutOut(checkout_url=session.url)


@router.post("/portal")
async def create_portal_session(
    account: Account = Depends(get_current_account),
    _csrf: None = Depends(require_csrf),
) -> PortalOut:
    if not settings.stripe_secret_key:
        raise bad_request("Billing not configured")
    if account.subscription is None or not account.subscription.provider_customer_id:
        raise bad_request("No active subscription found")

    stripe.api_key = settings.stripe_secret_key
    session = stripe.billing_portal.Session.create(
        customer=account.subscription.provider_customer_id,
        return_url=f"{settings.public_url}/dashboard/billing",
    )
    return PortalOut(portal_url=session.url)


@router.post("/webhook")
async def stripe_webhook(
    request: Request,
    stripe_signature: str = Header(alias="stripe-signature", default=""),
    db: AsyncSession = Depends(get_db),
) -> dict[str, str]:
    if not settings.stripe_webhook_secret:
        raise HTTPException(status_code=400, detail="Webhook not configured")

    payload = await request.body()
    try:
        event = stripe.Webhook.construct_event(
            payload, stripe_signature, settings.stripe_webhook_secret
        )
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    stripe.api_key = settings.stripe_secret_key

    if event["type"] == "checkout.session.completed":
        session_obj = event["data"]["object"]
        account_id_str = session_obj.get("client_reference_id") or session_obj.get("metadata", {}).get("account_id")
        if not account_id_str:
            return {"status": "skipped"}

        account_id = uuid.UUID(account_id_str)
        stripe_sub_id = session_obj.get("subscription")
        stripe_customer_id = session_obj.get("customer")

        sub = await db.get(Subscription, account_id)
        if sub is None:
            sub = Subscription(
                account_id=account_id,
                status="active",
                provider_customer_id=stripe_customer_id,
                provider_subscription_id=stripe_sub_id,
                updated_at=datetime.now(UTC),
            )
            db.add(sub)
        else:
            sub.status = "active"
            sub.provider_customer_id = stripe_customer_id
            sub.provider_subscription_id = stripe_sub_id
            sub.updated_at = datetime.now(UTC)
        await db.commit()

    elif event["type"] in ("customer.subscription.updated", "customer.subscription.deleted"):
        stripe_sub = event["data"]["object"]
        result = await db.execute(
            select(Subscription).where(
                Subscription.provider_subscription_id == stripe_sub["id"]
            )
        )
        sub = result.scalar_one_or_none()
        if sub is not None:
            if event["type"] == "customer.subscription.deleted":
                sub.status = "cancelled"
            else:
                sub.status = stripe_sub["status"]
                if stripe_sub.get("current_period_end"):
                    sub.current_period_end = datetime.fromtimestamp(
                        stripe_sub["current_period_end"], tz=UTC
                    )
            sub.updated_at = datetime.now(UTC)
            await db.commit()

    elif event["type"] == "invoice.payment_failed":
        invoice = event["data"]["object"]
        stripe_sub_id = invoice.get("subscription")
        if stripe_sub_id:
            result = await db.execute(
                select(Subscription).where(
                    Subscription.provider_subscription_id == stripe_sub_id
                )
            )
            sub = result.scalar_one_or_none()
            if sub is not None:
                sub.status = "past_due"
                sub.updated_at = datetime.now(UTC)
                await db.commit()

    return {"status": "ok"}
