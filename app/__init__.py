from flask import Flask
from app.routes.planets_routes import planets_bp
from .db import db, migrate
from .models import planets


def create_app(test_config=None):
    app = Flask(__name__)
    
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/solar_system_development'
    
    db.init_app(app)
    migrate.init_app(app, db)

    # Register planet_bp
    app.register_blueprint(planets_bp)

    return app