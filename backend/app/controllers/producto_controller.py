"""obtenemos todos los datos con request.get, validamos solos los nullable=False(models),
se devuelven todos los errores"""

"""importacion"""

from sqlalchemy.exc import IntegrityError
from app.models.producto import Producto # es necesario importarla
from app.models import db
from flask import Response, jsonify
from app.controllers import Controller

"""clase"""
class ProductoController (Controller):
    
    @staticmethod
    def get_all() -> tuple[Response, int]:
        productos_list = db.session.execute(db.select(Producto).order_by(db.desc(Producto.id))).scalars().all()
    
        productos_to_dict = [producto.to_dict() for producto in productos_list]
        # Si existen productos, se devuelve la lista con código 200 (OK).
        # Si no existen productos, se devuelve una lista vacía ([]), también con código 200,
        # porque la consulta se ejecutó correctamente aunque no haya registros. 
        # codigo 404 no es correcto en este caso, ya que no hubo error, simplemente no habia
                # registros para mostrar

        return jsonify(productos_to_dict), 200
    
    @staticmethod
    def show(id)-> tuple[Response, int]:
        producto = db.session.get(Producto, id)
        if producto:
            return jsonify(producto.to_dict()), 200
        return jsonify({"message": 'Producto no encontrado'}), 404
    
    @staticmethod
    def create(request) -> tuple[Response, int]:
        nombre:str = request.get('nombre')
        autor:str = request.get('autor')
        descripcion:str = request.get('descripcion')
        precio_costo:float = request.get('precio_costo')
        precio_venta:float = request.get('precio_venta')
        stock_actual:int = request.get('stock_actual')
        stock_minimo:int = request.get('stock_minimo')
        categoria_id:int = request.get('categoria_id')
        proveedor_id:int = request.get('proveedor_id')
        
        errores = [] 
        if nombre is None:
            errores.append ('El nombre es requerido')
        if autor is None:
            errores.append ('Nombre de autor requerido')
        if precio_costo is None:
            errores.append ('El precio de costo es requerido')
        if precio_venta is None:
            errores.append ('El precio de venta es requerido')
        if categoria_id is None:
            errores.append ('La categoria es requerida')
        if stock_actual is None:
            errores.append("El stock actual es requerido")
        if stock_minimo is None:
            errores.append("El stock mínimo es requerido")
        
        if stock_actual is not None and stock_actual < 0:
            errores.append("El stock actual no puede ser negativo")

        if stock_minimo is not None and stock_minimo < 0:
            errores.append("El stock mínimo no puede ser negativo")
        
        if errores:
            return jsonify({"errores": errores}), 422
        
        try:
            producto = Producto(nombre=nombre,
                autor=autor,
                descripcion=descripcion,
                precio_costo=precio_costo,
                precio_venta=precio_venta, 
                stock_actual=stock_actual, 
                stock_minimo=stock_minimo, 
                categoria_id=categoria_id, 
                proveedor_id=proveedor_id)
            
            db.session.add(producto)
            db.session.commit()
            return jsonify({'message': "Producto creado con exito"}), 201
        except IntegrityError:
            db.session.rollback()
            return jsonify({'message': "Producto ya registrado"}), 409
    
        
    @staticmethod
    def update(request, id)->tuple[Response, int]:
        nombre:str = request.get('nombre')
        autor:str = request.get('autor')
        descripcion:str = request.get('descripcion')
        precio_costo:float = request.get('precio_costo')
        precio_venta:float = request.get('precio_venta')
        stock_actual:int = request.get('stock_actual')
        stock_minimo:int = request.get('stock_minimo')
        categoria_id:int = request.get('categoria_id')
        proveedor_id:int = request.get('proveedor_id')
        
        errores = []
        
        if nombre is None:
            errores.append ('El nombre es requerido')
        if autor is None:
            errores.append ('Nombre de autor requerido')
        if precio_costo is None:
            errores.append ('El precio de costo es requerido')
        if precio_venta is None:
            errores.append ('El precio de venta es requerido')
        if categoria_id is None:
            errores.append ('La categoria es requerida')
        if stock_actual is None:
            errores.append("El stock actual es requerido")
        if stock_minimo is None:
            errores.append("El stock mínimo es requerido")
                
        if stock_actual is not None and stock_actual < 0:
            errores.append("El stock actual no puede ser negativo")
        
        if stock_minimo is not None and stock_minimo < 0:
            errores.append("El stock mínimo no puede ser negativo")
                    
            
        if errores:
            return jsonify({"errores": errores}), 422
    
    
        producto = db.session.get(Producto, id)
        if producto:
            try:
                producto.nombre = nombre
                producto.autor=autor
                producto.descripcion = descripcion
                producto.precio_costo = precio_costo
                producto.precio_venta = precio_venta
                producto.stock_actual = stock_actual
                producto.stock_minimo = stock_minimo 
                producto.categoria_id = categoria_id
                producto.proveedor_id = proveedor_id
                db.session.commit()
                return jsonify({'message':'Producto modificado con exito'}), 200
            except IntegrityError:
                db.session.rollback()
                return jsonify({'message': "Producto ya registrado"}), 409
    
        return jsonify({"message": "Producto no encontrado"}), 404

    @staticmethod
    def destroy(id) -> tuple[Response, int]:
        producto = db.session.get(Producto, id)
        
        if producto:
            db.session.delete(producto)
            db.session.commit()
            return jsonify({'message':'Producto eliminado con exito'}), 200

        return jsonify({"message": "Producto no encontrado"}), 404