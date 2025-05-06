from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional 
from sqlalchemy import ForeignKey
from ..db import db

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    size: Mapped[int]
    description: Mapped[str]
    discovered_at: Mapped[int]
    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="planets")
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'size': self.size,
            'description': self.description,
            'discovered_at': self.discovered_at
            }
    
    @classmethod
    def from_dict(cls, planet_data):
        return cls(
            size = planet_data["size"],
            description = planet_data["description"],
            discovered_at = planet_data["discovered_at"]
        )