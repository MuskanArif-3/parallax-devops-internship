# Frontend service 🌐
# A simple web server built with FastAPI.
# It shows a web page and talks to the backend service.

import json
import os
import socket
import time
import urllib.request

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="frontend")

start_time = time.time()

# Backend address. Default works with Docker network (container name "backend")
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")


# Used by Docker/Kubernetes to check if the service is alive
@app.get("/health")
def health():
    return {"status": "ok"}


# Basic details about this service
@app.get("/info")
def info():
    return {
        "service": "frontend",
        "version": "1.0.0",
        "hostname": socket.gethostname(),
        "uptime_seconds": round(time.time() - start_time),
    }


# Home page: calls the backend and shows its answer
@app.get("/", response_class=HTMLResponse)
def home():
    try:
        # Ask the backend for its info (wait max 2 seconds)
        with urllib.request.urlopen(BACKEND_URL + "/info", timeout=2) as res:
            data = json.loads(res.read())
        status = "connected ✅"
    except Exception as e:
        # If backend is down, still show the page
        data = {"error": str(e)}
        status = "not reachable ❌"

    return f"""
    <html>
      <body style="font-family: sans-serif; max-width: 600px; margin: 40px auto;">
        <h1>Frontend Service</h1>
        <p>Backend status: <b>{status}</b></p>
        <pre>{json.dumps(data, indent=2)}</pre>
      </body>
    </html>
    """
