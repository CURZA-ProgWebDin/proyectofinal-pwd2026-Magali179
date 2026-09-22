import { ref } from 'vue'
import { defineStore } from 'pinia'
import MovimientoService from '@/services/MovimientoService'

export const useMovimientosStore = defineStore('movimientos', () => {

    const movimientos = ref([])

    const getMovimientos = async () => { //Obtener todos los movimientos
        const respuesta = await MovimientoService.getAll()
        movimientos.value = respuesta.data
    }

    const getMisMovimientos = async () => {//Obtener movimientos del usuario q corresponda
        const respuesta = await MovimientoService.getMis()
        return respuesta.data
    }

    const getMovimiento = async (id) => {
        const respuesta = await MovimientoService.getById(id)
        return respuesta.data
    }

    const crearMovimiento = async (datos) => {
        const respuesta = await MovimientoService.create(datos)
        return respuesta.data
    }

    const eliminarMovimiento = async (id) => {
        const respuesta = await MovimientoService.delete(id)
        return respuesta.data
    }

    return {
        movimientos,
        getMovimientos,
        getMisMovimientos,
        getMovimiento,
        crearMovimiento,
        eliminarMovimiento
    }
})