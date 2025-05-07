import site


def test_create_one_moon(client):
    # Act
    response = client.post("/moons", json={
        "size": 9000,
        "description": "Closest moon to earth",
        "discovered_at": 250,
    })

    response_body = response.get_json()
    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "size": 9000,
        "description": "Closest moon to earth",
        "discovered_at": 250,
        "planet": None
    }


def test_create_one_moon_no_size(client):
    # Arrange
    test_data = {
        "description": "Closest moon to earth",
        "discovered_at": 250,
    }
    # Act
    response = client.post("/moons", json=test_data)
    response_body = response.get_json()
    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing size'}


def test_create_one_moon_with_extra_keys(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "size": 9000,
        "description": "Closest moon to earth",
        "discovered_at": 250,
        "another": "last value"
    }
    # Act
    response = client.post("/moons", json=test_data)
    response_body = response.get_json()
    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "size": 9000,
        "description": "Closest moon to earth",
        "discovered_at": 250,
        "planet": None
    }

def test_get_all_moons_two_saved_moons(client, two_saved_moons):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
            "id": 1,
            "size": 3125,
            "description": "Frozen surface with possible ocean beneath",
            "discovered_at": 1610, 
            "planet": None
        }
    assert response_body[1] == {
        "id": 2,
        "size": 1737,
        "description": "Rocky surface with many craters",
        "discovered_at": -4000, 
        "planet": None
    }


def test_get_all_moons_no_saved_moon(client):
    # Act
    response = client.get("/moons")
    response_body = response.get_json()
    # Assert
    assert response.status_code == 200
    assert response_body == []



