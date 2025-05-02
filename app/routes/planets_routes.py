from flask import Blueprint, request, abort, make_response, Response
from app.models.planets import Planet
from ..db import db
# from app.models.planets import list_of_planets







# Create blueprint
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

@planets_bp.post("")
def create_planet():
    request_body = request.get_json()
    try: 
        new_planet = Planet.from_dict(request_body) 
    except KeyError as error: 
        response = {"message": f"Invalid request: missing {error.args[0]}"} 
        abort(make_response(response, 400))

    db.session.add(new_planet)
    db.session.commit()
    return new_planet.to_dict(), 201


@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)
    
    
    name_param = request.args.get("name")
    description_param = request.args.get("description")
    diameter_param = request.args.get("diameter")
    
    if name_param:
        query = query.where(Planet.name.ilike(f"%{name_param}%"))
        
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
        planets_response.append(planet.to_dict())
    return planets_response


# Enpoint to get one plane
@planets_bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_planet(planet_id)

    return planet.to_dict()


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