from app import create_app
from app.models import db
from app.models.rol import Rol
from app.models.user import User
from app.models.categoria import Categoria
from app.models.proveedor import Proveedor
from app.models.producto import Producto

app = create_app()

with app.app_context():

    
    ###### CARGA DE ROLES ######
    
    rol_admin = Rol.query.filter_by(nombre='admin').first()
    if not rol_admin:
        rol_admin = Rol(nombre='admin')
        db.session.add(rol_admin)

    rol_operador = Rol.query.filter_by(nombre='operador').first()
    if not rol_operador:
        rol_operador = Rol(nombre='operador')
        db.session.add(rol_operador)

    db.session.commit()

    
    ##### USUARIO ADMIN ######

    admin = User.query.filter_by(nombre='admin').first()

    if not admin:
        admin = User(
            nombre='admin',
            email='admin@test.com',
            password='admin123',
            rol_id=rol_admin.id
        )

        admin.generate_password('admin123')

        db.session.add(admin)
        db.session.commit()

    
    ###### CATEGORIAS LITERARIAS ######
    
    literatura = Categoria.query.filter_by(nombre="Literatura").first()
    if not literatura:
        literatura = Categoria(
            nombre="Literatura",
            descripcion="Novelas, cuentos y obras literarias."
        )
        db.session.add(literatura)

    arte = Categoria.query.filter_by(nombre="Arte").first()
    if not arte:
        arte = Categoria(
            nombre="Arte",
            descripcion='Libros sobre pintura, escultura, fotografia y diseño.'
        )
        db.session.add(arte)

    historia = Categoria.query.filter_by(nombre="Historia").first()
    if not historia:
        historia = Categoria(
            nombre="Historia",
            descripcion="Libros de historia, biografias y acontecimientos historicos."
        )
        db.session.add(historia)
            
    infantil = Categoria.query.filter_by(nombre="Infantil").first()
    if not infantil:
        infantil = Categoria(
            nombre="Infantil",
            descripcion="Libros destinados al publico infantil."
        )
        db.session.add(infantil)
    
    tecnologia = Categoria.query.filter_by(nombre="Tecnologia").first()
    if not tecnologia:
        tecnologia = Categoria(
            nombre="Tecnologia",
            descripcion="Libros de informatica, programacion e innovacion tecnologica."
        )
        db.session.add(tecnologia)
    
    db.session.commit()

    ###### PROVEEDORES/EDITORIALES ######
    
    planeta = Proveedor.query.filter_by(nombre="Planeta").first()
    if not planeta:
        planeta = Proveedor(
            nombre="Planeta",
            contacto="Departamento Comercial",
            telefono="01162117812",
            email="contacto@planeta.com"
        )
        db.session.add(planeta)
        
    paidos = Proveedor.query.filter_by(nombre="Paidos").first()
    if not paidos:
        paidos = Proveedor(
            nombre="Paidos",
            contacto="Departamento Comercial",
            telefono="01162115421",
            email="contacto@paidos.com"
        )
        db.session.add(paidos)
        
    sudamericana = Proveedor.query.filter_by(nombre="Sudamericana").first()
    if not sudamericana:
        sudamericana = Proveedor(
            nombre="Sudamericana",
            contacto="Departamento Comercial",
            telefono="01162445422",
            email="contacto@sudamericana.com"
        )
        db.session.add(sudamericana)
        
    santillana = Proveedor.query.filter_by(nombre="Santillana").first()
    if not santillana:
        santillana = Proveedor(
            nombre="Santillana",
            contacto="Departamento Comercial",
            telefono="01162445422",
            email="contacto@santillana.com"
        )
        db.session.add(santillana)
        
    db.session.commit()

    
    ###### PRODUCTOS/LIBROS ######
    principito = Producto.query.filter_by(nombre="El Principito").first()
    if not principito:
        principito = Producto(
            nombre="El Principito",
            autor="Antoine de Saint-Exupery",
            descripcion="Novela corta considerada un clasico de la literatura universal.",
            precio_costo=12000,
            precio_venta=18000,
            stock_actual=20,
            stock_minimo=5,
            categoria_id=literatura.id,
            proveedor_id=planeta.id
        )
        db.session.add(principito)
        
    martin_fierro = Producto.query.filter_by(nombre="Martin Fierro").first()
    if not martin_fierro:
        martin_fierro = Producto(
            nombre="Martin Fierro",
            autor="Jose Hernandez",
            descripcion="Poema narrativo considerado una de las obras mas importantes de la literatura argentina.",
            precio_costo=14000,
            precio_venta=21000,
            stock_actual=15,
            stock_minimo=5,
            categoria_id=literatura.id,
            proveedor_id=sudamericana.id
        )
        db.session.add(martin_fierro)
        
    historia_arte = Producto.query.filter_by(nombre="Historia del Arte").first()
    if not historia_arte:
        historia_arte = Producto(
            nombre="Historia del Arte",
            autor="Ernst H. Gombrich",
            descripcion="Obra de referencia sobre la historia del arte occidental.",
            precio_costo=28000,
            precio_venta=39000,
            stock_actual=10,
            stock_minimo=2,
            categoria_id=arte.id,
            proveedor_id=paidos.id
        )
        db.session.add(historia_arte)
        
    vidas_artistas = Producto.query.filter_by(nombre="Vida de pintores, escultores y arquitectos").first()
    if not vidas_artistas:
        vidas_artistas = Producto(
            nombre="Vida de pintores, escultores y arquitectos",
            autor="Giorgio Vasari",
            descripcion="Clasico sobre la vida y obra de los grandes artistas del Renacimiento.",
            precio_costo=25000,
            precio_venta=36000,
            stock_actual=8,
            stock_minimo=2,
            categoria_id=arte.id,
            proveedor_id=planeta.id
            )
        db.session.add(vidas_artistas)
        
    sapiens = Producto.query.filter_by(nombre="Sapiens").first()
    if not sapiens:
        sapiens = Producto(
            nombre="Sapiens",
            autor="Yuval Noah Harari",
            descripcion="Ensayo sobre la historia y evolucion de la humanidad.",
            precio_costo=22000,
            precio_venta=32000,
            stock_actual=15,
            stock_minimo=3,
            categoria_id=historia.id,
            proveedor_id=sudamericana.id
            )
        db.session.add(sapiens)
        
    mitos_historia = Producto.query.filter_by(nombre="Los mitos de la historia argentina").first()
    if not mitos_historia:
        mitos_historia = Producto(
            nombre="Los mitos de la historia argentina",
            autor="Felipe Pigna",
            descripcion="Analisis de los principales hechos y personajes de la historia argentina.",
            precio_costo=18000,
            precio_venta=27000,
            stock_actual=12,
            stock_minimo=3,
            categoria_id=historia.id,
            proveedor_id=planeta.id
            )
        db.session.add(mitos_historia)
        
    cuentos_selva = Producto.query.filter_by(nombre="Cuentos de la Selva").first()
    if not cuentos_selva:
        cuentos_selva = Producto(
            nombre="Cuentos de la Selva",
            autor="Horacio Quiroga",
            descripcion="Coleccion de cuentos clasicos para niños ambientados en la selva misionera.",
            precio_costo=9000,
            precio_venta=14000,
            stock_actual=25,
            stock_minimo=5,
            categoria_id=infantil.id,
            proveedor_id=santillana.id
            )
        db.session.add(cuentos_selva)
        
    dailan_kifki = Producto.query.filter_by(nombre="Dailan Kifki").first()
    if not dailan_kifki:
        dailan_kifki = Producto(
            nombre="Dailan Kifki",
            autor="Maria Elena Walsh",
            descripcion="Novela infantil protagonizada por un elefante muy particular.",
            precio_costo=8500,
            precio_venta=13000,
            stock_actual=20,
            stock_minimo=5,
            categoria_id=infantil.id,
            proveedor_id=santillana.id
            )
        db.session.add(dailan_kifki)
        
    clean_code = Producto.query.filter_by(nombre="Clean Code").first()
    if not clean_code:
        clean_code = Producto(
            nombre="Clean Code",
            autor="Robert C. Martin",
            descripcion="Guia de buenas practicas para escribir codigo limpio y mantenible.",
            precio_costo=30000,
            precio_venta=42000,
            stock_actual=8,
            stock_minimo=2,
            categoria_id=tecnologia.id,
            proveedor_id=planeta.id
            )
        db.session.add(clean_code)
        
    programador_pragmatico = Producto.query.filter_by(nombre="El programador pragmatico").first()
    if not programador_pragmatico:
        programador_pragmatico = Producto(
            nombre="El programador pragmatico",
            autor="Andrew Hunt y David Thomas",
            descripcion="Libro de referencia sobre desarrollo de software y buenas practicas de programacion.",
            precio_costo=28000,
            precio_venta=39000,
            stock_actual=10,
            stock_minimo=2,
            categoria_id=tecnologia.id,
            proveedor_id=paidos.id
            )
        db.session.add(programador_pragmatico)
   
    db.session.commit()

    print("Seed completado correctamente.")
    
    
 
        