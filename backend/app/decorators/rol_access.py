from functools import wraps
from flask_jwt_extended import get_jwt_identity
from app.models import db
from app.models.user import User
from flask import jsonify
'''decorador que verifica si el rol del usuario tiene acceso a la ruta'''
def rol_access(roles_permitidos):
    '''funcion de la ruta que queremos proteger, func() represwenta create'''
    def decorator(func):
        '''func q envuelve la func original y controla si usuario tiene permiso o no'''
        @wraps(func)
        def wrapper(*args, **kwargs):
            '''obtenemos el id del usuario a partir del token'''
            user_id = get_jwt_identity()
            '''busca usuario en db y verifica si su rol esta en la lista de roles permitidos'''
            user = db.session.execute(db.select(User).filter_by(id=user_id)).scalar_one_or_none()
            '''existe usuario, tiene rol y su rol esta permitido?, ejecuta func, sino retorna mensaje 403'''
            if user and user.rol and user.rol.nombre in roles_permitidos:
                return func(*args, **kwargs)
            return jsonify({'message': 'Acceso denegado: rol no autorizado'}), 403
        return wrapper
    return decorator
