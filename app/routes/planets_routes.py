from flask import Blueprint, abort, make_response
# from app.models.planets import list_of_planets

# Create blueprint
planets_bp = Blueprint("planets_bp", __name__, url_prefix="/planets")

# Create endpoints
# @planets_bp.get("")
# def get_all_planets():
#     planets_response = []
    
#     for planet in list_of_planets:
#         planets_response.append(dict(
#             id = planet.id,
#             name = planet.name,
#             description = planet.description,
#             diameter = planet.diameter 
#         ))
    
#     return planets_response

# # wave 2
# @planets_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)
#     return dict(
#             id = planet.id,
#             name = planet.name,
#             description = planet.description,
#             diameter = planet.diameter)

# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         invalid = {"message": f"Planet id {planet_id} is invalid!"}
#         abort(make_response(invalid, 400))
        
#     for planet in list_of_planets:
#         if planet.id == planet_id:
#             return planet
        
#     not_found = {"message": f"Planet {planet_id} was not found"}
#     abort(make_response(not_found, 404))