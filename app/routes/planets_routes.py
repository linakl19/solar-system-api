from flask import Blueprint, request
from app.models.planets import Planet
from ..db import db
# from app.models.planets import list_of_planets

# Create blueprint
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    diameter = request_body["diameter"]
    
    new_planet = Planet(name=name, description=description, diameter=diameter)
    db.session.add(new_planet)
    db.session.commit()
    
    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "diameter": new_planet.diameter 
    }
    return response, 201
    
@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    
    planets_response = []
    
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "diameter": planet.diameter
            }
        )
    return planets_response