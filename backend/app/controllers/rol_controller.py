"""importacion"""
from sqlalchemy.exc import IntegrityError
from app.models.rol import Rol
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller
"""clase"""
class RolController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        roles_list = db.session.execute(db.select(Rol).order_by(db.desc(Rol.id))).scalars().all()
        if len( roles_list) >0:
            roles_to_dict = [rol.to_dict() for rol in roles_list ]
            return jsonify(roles_to_dict), 200 
        return jsonify([]), 200 # La consulta fue exitosa, pero no existen registros.
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        rol = db.session.get(Rol, id)
        if rol:
            return jsonify(rol.to_dict()), 200
        return jsonify({"message": 'Rol no encontrado'}), 404
    
    @staticmethod
    def create(request) -> tuple[Response, int]:
        nombre:str = request.get('nombre')
        
        errores = [] 
        if nombre is None:
            errores.append ('El nombre es requerido')
            
        if errores:
            return jsonify({"errores": errores}), 422
        
        try:
                rol = Rol(nombre=nombre)
                db.session.add(rol)
                db.session.commit()
                return jsonify({'message': "Rol creado con exito"}), 201
        except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "Rol ya registrado"}), 409
    
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        nombre:str = request.get('nombre')
        
        errores = []
        if nombre is None:
            errores.append ('El nombre es requerido')
            
        if errores:
            return jsonify({"errores": errores}), 422
            
        rol = db.session.get(Rol, id)
        if rol:
            try:
                rol.nombre = nombre
                db.session.commit()
                return jsonify({'message':'Rol modificado con exito'}), 200
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': 'El nombre ya existe'}), 409 

        return jsonify({'message': 'Rol no encontrado'}), 404
            
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        rol = db.session.get(Rol, id)
        
        if rol:
            try:
                db.session.delete(rol)
                db.session.commit()
                return jsonify({'message':'Rol eliminado con exito'}), 200
            except IntegrityError:
                db.session.rollback()
                return jsonify ({'message': 'No se pudo eliminar el rol'}), 409
        return jsonify({'message': 'Rol no encontrado'}), 404    
