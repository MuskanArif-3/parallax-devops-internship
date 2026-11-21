# Backend service 🛠️
# A small JSON API built with FastAPI.
# It has 2 required endpoints (/health and /info) and one extra (/api/items).

import socket
import time

from fastapi import FastAPI

# Create the app
app = FastAPI(title="backend")

# Remember when the server started, so /info can show uptime
start_time = time.time()


# Used by Docker/Kubernetes to check if the service is alive
@app.get("/health")
def health():
    return {"status": "ok"}


# Basic details about this service
@app.get("/info")
def info():
    return {
        "service": "backend",
        "version": "1.0.0",
        "hostname": socket.gethostname(),  # container name/ID
        "uptime_seconds": round(time.time() - start_time),
    }


# Extra endpoint with fake data, just to show the API works
@app.get("/api/items")
def items():
    return {"items": ["apple", "banana", "mango"]}
