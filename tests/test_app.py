import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_train_endpoint_no_files():
    response = client.post("/train", json={}, files=[])
    # Since endpoint expects files, it should return 422 validation error
    assert response.status_code == 422

def test_predict_without_model():
    response = client.post("/predict", json={"data": [0.5, 1.2]})
    # Should raise runtime error, FastAPI returns 500
    assert response.status_code == 500
