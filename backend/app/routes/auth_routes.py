'''blueprints para agrupar rutas de autenticacion/request para obtener datos enviados del frontend'''
from flask import Blueprint, request
from app.controllers.auth_controller import AuthController
'''crea el blueprint de autenticacion'''
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    '''obtiene los datos enviados por el frontend y guarda datos para pasarlos al controller'''
    data = request.get_json()
    '''controller encargte de registrar este usuario'''
    return AuthController.Register(data)    

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return AuthController.login(data)

