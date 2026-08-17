"""importacion"""

from app.models.movimientos_stock import MovimientoStock
from sqlalchemy.exc import IntegrityError
from app.models.producto import Producto 
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller
"""clase"""
class MovimientoStockController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        movimientos_list = db.session.execute(db.select(MovimientoStock).order_by(db.desc(MovimientoStock.id))).scalars().all()
        if len(movimientos_list) > 0:
            movimientos_to_dict = [movimiento.to_dict() for movimiento in movimientos_list ]
            return jsonify(movimientos_to_dict), 200 
        return jsonify([]), 200 #si lista vacia,busqueda exitosa(200),pero no hay mov registrados
                                #no es 404
    @staticmethod
    def get_by_user(user_id) -> tuple[Response, int]:
        movimientos_list = db.session.execute(db.select(MovimientoStock)
            .filter_by(user_id=user_id)
            .order_by(db.desc(MovimientoStock.id))
        ).scalars().all()

        if len(movimientos_list) > 0:
            movimientos_to_dict = [movimiento.to_dict() for movimiento in movimientos_list]
            return jsonify(movimientos_to_dict), 200

        return jsonify([]), 200
    
    @staticmethod
    def show(id)->tuple[Response, int]:
        movimiento = db.session.get(MovimientoStock, id)
        if movimiento:
            return jsonify(movimiento.to_dict()), 200
        return jsonify({"message": 'Movimiento no encontrado'}), 404
    
    @staticmethod
    def create(request) -> tuple[Response, int]:
        tipo_movimiento:str = request.get('tipo_movimiento')
        cantidad:int = request.get('cantidad')
        motivo:str = request.get('motivo')
        producto_id:int = request.get('producto_id')
        user_id:int = request.get('user_id')
        
        errores = []
        if tipo_movimiento is None:
            errores.append ('El tipo de movimiento es requerido')
        if cantidad is None:
            errores.append ('La cantidad es requerida')
        if producto_id is None:
            errores.append ('El producto es requerido')
        if user_id is None:
            errores.append('El usuario es requerido')
            
        if errores:
            return jsonify({"errores": errores}), 422
        
        if tipo_movimiento not in ['entrada', 'salida']:
            return jsonify({'message': 'El tipo de movimiento debe ser "entrada" o "salida"'}), 422

        if cantidad <= 0:
            return jsonify({'message': 'La cantidad debe ser mayor a cero'}), 422

        producto: Producto | None = db.session.get(Producto, producto_id)

        if producto is None:
            return jsonify({'message': 'Producto no encontrado'}), 404

        if tipo_movimiento == 'salida' and producto.stock_actual < cantidad:
            return jsonify({'message': 'No hay suficiente stock para realizar la salida'}), 422

        try:
            movimiento_stock = MovimientoStock(
            tipo_movimiento=tipo_movimiento,
            cantidad=cantidad,
            motivo=motivo,
            producto_id=producto_id,
            user_id=user_id
        )

            db.session.add(movimiento_stock)

            if tipo_movimiento == 'entrada':
                producto.stock_actual += cantidad
            else:
                producto.stock_actual -= cantidad

            db.session.commit()

            return jsonify({'message': 'Movimiento de stock registrado con éxito'}), 201

        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': 'Error al registrar el movimiento de stock'}), 409
  
    def destroy(id) -> tuple[Response, int]:
        movimiento = db.session.get(MovimientoStock, id)
        if movimiento:
            try:
                producto: Producto | None = db.session.get(Producto, movimiento.producto_id)

                if producto:
                    if movimiento.tipo_movimiento == 'entrada':
                        producto.stock_actual -= movimiento.cantidad
                else:
                        producto.stock_actual += movimiento.cantidad

                db.session.delete(movimiento)
                db.session.commit()

                return jsonify({'message': 'Movimiento de stock eliminado con exito'}), 200

            except IntegrityError:
                db.session.rollback()
        return jsonify({'message': 'Error al eliminar el movimiento de stock'}), 409
    
   
    """no implemento la actualización(update) porque un movimiento de stock representa un registro 
    histórico. Una vez registrado, no debe modificarse para preservar la trazabilidad del 
    inventario. Si se comete un error, se registra un nuevo movimiento correctivo o, según
    el caso, se elimina el movimiento incorrecto.""" 