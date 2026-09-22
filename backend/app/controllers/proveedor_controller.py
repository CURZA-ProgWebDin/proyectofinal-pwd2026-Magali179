"""obtenemos todos los datos con request.get, validamos solos los nullable=False(models),
se devuelven todos los errores"""

"""importacion"""

from app.models.proveedor import Proveedor
from sqlalchemy.exc import IntegrityError
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller

"""clase"""
class ProveedorController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        proveedores_list = db.session.execute(db.select(Proveedor).order_by(db.desc(Proveedor.id))).scalars().all()
       
        proveedores_to_dict = [proveedor.to_dict() for proveedor in proveedores_list ]
        # Si existen proveedores, se devuelve la lista con código 200 (OK).
                # Si no existen proveedores, se devuelve una lista vacía ([]), también con código 200,
                # porque la consulta se ejecutó correctamente aunque no haya registros
                # codigo 404 no es correcto en este caso, ya que no hubo error, simplemente no habia
                # registros para mostrar
        
        return jsonify(proveedores_to_dict), 200 
       
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        proveedor = db.session.get(Proveedor, id)
        if proveedor:
            return jsonify(proveedor.to_dict()), 200
        return jsonify({"message": 'Proveedor no encontrado'}), 404
    
    @staticmethod
    def create(request) -> tuple[Response, int]:
        nombre:str = request.get('nombre')
        contacto:str = request.get('contacto')
        email:str = request.get('email')
        telefono:str = request.get('telefono')
       
        errores = []
        if nombre is None:
            errores.append ('El nombre es requerido')
        
        if errores:
            return jsonify({"errores": errores}), 422
            
        try:
            proveedor = Proveedor(nombre=nombre, contacto=contacto, telefono=telefono, email=email)
            db.session.add(proveedor)
            db.session.commit()
            return jsonify({'message': "Proveedor creado con exito"}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': "Proveedor ya registrado"}), 409
                
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        nombre:str = request.get('nombre')
        contacto:str = request.get('contacto')
        email:str = request.get('email')
        telefono:str = request.get('telefono')
        
        errores = []
        if nombre is None:
            errores.append ('El nombre es requerido')
        if errores:
            return jsonify({'errores': errores}), 422            
        
        proveedor = db.session.get(Proveedor, id)
        if proveedor:
            try:
                proveedor.nombre = nombre
                proveedor.contacto = contacto
                proveedor.email = email
                proveedor.telefono = telefono
                    
                db.session.commit()
                return jsonify({'message':'Proveedor modificado con exito'}), 200
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': 'El nombre ya existe'}), 409

        return jsonify({'message': 'Proveedor no encontrado'}), 404
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        proveedor = db.session.get(Proveedor, id)
        
        if proveedor:

            if len(proveedor.productos) == 0:
                db.session.delete(proveedor)
                db.session.commit()

                return jsonify({'message': 'Proveedor eliminado con éxito'}), 200

            return jsonify({'message': 'El proveedor tiene productos asociados'}), 409

        return jsonify({'message': 'Proveedor no encontrado'}), 404