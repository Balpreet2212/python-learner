# PyQuest

A story-driven Python learning platform for grades 5–12.

## Quick start (local dev, no Docker)

```bash
# 1. Install backend dependencies
make install

# 2. Copy env file and optionally edit
cp backend/.env.example backend/.env

# 3. Run migrations (creates SQLite DB on first run)
make migrate

# 4. Start both apps
make dev
# Backend:  http://localhost:8000
# Frontend: http://localhost:5173
```

## Quick start (Docker)

```bash
cp backend/.env.example backend/.env
make up     # starts app + postgres + mailpit
# Backend:  http://localhost:8000
# Mail UI:  http://localhost:8025
```

## Common commands

| Command | Purpose |
|---|---|
| `make dev` | Start backend (uvicorn) + frontend (vite) |
| `make test` | Run all tests |
| `make lint` | Lint + typecheck both apps |
| `make migrate` | Run Alembic migrations |
| `make seed` | Seed dev data |
| `make build` | Production build |
| `make up` | Start Docker Compose stack |

## Project layout

```
.
├── backend/          FastAPI app (Python 3.12)
├── frontend/         React 18 + TypeScript + Vite SPA
├── content/          Markdown + YAML lesson content
├── infra/            Deployment config (Dockerfile is in backend/)
├── docs/
│   └── decisions/    Architecture decision records (ADRs)
└── docker-compose.yml
```

## Design document

See `PyQuest_Design_Document.docx` in the project root for the full product and technical specification.
