import api from './api'

const UserService = { //Usuario de Libreria Suipacha

    getAll() {
        return api.get('/users/')
    },

    getById(id) {
        return api.get(`/users/${id}`)
    },

    create(datos) {
        return api.post('/users/', datos)
    },

    update(id, datos) {
        return api.put(`/users/${id}`, datos)
    },

    delete(id) {
        return api.delete(`/users/${id}`)
    }

}

export default UserService