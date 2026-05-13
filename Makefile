.PHONY: dev test lint migrate seed build install help

# Run both apps in development mode (requires tmux or runs sequentially)
dev:
	@echo "Starting PyQuest dev environment..."
	@echo "Backend:  http://localhost:8000"
	@echo "Frontend: http://localhost:5173"
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
	cd frontend && npm run dev

# Run all tests
test:
	cd backend && pytest --cov=app --cov-report=term-missing -q
	cd frontend && npm run typecheck

# Lint both apps
lint:
	cd backend && ruff check . && mypy app
	cd frontend && npm run lint && npm run typecheck

# Run database migrations (Alembic)
migrate:
	cd backend && alembic upgrade head

# Seed the database with dev data
seed:
	cd backend && python -m app.db.seed

# Build production artefacts
build:
	cd frontend && npm run build
	cd backend && pip install --no-cache-dir -e .

# Install dependencies for both apps
install:
	cd backend && pip install -e ".[dev]"
	cd frontend && npm install

# Docker Compose shortcuts
up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

help:
	@echo "PyQuest Makefile targets:"
	@echo "  make dev      - Start backend + frontend in dev mode"
	@echo "  make test     - Run all tests"
	@echo "  make lint     - Lint + typecheck both apps"
	@echo "  make migrate  - Run Alembic migrations"
	@echo "  make seed     - Seed development data"
	@echo "  make build    - Build production artefacts"
	@echo "  make install  - Install all dependencies"
	@echo "  make up       - Start Docker Compose stack"
	@echo "  make down     - Stop Docker Compose stack"
