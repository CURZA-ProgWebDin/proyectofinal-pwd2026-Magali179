import { ref } from 'vue'
import { defineStore } from 'pinia'
import RolService from '@/services/RolService'

export const useRolesStore = defineStore('roles', () => {

    const roles = ref([])

    const getRoles = async () => {
        const respuesta = await RolService.getAll()
        roles.value = respuesta.data
    }

    const getRol = async (id) => {
        const respuesta = await RolService.getById(id)
        return respuesta.data
    }

    const crearRol = async (datos) => {
        const respuesta = await RolService.create(datos)
        return respuesta.data
    }

    const actualizarRol = async (id, datos) => {
        const respuesta = await RolService.update(id, datos)
        return respuesta.data
    }

    const eliminarRol = async (id) => {
        const respuesta = await RolService.delete(id)
        return respuesta.data
    }

    return {
        roles,
        getRoles,
        getRol,
        crearRol,
        actualizarRol,
        eliminarRol
    }
})