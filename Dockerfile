FROM python:3.12-slim

WORKDIR /app

# System deps needed for building some wheels
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Copy source
COPY pyproject.toml .
COPY README.md .
COPY LICENSE .
COPY agentguard/ ./agentguard/
COPY tests/ ./tests/

# Install package (no cache to keep image small)
RUN pip install --no-cache-dir -e .

# Expose API port
EXPOSE 8000

# Default command (overridden by docker‑compose)
CMD ["${repo//-/_}", "run", "--policy", "/app/policy.yaml"]
