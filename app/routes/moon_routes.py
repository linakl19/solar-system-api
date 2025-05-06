from flask import Blueprint, request, Response, abort, make_response
from app.models.moon import Moon
from ..db import db
from app.routes.route_utilities import validate_models, get_models_with_filters, create_model

bp = Blueprint("moons_bp", __name__, url_prefix="/moons")

@bp.get("")
def get_all_moons():
    return get_models_with_filters(Moon, request.args)


@bp.post("")
def create_moon():
    request_body = request.get_json()
    return create_model(Moon, request_body)



