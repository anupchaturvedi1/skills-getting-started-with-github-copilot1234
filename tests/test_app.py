from fastapi.testclient import TestClient

from src import app as app_module


def test_unregister_participant_removes_email_from_activity():
    # Arrange
    client = TestClient(app_module.app)
    activity_name = "Chess Club"
    email = "daniel@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    # Assert
    assert response.status_code == 200
    assert email not in app_module.activities[activity_name]["participants"]
    assert "michael@mergington.edu" in app_module.activities[activity_name]["participants"]


def test_unregister_participant_returns_404_for_unknown_activity():
    # Arrange
    client = TestClient(app_module.app)
    activity_name = "Unknown"
    email = "test@example.com"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    # Assert
    assert response.status_code == 404
