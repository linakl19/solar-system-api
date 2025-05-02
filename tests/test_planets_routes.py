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



def test_create_one_planet_no_name(client):
    # Arrange
    test_data = { 
        "description":"The third planet from the Sun and the only known planet to support life.", 
        "diameter":12756
        }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing name'}





def test_create_one_planet_no_description(client):
    test_data = { 
        "name":"Earth", 
        "diameter":12756
        }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing description'}

def test_create_one_book_with_extra_keys(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "name":"Earth", 
        "description":"The third planet from the Sun and the only known planet to support life.", 
        "diameter":12756,
        "another": "last value"
    }

    # Act
    response = client.post("/planets", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name":"Earth", 
        "description":"The third planet from the Sun and the only known planet to support life.", 
        "diameter":12756
    }
    
    # GET edge cases
def test_get_all_planets_with_two_records(client, two_saved_planets):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0] == {
            "id": 1,
            "name": "Mercury", 
            "description": "The smallest planet in our solar system", 
            "diameter": 4879
        }
    assert response_body[1] == {
            "id": 2,
            "name": "Venus", 
            "description": "The second planet from the Sun.", 
            "diameter": 12104
        }

# 
def test_get_all_planets_with_title_query_matching_none(client, two_saved_planets):
    # Act
    data = {'name': 'Desert Planet'}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# # When we have records and a `title` query in the request arguments, `get_all_books` returns a list containing only the `Book`s that match the query
def test_get_all_books_with_title_query_matching_one(client, two_saved_planets):
    # Act
    data = {'name': "Mercury"}
    response = client.get("/planets", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
            "id": 1,
            "name": "Mercury", 
            "description": "The smallest planet in our solar system", 
            "diameter": 4879
        }

# # When we call `get_one_book` with a numeric ID that doesn't have a record, we get the expected error message
def test_get_one_planet_missing_record(client, two_saved_planets):
    # Act
    response = client.get("/planets/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Planet with id (3) not found"}

# When we call `get_one_book` with a non-numeric ID, we get the expected error message
def test_get_one_planet_invalid_id(client, two_saved_planets):
    # Act
    response = client.get("/planets/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Planet with id (cat) is invalid"}