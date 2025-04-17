class Planet:
    def __init__(self, id, name, description, diameter):
        self.id = id
        self.name = name
        self.description = description
        self.diameter = diameter

list_of_planets = [
    Planet(1, "Mercury", "The smallest planet in our solar system.", 4879),
    Planet(2, "Venus", "The second planet from the Sun.", 12104),
    Planet(3, "Earth", "The third planet from the Sun and the only known planet to support life.", 12756),
    Planet(4, "Mars", "The fourth planet from the Sun, known as the Red Planet.", 67920),
    Planet(5, "Jupiter", "The largest planet in our solar system.", 142984)
]