
import socket
import time

from fastapi import FastAPI

app = FastAPI(title="backend")

start_time = time.time()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/info")
def info():
    return {
        "service": "backend",
        "version": "1.0.0",
        "hostname": socket.gethostname(),
        "uptime_seconds": round(time.time() - start_time),
    }


@app.get("/api/items")
def items():
    return {"items": ["apple", "banana", "mango"]}
