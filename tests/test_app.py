import pytest
from fastapi.testclient import TestClient

from src import app as app_module


@pytest.fixture(autouse=True)
def reset_state():
    app_module.activities["Chess Club"]["participants"] = ["michael@mergington.edu", "daniel@mergington.edu"]
    yield


def test_unregister_participant_removes_email_from_activity():
    client = TestClient(app_module.app)

    response = client.delete("/activities/Chess Club/participants/daniel@mergington.edu")

    assert response.status_code == 200
    assert "daniel@mergington.edu" not in app_module.activities["Chess Club"]["participants"]
    assert "michael@mergington.edu" in app_module.activities["Chess Club"]["participants"]


def test_unregister_participant_returns_404_for_unknown_activity():
    client = TestClient(app_module.app)

    response = client.delete("/activities/Unknown/participants/test@example.com")

    assert response.status_code == 404
