# ── Stage 1: build the React frontend ─────────────────────────────────────────
FROM node:20-slim AS frontend
WORKDIR /build
COPY frontend/package*.json ./
RUN npm ci
COPY frontend/ ./
RUN npm run build

# ── Stage 2: Python backend + built frontend ───────────────────────────────────
FROM python:3.12-slim
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY backend/pyproject.toml ./
RUN pip install --no-cache-dir -e .

# Copy backend source
COPY backend/ ./

# Copy content YAML files (loaded at runtime by app/content/service.py)
COPY content/ /content

# Copy built frontend into the package's static/ dir so FastAPI serves it
COPY --from=frontend /build/dist ./app/static

EXPOSE 8000

# Run migrations with a 60s timeout so a hanging DB connection never blocks startup
CMD ["sh", "-c", "timeout 60 alembic upgrade head || echo 'WARNING: migration skipped'; exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
