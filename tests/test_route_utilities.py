from werkzeug.exceptions import HTTPException
from app.routes.route_utilities import validate_models
import pytest
from app.models.planets import Planet

def test_validate_planet(two_saved_planets):
    # Act
    result_planet = validate_models(Planet, 1)

    # Assert
    assert result_planet.id == 1
    assert result_planet.name == "Mercury"
    assert result_planet.description == "The smallest planet in our solar system" 
    assert result_planet.diameter == 4879


def test_validate_planet_missing_record(two_saved_planets):
    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        result_planet = validate_models(Planet, "3")
    
    response = exc_info.value.get_response()
    assert response.status_code == 404

    data = response.get_data(as_text=True)
    assert "Planet with id (3) not found" in data


def test_validate_planet_invalid_id(two_saved_planets):
    # Act & Assert
    with pytest.raises(HTTPException) as exc_info:
        result_planet = validate_models(Planet, "cat")

    # response = exc_info.value.get_response()
    # assert response.status_code == 400

    # data = response.get_data(as_text=True)
    # assert "Planet with id (cat) is invalid" in data