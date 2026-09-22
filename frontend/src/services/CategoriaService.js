import api from './api' //Traer el objeto api que tenemos creado en api.js

const CategoriaService = { //Crea objeto llamado CategoriaService
 
    getAll() {  //Obtener todas las categorias que existen en el  backend
        return api.get('/categorias/') // Peticion al backend
    },

    getById(id) {  //Busca categoria por ID
        return api.get(`/categorias/${id}`) //Hacemos GET al backend
    },

    create(datos) { //Crear categoria nueva
        return api.post('/categorias/', datos) //POST porque en las rutas reales de Flask tenemos POST
    },

    update(id, datos) { //Modificar categoria existente, indicando q categoria ID y datos
        return api.put(`/categorias/${id}`, datos)
    },

    delete(id) { //Eliminar categoria existente x ID
        return api.delete(`/categorias/${id}`) //api.delete() Porque la ruta real de Flask es DELETE
    }

}

export default CategoriaService