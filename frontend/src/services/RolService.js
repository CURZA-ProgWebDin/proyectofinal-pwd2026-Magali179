import api from './api'

const RolService = { //Tipo de ususario dentro del sistema

    getAll() {
        return api.get('/roles/')
    },

    getById(id) {
        return api.get(`/roles/${id}`)
    },

    create(datos) {
        return api.post('/roles/', datos)
    },

    update(id, datos) {
        return api.put(`/roles/${id}`, datos)
    },

    delete(id) {
        return api.delete(`/roles/${id}`)
    }

}

export default RolService