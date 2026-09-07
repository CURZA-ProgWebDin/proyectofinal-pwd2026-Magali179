"""importacion"""
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller
from werkzeug.security import generate_password_hash
"""clase"""
class UserController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        usuarios_list = db.session.execute(db.select(User).order_by(db.desc(User.id))).scalars().all()
        if len(usuarios_list) > 0:
            usuarios_to_dict = [usuario.to_dict() for usuario in usuarios_list ]
            return jsonify(usuarios_to_dict), 200 
        return jsonify([]), 200  # La consulta fue exitosa, pero no existen registros.      
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        usuario = db.session.get(User, id)
        if usuario:
            return jsonify(usuario.to_dict()), 200
        return jsonify({"message": 'Usuario no encontrado'}), 404
    
    @staticmethod
    def create(request) -> tuple[Response, int]:
        nombre:str = request.get('nombre')
        email:str = request.get('email')
        rol_id:int = request.get('rol_id')
        password:str = request.get('password')
        
        errores = []
        if nombre is None:
            errores.append ('El nombre es requerido')
        if email is None:
            errores.append ('El email es requerido')
        if rol_id is None:
            errores.append ('El rol es requerido')
        if password is None:
            errores.append ('La contraseña es requerida')
        if errores:
            return jsonify({"errores": errores}), 422
            
    
        try:
            # se convierte la contraseña en hash antes de guardarla
            password_hash = generate_password_hash(password)

            user = User(nombre=nombre, email=email, rol_id=rol_id, password=password_hash)
            db.session.add(user)
            db.session.commit()
            return jsonify({'message': "Usuario creado con exito"}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': "Usuario ya registrado"}), 409
    
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        nombre:str = request.get('nombre')
        email:str = request.get('email')
        rol_id:int = request.get('rol_id')
        password:str = request.get('password')
        
        errores = []
        if nombre is None:
            errores.append ('El nombre es requerido')
        if email is None:
            errores.append ('El email es requerido')
        if rol_id is None:
            errores.append ('El rol es requerido')
        if password is None:
            errores.append ('La contraseña es requerida')
        if errores:
            return jsonify({"errores": errores}), 422    
    
        usuario = db.session.get(User, id)
        if usuario:
            try:
                # se convierte la contraseña en hash antes de guardarla
                password_hash = generate_password_hash(password)
                usuario.nombre = nombre
                usuario.email = email
                usuario.rol_id = rol_id
                usuario.password = password_hash
                db.session.commit()
                return jsonify({'message':'Usuario modificado con exito'}), 200
            except IntegrityError:
                db.session.rollback()
                return jsonify({"message": "El nombre o el email ya estan registrados"}), 409
        
    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        usuario = db.session.get(User, id)

        if usuario:
            try:
                db.session.delete(usuario)
                db.session.commit()
                return jsonify({"message": "Usuario eliminado con exito"}), 200

            except IntegrityError:
                db.session.rollback()
                return jsonify({"message": "No se pudo eliminar el usuario"}), 409

        return jsonify({"message": "Usuario no encontrado"}), 404