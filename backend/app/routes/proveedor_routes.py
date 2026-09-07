from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.proveedor_controller import ProveedorController
from app.decorators.rol_access import rol_access

proveedor_bp = Blueprint("proveedores", __name__, url_prefix="/proveedores")

@proveedor_bp.route("/", methods=["GET"])
@jwt_required()
@rol_access("admin")
def get_all():
    return ProveedorController.get_all()

@proveedor_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
@rol_access("admin")
def show(id):
    return ProveedorController.show(id)

@proveedor_bp.route("/", methods=["POST"])
@jwt_required()
@rol_access("admin")
def create():
    data = request.get_json()
    return ProveedorController.create(data)

@proveedor_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
@rol_access("admin")
def update(id):
    data = request.get_json()
    return ProveedorController.update(data,id)

@proveedor_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@rol_access("admin")
def destroy(id):
    return ProveedorController.destroy(id)