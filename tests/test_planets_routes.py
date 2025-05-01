def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


# 1.GET /planets/1 returns a response body that matches our fixture
def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Mercury",
        "description": "The smallest planet in our solar system",
        "diameter": 4879
    }

# 2. GET /planets/1 with no data in test database returns a 404
def test_get_one_planet_returns_not_found(client, two_saved_planets):
    # Act
    response = client.get("/planets/10")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {
        "message": "Planet with id (10) not found"
    }

# 3. GET /planets with valid test data returns a 200 with data
def test_get_all_planets_returns_array_with_data(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "name": "Mercury", 
            "description": "The smallest planet in our solar system", 
            "diameter": 4879
        },
        {
            "id": 2,
            "name": "Venus", 
            "description": "The second planet from the Sun.", 
            "diameter": 12104
        }
    ]

# 4. POST /planets with a JSON request body returns a 201
# Without two_saved_planets the id will be 1 bcs empty table
def test_creates_one_planet_returns_status_created(client, two_saved_planets):
    # Act
    response = client.post("/planets", json={
        "name":"Earth", 
        "description":"The third planet from the Sun and the only known planet to support life.", 
        "diameter":12756
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 3,
        "name":"Earth", 
        "description":"The third planet from the Sun and the only known planet to support life.", 
        "diameter":12756
    }
