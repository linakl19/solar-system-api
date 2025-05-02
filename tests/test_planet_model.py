from app.models.planets import Planet
import pytest

def test_from_dict_returns_planet():
    # Arrange
    planet_data = {
        "name": "Mercury",
        "description": "The smallest planet in our solar system",
        "diameter": 4879
    }
    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Mercury"
    assert new_planet.description == "The smallest planet in our solar system"
    assert new_planet.diameter == 4879



def test_from_dict_with_no_name():
    # Arrange
    planet_data = {
        "description": "The smallest planet in our solar system",
        "diameter": 4879
    }
    # Act & Assert 
    with pytest.raises(KeyError, match = 'name'): 
        new_planet = Planet.from_dict(planet_data)


def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Mercury",
        "diameter": 4879
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_planet = Planet.from_dict(planet_data)

def test_from_dict_with_no_description():
    # Arrange
    planet_data = {
        "name": "Mercury",
        "description": "The smallest planet in our solar system"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'diameter'):
        new_planet = Planet.from_dict(planet_data)
        
        
        
def test_from_dict_with_extra_keys():
    # Arrange
    planet_data = {
        "extra": "some stuff",
        "name": "Mercury",
        "description": "The smallest planet in our solar system",
        "diameter": 4879,
        "another": "last value"
    }

    # Act
    new_planet = Planet.from_dict(planet_data)

    # Assert
    assert new_planet.name == "Mercury"
    assert new_planet.description == "The smallest planet in our solar system"
    assert new_planet.diameter == 4879



#######
def test_to_dict_no_missing_data():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mercury",
                    description="The smallest planet in our solar system",
                    diameter=4879)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "The smallest planet in our solar system"
    assert result["diameter"] == 4879


# ask about missing id??
def test_to_dict_missing_id():
    # Arrange
    test_data = Planet(name="Mercury",
                description="The smallest planet in our solar system",
                diameter=4879)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] is None
    assert result["name"] == "Mercury"
    assert result["description"] == "The smallest planet in our solar system"
    assert result["diameter"] == 4879

def test_to_dict_missing_name():
    # Arrange
    test_data = Planet(id = 1, 
                    description="The smallest planet in our solar system",
                    diameter=4879)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] is None
    assert result["description"] == "The smallest planet in our solar system"
    assert result["diameter"] == 4879


def test_to_dict_missing_description():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mercury",
                    diameter=4879)

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] is None
    assert result["diameter"] == 4879


def test_to_dict_missing_diameter():
    # Arrange
    test_data = Planet(id = 1,
                    name="Mercury",
                    description="The smallest planet in our solar system")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 4
    assert result["id"] == 1
    assert result["name"] == "Mercury"
    assert result["description"] == "The smallest planet in our solar system"
    assert result["diameter"] is None