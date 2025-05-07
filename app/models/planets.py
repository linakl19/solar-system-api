from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    description: Mapped[str]
    diameter: Mapped[int]
    moons: Mapped[list["Moon"]] = relationship(back_populates="planet")

    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'diameter': self.diameter,
            'moons': [moon.to_dict() for moon in self.moons]
            }
        
    
    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            name = planet_data["name"],
            description = planet_data["description"],
            diameter = planet_data["diameter"]
        )