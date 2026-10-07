from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers.movimientos_stock_controller import MovimientoStockController
from app.decorators.rol_access import rol_access

movimiento_bp = Blueprint("movimientos", __name__, url_prefix="/movimientos")

@movimiento_bp.route("/", methods=["GET"])
@jwt_required()
@rol_access("admin")
def get_all():
    return MovimientoStockController.get_all()

@movimiento_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
@rol_access("admin")
def show(id):
    return MovimientoStockController.show(id)

@movimiento_bp.route("/mis/", methods=["GET"])
@jwt_required()
def get_mis():
    user_id = get_jwt_identity()
    return MovimientoStockController.get_by_user(user_id)


@movimiento_bp.route("/", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()
    data["user_id"] = get_jwt_identity()
    return MovimientoStockController.create(data)

@movimiento_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@rol_access("admin")
def destroy(id):
    return MovimientoStockController.destroy(id)