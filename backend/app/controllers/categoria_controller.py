"""obtenemos todos los datos con request.get, validamos solos los nullable=False(models),
se devuelven todos los errores"""

"""importacion"""

from app.models.categoria import Categoria
from sqlalchemy.exc import IntegrityError
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller

"""clase"""
class CategoriaController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        categorias_list = db.session.execute(
        db.select(Categoria).order_by(db.desc(Categoria.id))).scalars().all()

        categorias_to_dict = [
            categoria.to_dict() for categoria in categorias_list ]
# Si existen categorías, se devuelve la lista con código 200 (OK).
# Si no existen categorías, se devuelve una lista vacía ([]), también con código 200,
# porque la consulta se ejecutó correctamente aunque no haya registros. no me parece
#correcto error 404
        return jsonify(categorias_to_dict), 200
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        categoria = db.session.get(Categoria, id)
        if categoria:
            return jsonify(categoria.to_dict()), 200
        # Si la categoría existe, devuelve sus datos con código 200 (OK).
# Si no existe una categoría con ese ID, devuelve un mensaje de error y código 404 (Not Found).
        return jsonify({"message": 'Categoria no encontrada'}), 404
    
    @staticmethod
    def create(request) -> tuple[Response, int]:
        nombre:str = request.get('nombre')
        descripcion:str = request.get('descripcion')
        
        errores = [] #coleccion de mensajes error
        # solo validamos los nullable= False
        if nombre is None:
            errores.append ('El nombre es requerido')
            
        if errores:
             return jsonify({"errores": errores}), 422
        """si hay 1 error habra mensaje x ese error, si se dan los 2 errores habra mensaje 
        x ambos"""
        try:
            categoria = Categoria(nombre=nombre, descripcion=descripcion)
            db.session.add(categoria)
            db.session.commit()
            return jsonify({'message': "Categoria creada con exito"}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': "Categoria ya registrada"}), 409
       
    @staticmethod
    def update(request, id)-> tuple[Response, int]:
        nombre:str = request.get('nombre')
        descripcion:str = request.get('descripcion')
        
        errores = []
        if nombre is None:
            errores.append ('El nombre es requerido')
                    
        if errores:
            return jsonify({"errores": errores}), 422
         
        categoria = db.session.get(Categoria, id)
        if categoria:
            try:
                categoria.nombre = nombre
                categoria.descripcion = descripcion
                db.session.commit()
                return jsonify({'message':'Categoria modificada con exito'}), 200
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': 'El nombre de la categoria ya existe' }), 409
        else:     
            return jsonify({'message': 'Categoria no encontrada' }), 404
            
     
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        categoria = db.session.get(Categoria, id)
        
        if categoria:
            if len(categoria.productos) == 0:
                db.session.delete(categoria)
                db.session.commit()
                return jsonify({"message": "Categoría eliminada con éxito" }), 200
            else:
                return jsonify({"message": "La categoría tiene productos asociados"}), 409
        return jsonify({"message": "Categoría no encontrada"}), 404       