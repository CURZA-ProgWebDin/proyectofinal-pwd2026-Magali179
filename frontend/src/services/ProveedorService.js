import api from './api'

const ProveedorService = {

    getAll() {
        return api.get('/proveedores/')
    },

    getById(id) {
        return api.get(`/proveedores/${id}`)
    },

    create(datos) {
        return api.post('/proveedores/', datos)
    },

    update(id, datos) {
        return api.put(`/proveedores/${id}`, datos)
    },

    delete(id) {
        return api.delete(`/proveedores/${id}`)
    }

}

export default ProveedorService