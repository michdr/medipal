FROM python:3.11-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY . .
RUN uv sync --frozen --no-dev
ENV NANOBOT_CONFIG_DIR=/app
ENV PORT=8080
EXPOSE ${PORT}
CMD ["nanobot", "gateway"]
