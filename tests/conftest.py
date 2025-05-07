import pytest
from app import create_app
from app.db import db
from flask.signals import request_finished
from dotenv import load_dotenv
import os
from app.models.moon import Moon
from app.models.planets import Planet


load_dotenv()

@pytest.fixture
def app():
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    app = create_app(test_config)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mercury = Planet(
        name="Mercury", 
        description="The smallest planet in our solar system", 
        diameter=4879)
    venus = Planet(
        name="Venus", 
        description="The second planet from the Sun.", 
        diameter=12104)
    
    db.session.add_all([mercury, venus])
    db.session.commit()


@pytest.fixture
def two_saved_moons(app):
    # Arrange
    europa = Moon(
        size= 3125,
        description= "Frozen surface with possible ocean beneath",
        discovered_at= 1610,
        planet = None
    )
    luna = Moon(
        size= 1737,
        description= "Rocky surface with many craters",
        discovered_at= -4000,
        planet = None
    )
    
    db.session.add_all([europa, luna])
    db.session.commit()

@pytest.fixture
def planet_with_two_moons(app, two_saved_planets):
    europa_moon = Moon(
        size= 3125,
        description= "Frozen surface with possible ocean beneath",
        discovered_at= 1610,
        planet_id = 1
    )
    luna_moon = Moon(
        size= 1737,
        description= "Rocky surface with many craters",
        discovered_at= -4000,
        planet_id = 1
    )
    db.session.add_all([europa_moon, luna_moon])
    db.session.commit()