from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.producto_controller import ProductoController
from app.decorators.rol_access import rol_access

producto_bp = Blueprint("productos", __name__, url_prefix="/productos")



@producto_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return ProductoController.get_all()

@producto_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def show(id):
    return ProductoController.show(id)

@producto_bp.route("/", methods=["POST"])
@jwt_required()
@rol_access("admin")
def create():
    data = request.get_json()
    return ProductoController.create(data)

@producto_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
@rol_access("admin")
def update(id):
    data = request.get_json()
    return ProductoController.update(data,id)

@producto_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@rol_access("admin")
def destroy(id):
    return ProductoController.destroy(id)