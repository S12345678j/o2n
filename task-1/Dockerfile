# ---------- Stage 1: Build ----------
FROM python:3.12-slim AS builder

WORKDIR /app

# Install system dependencies (minimal)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies into a separate folder
RUN pip install --user --no-cache-dir -r requirements.txt

# ---------- Stage 2: Runtime ----------
FROM python:3.12-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local

# Add app source code
COPY . .

# Ensure PATH includes installed packages
ENV PATH=/root/.local/bin:$PATH

# Environment variables (can override at runtime)
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Expose port
EXPOSE 5000

# Healthcheck (optional but recommended)
HEALTHCHECK CMD curl --fail http://localhost:5000/healthcheck || exit 1

# Run app
CMD ["python", "run.py"]
