FROM python:3.11-slim

WORKDIR /app

# Create non-root user for security (before installing dependencies)
RUN groupadd --system --gid 1001 python && \
    useradd --system --uid 1001 --gid python python

# Upgrade pip
RUN pip install --upgrade pip

# Copy ONLY dependency files first (for layer caching)
COPY requirements.txt pyproject.toml ./

# Install dependencies (this layer is cached unless deps change)
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code AFTER deps installed (code changes don't bust dep cache)
COPY --chown=python:python src/ ./src/

# Change ownership to non-root user
RUN chown -R python:python /app

USER python

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

LABEL maintainer="Phase Backend Team" \
      version="1.0" \
      description="Production build of Phase backend application"

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1