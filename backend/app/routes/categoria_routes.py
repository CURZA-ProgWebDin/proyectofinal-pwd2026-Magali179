from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.controllers.categoria_controller import CategoriaController
from app.decorators.rol_access import rol_access

categoria_bp = Blueprint("categorias", __name__, url_prefix="/categorias")


@categoria_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    return CategoriaController.get_all()


@categoria_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
def show(id):
    return CategoriaController.show(id)


@categoria_bp.route("/", methods=["POST"])
@jwt_required()
@rol_access("admin")
def create():
    data = request.get_json()
    return CategoriaController.create(data)


@categoria_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
@rol_access("admin")
def update(id):
    data = request.get_json()
    return CategoriaController.update(data, id)


@categoria_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@rol_access("admin")
def destroy(id):
    return CategoriaController.destroy(id)