import os
import requests
import pytest

BASE_URL = os.environ.get("APP_BASE_URL", "http://localhost:8080")


def test_app_is_available():
    """Vérifie la disponibilité de l'application (page d'accueil)."""
    res = requests.get(BASE_URL, timeout=10)
    assert res.status_code == 200
    assert "MyApp" in res.text


def test_health_endpoint():
    res = requests.get(f"{BASE_URL}/health", timeout=10)
    assert res.status_code == 200
    assert res.json()["status"] == "ok"


def test_greet_endpoint_functional_flow():
    """Parcours réel : appel d'une fonctionnalité en plus du /health."""
    res = requests.get(f"{BASE_URL}/api/greet/Alice", timeout=10)
    assert res.status_code == 200
    assert res.json()["message"] == "Hello, Alice!"

### rien de ouf quoi ;)
def test_greet_endpoint_error_case():
    res = requests.get(f"{BASE_URL}/api/greet/%20", timeout=10)
    assert res.status_code == 400