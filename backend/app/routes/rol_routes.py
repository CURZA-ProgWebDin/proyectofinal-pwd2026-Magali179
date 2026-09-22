from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.rol_controller import RolController
from app.decorators.rol_access import rol_access


rol_bp = Blueprint('roles', __name__, url_prefix='/roles')

@rol_bp.route('/', methods=["GET"])
@jwt_required()
@rol_access("admin")
def get_all():
    return RolController.get_all()

@rol_bp.route('/<int:id>', methods=["GET"])
@jwt_required()
@rol_access("admin")
def show(id):
    return RolController.show(id)

@rol_bp.route("/", methods=['POST'])
@jwt_required()
@rol_access("admin")
def create():
    data = request.get_json()
    return RolController.create(data)

@rol_bp.route("/<int:id>", methods=['PUT'])
@jwt_required()
@rol_access("admin")
def update(id):
    data = request.get_json()
    return  RolController.update(data, id)
    
@rol_bp.route("/<int:id>", methods=['DELETE'])
@jwt_required()
@rol_access("admin")
def destroy(id):
    return RolController.destroy( id)
