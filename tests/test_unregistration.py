from src.app import activities


def test_unregister_participant_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    route = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(route, params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in activities[activity_name]["participants"]


def test_unregister_unknown_activity_returns_not_found(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    route = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(route, params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload["detail"] == "Activity not found"


def test_unregister_non_member_returns_not_found(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not-enrolled@mergington.edu"
    route = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(route, params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload["detail"] == "Participant not found in this activity"
