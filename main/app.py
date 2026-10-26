
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="DevOps Serving API", version="1.0.0")

Instrumentator().instrument(app).expose(
    app, endpoint="/metrics", include_in_schema=False
)


@app.get("/")
def home():
    return {"service": "devops-serving-api", "status": "running"}


@app.get("/healthz")
def health():
    return {"status": "healthy"}


@app.get("/readyz")
def ready():
    return {"status": "ready"}


@app.post("/generate")
def generate(payload: dict):
    prompt = str(payload.get("prompt", "")).strip()

    if not prompt:
        return {"error": "prompt is required"}

    # Demo only: replace with an actual LLM inference client later.
    return {
        "response": f"Demo response for: {prompt[:200]}",
        "model": "demo-model"
    }
