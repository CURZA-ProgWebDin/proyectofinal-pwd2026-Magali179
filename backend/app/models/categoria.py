"""importacion"""
from app.models import db
from app.models.base_model import BaseModel

"""clase"""
class Categoria(BaseModel):
    __tablename__ = 'categorias'
    
    nombre = db.Column(db.String(100), unique = True, nullable = False)
    descripcion = db.Column(db.String (255), nullable = True)
    
    productos = db.relationship('Producto', back_populates='categoria')
    
    """constructor"""
    def __init__(self, nombre, descripcion) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        
    def to_dict(self):
        data = super().to_dict()
        """herencia BaseModel"""
        data.update ({
            
            'nombre': self.nombre,
            'descripcion': self.descripcion,
                       
        })
        return data