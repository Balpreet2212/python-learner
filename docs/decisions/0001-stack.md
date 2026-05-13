# ADR 0001 — Technology Stack

**Date:** 2026-05-13  
**Status:** Accepted  
**Sections:** §9, §9.1, §9.3, §9.4

---

## Context

PyQuest is a story-driven Python learning platform for grades 5–12. This ADR records the technology choices made for v1 and documents any deviations from the build prompt.

---

## Decisions

### Frontend

| Choice | Library / Tool | Reasoning |
|---|---|---|
| SPA framework | React 18 + TypeScript (strict) | Specified in build prompt. Large ecosystem, stable. |
| Build tool | Vite 5 | Specified. Fast dev HMR, first-class TypeScript. |
| Styling | Tailwind CSS 3 | Specified. Utility-first, easy theme variants for three worlds. |
| Routing | React Router v6 | Specified. |
| Server state | TanStack Query v5 | Specified. No Redux needed for this data shape. |
| Code editor | Monaco (deferred to M4) | Specified. VS Code's editor; first-class keyboard nav and font-size control (§12.1). |
| Runtime validation | Zod | Specified. All API responses validated at the boundary. |
| Python runtime | Pyodide (CDN, lazy) | Specified in §9.3. Loads on first runnable card only. |

### Backend

| Choice | Library / Tool | Reasoning |
|---|---|---|
| Web framework | FastAPI + uvicorn | Specified. Async-first, automatic OpenAPI docs. |
| ORM | SQLAlchemy 2.x (async) | Specified. Supports both Postgres (prod) and SQLite (dev). |
| Migrations | Alembic | Specified. |
| Password hashing | argon2-cffi | Specified (§11.1). |
| Session auth | HttpOnly cookies + CSRF header token | Specified (§11.1). No bearer tokens for browser clients. |
| Email | Stubbed (console logger) → Resend | Stub wired in M1; real provider swapped at M2. |
| Billing | Stubbed → Stripe Checkout + Portal | Stub wired in M1; real Stripe wired at M10. |
| Linter | ruff | Fast; covers flake8 + isort in one pass. |
| Type checker | mypy (strict) | Specified quality bar. |

### Database

| Environment | Database | Notes |
|---|---|---|
| Development | SQLite + aiosqlite | Zero-config local setup. Partitioning not available — see deviation below. |
| Production | PostgreSQL 16 | `progress_event` partitioned by month (§10.3). |

### Infrastructure

| Concern | Choice | Reasoning |
|---|---|---|
| Local dev orchestration | Docker Compose | `app` + `db` (Postgres 16) + `mail` (Mailpit). |
| CI | GitHub Actions | Standard; free for public repos. |
| Deployment | Container-based PaaS (portable) | Dockerfile targets Fly.io / Render / Railway. No provider-specific config baked in. |
| Content delivery | Static files from FastAPI in dev; CDN bucket in prod | §9.5 — content is immutable versioned bundles. |

---

## Deviations from the build prompt

### 1. Progress event partitioning skipped in SQLite dev

**Prompt requirement:** `progress_event` is append-only and partitioned by month (§10.3).  
**Deviation:** PostgreSQL declarative partitioning is only applied in the production schema. The SQLite dev database uses a plain table.  
**Reason:** SQLite does not support declarative table partitioning.  
**Risk:** None in practice — SQLite is only used for local development and test runs. The Alembic migration for PostgreSQL includes the partitioning DDL.

### 2. Streak excluded everywhere

**Doc inconsistency:** §5.3 excludes streaks from v1 but §8.5 lists "current streak" on the parent dashboard.  
**Decision:** Follow §5.3. No streak is tracked or displayed in v1. The parent dashboard (M9) will omit the streak metric. Confirmed with project owner.

### 3. Email provider defaulting to console logger

**Prompt requirement:** Use Resend in prod, Mailpit in dev.  
**Deviation:** Added a third mode (`EMAIL_PROVIDER=console`) that prints emails to stdout. This is the default for local dev without Docker. Mailpit is available via `make up` (Docker Compose).  
**Reason:** Reduces friction for first-time setup without Docker.

### 4. Weekly challenge sandbox choice

**§9.4 requires:** Server-side re-run of hidden tests in a sandbox. Options: managed third-party or containerized worker with `resource.setrlimit`.  
**Decision (to be confirmed at M8):** Default to a sandboxed subprocess using CPython with `resource.setrlimit` (CPU + wall-clock timeout). This avoids vendor dependency and works on Fly.io workers. Will be documented further in `docs/decisions/0008-challenge-sandbox.md`.

---

## Configuration reference

All environment variables are documented in `docs/configuration.md` (created at M2) and in `backend/.env.example`.
