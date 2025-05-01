# place in a top-level file. call it something like seed.py
# no need to dwell on the `with my_app.app_context():`, other than to say
# that the `db` reference won't work unless it runs with an app context
from app import create_app, db
from app.models.planets import Planet

my_app = create_app()


with my_app.app_context():
    db.session.add(Planet(name="Mercury", description="The smallest planet in our solar system", diameter=4879)),
    db.session.add(Planet(name="Venus", description="The second planet from the Sun.", diameter=12104)),
    db.session.add(Planet(name="Earth", description="The third planet from the Sun and the only known planet to support life.", diameter=12756)),
    db.session.add(Planet(name="Mars", description="The fourth planet from the Sun, known as the Red Planet.", diameter=67920)),
    db.session.add(Planet(name="Jupiter",description="The largest planet in our solar system.",diameter=142984
    )),

    db.session.commit()

