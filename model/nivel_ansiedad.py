from utils.db import db
from dataclasses import dataclass

@dataclass
class NivelAnsiedad(db.Model):
    id_nivel_ansiedad: int = db.Column(db.Integer, primary_key=True)
    descripcion: str = db.Column(db.String(50), nullable=False)

    def __init__(self, descripcion):
        self.descripcion = descripcion
