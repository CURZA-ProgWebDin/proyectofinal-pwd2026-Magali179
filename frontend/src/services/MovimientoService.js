import api from './api'

const MovimientoService = {

    getAll() {
        return api.get('/movimientos/')
    },

    getMis() {  //Obtener mis movimientos
        return api.get('/movimientos/mis/') //Hacemos peticion GET al backend
    },

    getById(id) {
        return api.get(`/movimientos/${id}`)
    },

    create(datos) {
        return api.post('/movimientos/', datos)
    },

    delete(id) {
        return api.delete(`/movimientos/${id}`)
    }

}

export default MovimientoService