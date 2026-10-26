
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_health():
    assert client.get("/healthz").status_code == 200


def test_readiness():
    assert client.get("/readyz").json()["status"] == "ready"


def test_generate():
    response = client.post(
        "/generate", json={"prompt": "Explain Kubernetes"}
    )
    assert response.status_code == 200
    assert response.json()["model"] == "demo-model"


def test_generate_rejects_empty_prompt():
    response = client.post("/generate", json={"prompt": "  "})
    assert response.json()["error"] == "prompt is required"
