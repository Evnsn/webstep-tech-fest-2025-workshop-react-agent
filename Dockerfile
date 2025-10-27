FROM python:3.11-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.4.21 /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH" \
    PORT=7860 \ 
    UV_PROJECT_ENVIRONMENT="/app/.venv"

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends tzdata ca-certificates \
 && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY . .

EXPOSE 7860

CMD ["uv", "run", "--frozen", "python", "-m", "src.app"]