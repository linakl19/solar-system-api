from flask import Blueprint, request, Response, abort, make_response
from app.models.planets import Planet
from app.models.moon import Moon
from ..db import db
from app.routes.route_utilities import validate_models, create_model, get_models_with_filters

bp = Blueprint("planet_bp", __name__, url_prefix="/planets")

@bp.post("")
def create_planet():
    request_body = request.get_json()
    return create_model(Planet, request_body)


@bp.get("")
def get_all_planets():
    return get_models_with_filters(Planet, request.args)


# Enpoint to get one plane
@bp.get("/<planet_id>")
def get_one_planet(planet_id):
    planet = validate_models(Planet, planet_id)

    return planet.to_dict()



# Endpoint to update one planet
@bp.put("/<planet_id>")
def update_one_planet(planet_id):
    planet = validate_models(Planet, planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.diameter = request_body["diameter"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# Endpoint to delete one planet
@bp.delete("/<planet_id>")
def delete_one_planet(planet_id):
    planet = validate_models(Planet, planet_id)

    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


@bp.get("/<planet_id>/moons")
def get_moons_by_planet(planet_id):
    planet = validate_models(Planet, planet_id)
    response = [book.to_dict() for book in planet.moons]
    return response


@bp.post("/<planet_id>/moons")
def create_moon_with_planet(planet_id):
    planet = validate_models(Planet, planet_id)
    
    request_body = request.get_json()
    request_body["planet_id"] = planet.id
    return create_model(Moon, request_body)


