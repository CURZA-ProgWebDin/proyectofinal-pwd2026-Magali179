""" importacion """
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from app.models import db
"""configuracion"""
from app.config import config
"""rutas"""
from app.routes.categoria_routes import categoria_bp
from app.routes.movimientos_routes import movimiento_bp
from app.routes.producto_routes import producto_bp
from app.routes.proveedor_routes import proveedor_bp
from app.routes.user_routes import user_bp
from app.routes.rol_routes import rol_bp
from app.routes.auth_routes import auth_bp
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

load_dotenv(override = True)
import os
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app)
    env = os.getenv('FLASK_ENV', 'development')
    app.config.from_object(config[env])
    app.register_blueprint(user_bp)
    app.register_blueprint(rol_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(proveedor_bp)
    app.register_blueprint(producto_bp)
    app.register_blueprint(movimiento_bp)

   
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    jwt.init_app(app)
    return app
    