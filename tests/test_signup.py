from src.app import activities


def test_signup_for_activity_success(client):
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"
    route = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(route, params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert payload["message"] == f"Signed up {email} for {activity_name}"
    assert email in activities[activity_name]["participants"]


def test_signup_for_activity_rejects_duplicate(client):
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"
    route = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(route, params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 400
    assert payload["detail"] == "Student already signed up for this activity"


def test_signup_for_unknown_activity_returns_not_found(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"
    route = f"/activities/{activity_name}/signup"

    # Act
    response = client.post(route, params={"email": email})
    payload = response.json()

    # Assert
    assert response.status_code == 404
    assert payload["detail"] == "Activity not found"
