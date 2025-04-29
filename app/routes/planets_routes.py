from flask import Blueprint, request, abort, make_response, Response
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
    query = db.select(Planet)
    
    description_param = request.args.get("description")
    diameter_param = request.args.get("diameter")
    
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
    if diameter_param:
        # query = query.where(Planet.diameter == diameter_param)
        # query = query.where((Planet.diameter >= input - tolerance) & (Planet.diameter <= input + tolerance))
        
        tolerance = 1000
        diameter = int(diameter_param)
        
        query = query.where(Planet.diameter.between(diameter - tolerance, diameter + tolerance))
        
    query = query.order_by(Planet.id)
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


# Enpoint to get one planet
@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return {
        "id": planet.id,
        "name": planet.name ,
        "description": planet.description,
        "diameter": planet.diameter,
    }


# Endpoint to update one planet
@planets_bp.put("/<planet_id>")
def update_one_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter = request_body["diameter"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# Endpoint to delete one planet
@planets_bp.delete("/<planet_id>")
def delete_one_planet(planet_id):
    planet = validate_planet(planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# Validate planet - helper function
def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"Planet with id ({planet_id}) is invalid"}
        abort(make_response(response, 400))
    
    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)

    if not planet:
        response = {"message": f"Planet with id ({planet_id}) not found"}
        abort(make_response(response, 404))
    
    return planet