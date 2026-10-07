import { ref } from 'vue'
import { defineStore } from 'pinia'
import UserService from '@/services/UserService'

export const useUsuariosStore = defineStore('usuarios', () => {

    const usuarios = ref([])

    const getUsuarios = async () => {
        const respuesta = await UserService.getAll()
        usuarios.value = respuesta.data
    }

    const getUsuario = async (id) => {
        const respuesta = await UserService.getById(id)
        return respuesta.data
    }

    const crearUsuario = async (datos) => {
        const respuesta = await UserService.create(datos)
        return respuesta.data
    }

    const actualizarUsuario = async (id, datos) => {
        const respuesta = await UserService.update(id, datos)
        return respuesta.data
    }

    const eliminarUsuario = async (id) => {
        const respuesta = await UserService.delete(id)
        return respuesta.data
    }

    return {
        usuarios,
        getUsuarios,
        getUsuario,
        crearUsuario,
        actualizarUsuario,
        eliminarUsuario
    }
})