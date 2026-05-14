from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def db_url(self) -> str:
        """Return a SQLAlchemy-compatible async URL.

        Railway (and many PaaS providers) supply DATABASE_URL as
        'postgres://' or 'postgresql://' — both need the '+asyncpg' driver
        suffix for async SQLAlchemy.
        """
        url = self.database_url
        if url.startswith("postgres://"):
            return "postgresql+asyncpg://" + url[len("postgres://"):]
        if url.startswith("postgresql://"):
            return "postgresql+asyncpg://" + url[len("postgresql://"):]
        return url  # already correct (e.g. sqlite+aiosqlite://...)

    # App
    app_env: str = "development"
    secret_key: str = "change-me-in-production"
    domain: str = "pyquest.local"

    # Database
    database_url: str = "sqlite+aiosqlite:///./pyquest_dev.db"

    # Email (stubbed — swap for real Resend config)
    email_provider: str = "console"  # "console" | "resend"
    resend_api_key: str = ""
    email_from: str = "noreply@pyquest.local"

    # Billing (stubbed — swap for real Stripe config)
    billing_provider: str = "stub"  # "stub" | "stripe"
    stripe_secret_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_price_id: str = ""

    # Public base URL for email links — set to your Railway domain in production
    # e.g. https://python-learner-production.up.railway.app
    public_url: str = "http://localhost:5173"

    # CORS — comma-separated origins allowed in production
    allowed_origins: list[str] = []

    # Sessions
    session_max_age: int = 60 * 60 * 24 * 30  # 30 days

    # Content
    content_version: str = "local"
    content_base_url: str = "/content"


settings = Settings()
