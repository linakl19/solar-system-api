#########
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
# def test_to_dict_no_missing_data():
#     # Arrange
#     test_data = Book(id = 1,
#                     title="Ocean Book",
#                     description="watr 4evr")

#     # Act
#     result = test_data.to_dict()

#     # Assert
#     assert len(result) == 3
#     assert result["id"] == 1
#     assert result["title"] == "Ocean Book"
#     assert result["description"] == "watr 4evr"



# def test_to_dict_missing_id():
#     # Arrange
#     test_data = Book(title="Ocean Book",
#                     description="watr 4evr")

#     # Act
#     result = test_data.to_dict()

#     # Assert
#     assert len(result) == 3
#     assert result["id"] is None
#     assert result["title"] == "Ocean Book"
#     assert result["description"] == "watr 4evr"

# def test_to_dict_missing_title():
#     # Arrange
#     test_data = Book(id=1,
#                     description="watr 4evr")

#     # Act
#     result = test_data.to_dict()

#     # Assert
#     assert len(result) == 3
#     assert result["id"] == 1
#     assert result["title"] is None
#     assert result["description"] == "watr 4evr"

# def test_to_dict_missing_description():
#     # Arrange
#     test_data = Book(id = 1,
#                     title="Ocean Book")

#     # Act
#     result = test_data.to_dict()

#     # Assert
#     assert len(result) == 3
#     assert result["id"] == 1
#     assert result["title"] == "Ocean Book"
#     assert result["description"] is None