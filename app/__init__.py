from flask import Flask
from app.routes.planets_routes import bp as planets_bp
from app.routes.planets_routes import bp as moons_bp
from .db import db, migrate
from .models import planets, moon
import os


def create_app(config=None):
    app = Flask(__name__)
    
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    if config:
        app.config.update(config)
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Register planet_bp
    app.register_blueprint(planets_bp)
    app.register_blueprint(moons_bp)

    return app