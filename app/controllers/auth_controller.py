"""importacion"""
from app.models import db
from app.models.user import User
from app.models.rol import Rol
from flask import Response, jsonify
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError

"""clase            """
class AuthController:

    @staticmethod
    def Register(request: dict) -> tuple[Response, int]:
        nombre: str | None = request.get('nombre')
        email: str | None = request.get('email')
        password: str | None = request.get('password')

        errores = []

        if nombre is None:
            errores.append ('El nombre es requerido')
        if email is None:
            errores.append ('El email es requerido')
        if password is None:
            errores ('La contraseña es requerida')
            
        if errores:
            return jsonify({"errores": errores}), 422

        try:
            rol_operador = db.session.execute(db.select(Rol).filter_by(nombre='operador')).scalar_one_or_none()

            if rol_operador is None:
                return jsonify({'message': 'El rol operador no existe'}), 404

            user = User(nombre=nombre, email=email, rol_id=rol_operador.id, password=password)

            user.generate_password(password)

            db.session.add(user)
            db.session.commit()

            return jsonify({'message': 'Usuario creado con éxito'}), 201

        except IntegrityError:
            db.session.rollback()
        return jsonify({'message': 'Usuario ya registrado'}), 409

    @staticmethod
    def login(request: dict) -> tuple[Response, int]:

        nombre: str | None = request.get('nombre')
        password: str | None = request.get('password')

        errores = []

        if nombre is None:
            errores.append ('El nombre es requerido')
        if password is None:
            errores ('La contraseña es requerida')
            
        if errores:
            return jsonify({'errores': errores}), 422

   
        user = db.session.execute(db.select(User).filter_by(nombre=nombre)).scalar_one_or_none()

        if user and user.activo == 'N':
            return jsonify({'message': 'Usuario inactivo'}), 401

        if user and user.validate_password(password):
            access_token = create_access_token(identity=str(user.id), additional_claims={
                'rol': user.rol.nombre if user.rol else None
        }
    )

            return jsonify({
                'access_token': access_token,
                'rol': user.rol.nombre if user.rol else None,
                'nombre': user.nombre
    }), 200

        return jsonify({'message': 'Credenciales inválidas'}), 401