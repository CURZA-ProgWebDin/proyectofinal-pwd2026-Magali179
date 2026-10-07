from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.user_controller import UserController
from app.decorators.rol_access import rol_access

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/', methods=["GET"])
@jwt_required()
@rol_access(['admin'])
def get_all():
    return UserController.get_all()

@user_bp.route('/<int:id>', methods=["GET"])
@jwt_required()
@rol_access(['admin'])
def show(id):
    return UserController.show(id)

@user_bp.route("/", methods=['POST'])
@jwt_required()
@rol_access(['admin'])
def create():
    data = request.get_json()
    return UserController.create(data)

@user_bp.route("/<int:id>", methods=['PUT'])
@jwt_required()
@rol_access(['admin'])
def update(id):
    data = request.get_json()
    return  UserController.update(data,id)

@user_bp.route("/<int:id>", methods=['DELETE'])
@jwt_required()
@rol_access(['admin'])
def destroy(id):
    return UserController.destroy( id)
