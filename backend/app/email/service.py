"""Email service — console stub by default; swap EMAIL_PROVIDER=resend for production.

The interface here is intentionally thin so the LLM tutor (§13.1) and other
future features can send email without touching provider details.
"""

import logging

import httpx

from app.config import settings

logger = logging.getLogger(__name__)


async def _send_console(to: str, subject: str, html: str) -> None:
    logger.info("EMAIL to=%s subject=%r", to, subject)
    # Print a text-mode version to stdout for dev convenience
    text = html.replace("<br>", "\n").replace("</p>", "\n")
    print(f"\n{'='*60}\nTO: {to}\nSUBJECT: {subject}\n{'-'*60}\n{text}\n{'='*60}\n")


async def _send_resend(to: str, subject: str, html: str) -> None:
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {settings.resend_api_key}"},
            json={"from": settings.email_from, "to": [to], "subject": subject, "html": html},
            timeout=10,
        )
        resp.raise_for_status()


async def send_email(to: str, subject: str, html: str) -> None:
    if settings.email_provider == "resend":
        await _send_resend(to, subject, html)
    else:
        await _send_console(to, subject, html)


async def send_verification_email(to: str, token: str) -> None:
    link = f"http://{settings.domain}:5173/auth/verify-email?token={token}"
    await send_email(
        to=to,
        subject="Verify your PyQuest email",
        html=(
            f"<p>Welcome to PyQuest! Click the link below to verify your email address.</p>"
            f"<p><a href='{link}'>{link}</a></p>"
            f"<p>This link expires in 24 hours.</p>"
        ),
    )


async def send_parent_invite_email(parent_email: str, learner_display: str, token: str) -> None:
    link = f"http://{settings.domain}:5173/auth/parent-verify?token={token}"
    await send_email(
        to=parent_email,
        subject="Your child wants to join PyQuest",
        html=(
            f"<p>{learner_display} has signed up for PyQuest and listed you as their parent.</p>"
            "<p>PyQuest teaches Python through story-driven adventures for grades 5-12.</p>"
            "<p>Click below to verify their account and set up your parent dashboard:</p>"
            f"<p><a href='{link}'>{link}</a></p>"
            "<p>This link expires in 7 days. Ignore this email if unexpected.</p>"
        ),
    )


async def send_password_reset_email(to: str, token: str) -> None:
    link = f"http://{settings.domain}:5173/auth/reset-password?token={token}"
    await send_email(
        to=to,
        subject="Reset your PyQuest password",
        html=(
            f"<p>Click the link below to reset your password. This link expires in 1 hour.</p>"
            f"<p><a href='{link}'>{link}</a></p>"
            f"<p>If you did not request a password reset, you can ignore this email.</p>"
        ),
    )
