import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest
from app import app as flask_app


@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client


def test_health_returns_200_and_ok(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_greet_returns_message(client):
    res = client.get("/api/greet/John")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Hello, John!"


def test_greet_empty_name_returns_400(client):
    res = client.get("/api/greet/%20")
    assert res.status_code == 400