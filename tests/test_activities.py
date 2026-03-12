def test_get_activities_returns_expected_catalog(client):
    # Arrange
    expected_count = 9

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == expected_count
    assert "Chess Club" in payload
    assert "participants" in payload["Chess Club"]


def test_get_activities_includes_expected_fields(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    payload = response.json()
    for activity in payload.values():
        assert expected_fields.issubset(activity.keys())
