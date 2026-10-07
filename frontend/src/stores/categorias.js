import { ref } from 'vue'
import { defineStore } from 'pinia'
import CategoriaService from '@/services/CategoriaService'

export const useCategoriasStore = defineStore('categorias', () => {

    const categorias = ref([])

    const getCategorias = async () => {
        const respuesta = await CategoriaService.getAll()
        categorias.value = respuesta.data
    }

    const getCategoria = async (id) => {
        const respuesta = await CategoriaService.getById(id)
        return respuesta.data
    }

    const crearCategoria = async (datos) => {
        const respuesta = await CategoriaService.create(datos)
        return respuesta.data
    }

    const actualizarCategoria = async (id, datos) => {
        const respuesta = await CategoriaService.update(id, datos)
        return respuesta.data
    }

    const eliminarCategoria = async (id) => {
        const respuesta = await CategoriaService.delete(id)
        return respuesta.data
    }

    return {
        categorias,
        getCategorias,
        getCategoria,
        crearCategoria,
        actualizarCategoria,
        eliminarCategoria
    }
})