from flask import Blueprint
from app.models.planets import list_of_planets

# Create blueprint
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# Create endpoints
@planets_bp.get("")
def get_all_planets():
    planets_response = []
    
    for planet in list_of_planets:
        planets_response.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            diameter = planet.diameter 
        ))
    
    return planets_response