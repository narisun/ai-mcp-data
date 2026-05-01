# ai-mcp-data — built on the SDK-bundled base image.
# Base image (ghcr.io/narisun/ai-python-base) ships the SDK pre-installed;
# we only add server-specific runtime extras here.
ARG BASE_TAG=3.11-sdk0.5.0
FROM ghcr.io/narisun/ai-python-base:${BASE_TAG}

WORKDIR /app

COPY requirements-runtime.txt .
RUN pip install --no-cache-dir -r requirements-runtime.txt

COPY src/ /app/src/

USER appuser
EXPOSE 8080
CMD ["python", "-m", "src.server"]
