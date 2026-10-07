import api from './api' //Traer el objeto api que tenemos creado en api.js

const ProductoService = { //Creamos objeto llamado ProductoService, dentro vamos a  poner todas
                            //las operaciones relacionadas con productos
 
    getAll() { //Obtener todos los productos
        return api.get('/productos/') //pedirlos al backend
    },

    getById(id) {  //Obtener producto por su ID
        return api.get(`/productos/${id}`) // Ruta al backend par aobtener id
    },

    create(datos) { //Envía los datos de un producto nuevo mediante POST
        return api.post('/productos/', datos)
    },

    update(id, datos) { //Modificar un producto que ya existe, reibe 2 parametros id y datos
        return api.put(`/productos/${id}`, datos) //"put" porque en las rutas reales de tu backend tenemos PUT
    },

    delete(id) { //Eliminar un producto existente x id
        return api.delete(`/productos/${id}`)
    }

}

export default ProductoService