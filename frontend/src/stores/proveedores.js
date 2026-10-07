import { ref } from 'vue'
import { defineStore } from 'pinia'
import ProveedorService from '@/services/ProveedorService'

export const useProveedoresStore = defineStore('proveedores', () => {

    const proveedores = ref([])

    const getProveedores = async () => {
        const respuesta = await ProveedorService.getAll()
        proveedores.value = respuesta.data
    }

    const getProveedor = async (id) => {
        const respuesta = await ProveedorService.getById(id)
        return respuesta.data
    }

    const crearProveedor = async (datos) => {
        const respuesta = await ProveedorService.create(datos)
        return respuesta.data
    }

    const actualizarProveedor = async (id, datos) => {
        const respuesta = await ProveedorService.update(id, datos)
        return respuesta.data
    }

    const eliminarProveedor = async (id) => {
        const respuesta = await ProveedorService.delete(id)
        return respuesta.data
    }

    return {
        proveedores,
        getProveedores,
        getProveedor,
        crearProveedor,
        actualizarProveedor,
        eliminarProveedor
    }
})