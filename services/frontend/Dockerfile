# ---------- Stage 1: builder ----------
# Install the python packages here, so the final image stays small
FROM python:3.12-slim AS builder
WORKDIR /build
COPY requirements.txt .
 RUN pip install --no-cache-dir --default-timeout=100 --retries=5 --prefix=/install -r requirements.txt

# ---------- Stage 2: final image ----------
# Only copy what we need to run the app
FROM python:3.12-slim
WORKDIR /app

# Copy installed packages from stage 1
COPY --from=builder /install /usr/local

# Copy our code and give ownership to user 1001
COPY --chown=1001:1001 app ./app

# Do not run as root (security rule) 🔒
USER 1001

EXPOSE 8080

# Start the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
