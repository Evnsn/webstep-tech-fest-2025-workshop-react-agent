FROM python:3.11-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.4.21 /uv /uvx /bin/

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=7860

RUN useradd -u 1000 -m appuser

ENV UV_PROJECT_ENVIRONMENT="/home/appuser/.venv" \
    PATH="/home/appuser/.venv/bin:$PATH" 

WORKDIR /app

RUN apt-get update \
 && apt-get install -y --no-install-recommends tzdata ca-certificates \
 && rm -rf /var/lib/apt/lists/*

USER 1000

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev

COPY --chown=1000:1000 . .

EXPOSE 7860

CMD ["uv", "run", "--frozen", "python", "-m", "src.app"]