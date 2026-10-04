<template> <!--part visual del componente vue-->

    <div class="movimientos-page"> <!--Contenor principal de toda la pantlla de movimientos-->

        <div class="movimientos-contenido"> <!--Organiza movimiento interno-->

            <div class="encabezado-movimientos"><!--agrupa iconos q pondremos en parte superior de pantlla(titulos,botones)-->

                <h1>Movimientos</h1>

                <div class="botones-movimientos">

                    <!--#solo admin ve todos los movimientos-->
                    <button
                        v-if="authStore.rol_user === 'admin'" 
                        class="btn-movimientos"
                        @click="mostrarTodos"
                    >
                        Todos los movimientos
                    </button>

                    <button
                        class="btn-movimientos"
                        @click="mostrarMisMovimientos"
                    >
                        Mis movimientos
                    </button>

                </div>

            </div>

            <div
                v-if="errores.length"
                class="mensaje-error"
            >

                <p
                    v-for="error in errores"
                    :key="error"
                >
                    {{ error }}
                </p>

            </div>

            <div
                v-if="productoSeleccionado"
                class="formulario-movimiento"
            >

                <h2>Registrar venta</h2>

                <p>
                    <strong>Libro:</strong>
                    {{ productoSeleccionado.nombre }}
                </p>

                <p>
                    <strong>Stock disponible:</strong>
                    {{ productoSeleccionado.stock_actual }}
                </p>

                <label>
                    Cantidad:

                    <input
                        v-model.number="cantidad"
                        type="number"
                        min="1"
                        :max="productoSeleccionado.stock_actual"
                    >
                </label>

                <label>
                    Motivo:

                    <input
                        v-model="motivo"
                        type="text"
                    >
                </label>

                <button
                    class="btn-movimientos"
                    @click="registrarMovimiento"
                >
                    Registrar venta
                </button>

                <p
                    v-if="errorMovimiento"
                    class="mensaje-error"
                >
                    {{ errorMovimiento }}
                </p>

                <p
                    v-if="mensajeMovimiento"
                    class="mensaje-exito"
                >
                    {{ mensajeMovimiento }}
                </p>

            </div>

            <div class="lista-movimientos">

                <h2>
                    {{ mostrandoMisMovimientos
                        ? 'Mis movimientos'
                        : 'Todos los movimientos'
                    }}
                </h2>

                <p v-if="movimientos.length === 0">
                    No hay movimientos registrados.
                </p>

                <table v-else>

                    <thead>

                        <tr>

                            <th
                                v-for="columna in columnas"
                                :key="columna"
                            >
                                {{ columna }}
                            </th>

                        </tr>

                    </thead>

                    <tbody>

                        <tr
                            v-for="movimiento in movimientos"
                            :key="movimiento.id"
                        >

                            <td
                                v-for="columna in columnas"
                                :key="columna"
                            >
                                {{ mostrarValor(movimiento[columna]) }}
                            </td>

                        </tr>

                    </tbody>

                </table>

            </div>

        </div>

    </div>

</template>

<script setup>
// ppr que necesitamos auth.js? poruqe nuestra regla es que todos los mo0vimientos solo los ve el admin 

import { ref, computed, onMounted } from 'vue'//Tres funciones de vue; ref, computed y onMounted
import { useMovimientosStore } from '@/stores/movimientos'//Importamos store de movimientoss
import { useAuthStore } from '@/stores/auth'
//Tenemos 2 stores porque necesitamos 2 tipos de info
import { useRoute } from 'vue-router'//nos permite leer el id q viene en la url
import { useProductosStore } from '@/stores/productos'//nos permite buscar los datos del libro seleccionado

const movimientosStore = useMovimientosStore()// Utilizar el store de movientos dentro de MovimientosView
// crea el acceso l store de moviminetos dentro de ese componente
const authStore = useAuthStore()//Nos dice quien esta logueqado y cual es su rol
const route = useRoute()//Permite acceder a los datos de la ruta y leer el id del libro
const productosStore = useProductosStore()//Accedemos al store del producto para obtener los datos del libro

const movimientos = ref([])

const errores = ref([])

const mostrandoMisMovimientos = ref(false)

const productoSeleccionado = ref(null)//Guarda los datros del libro seleccionado
const cantidad = ref(1)//Guarda cantidad de libros a vender
const motivo = ref('Venta')//Motivo del movimiento, venta
const errorMovimiento = ref('')//Guarda mensaje si ocurre error al registrar el movimiento
const mensajeMovimiento = ref('')//Guarda mensaje de confirmacion de movimiento, venta

const columnas = computed(() => {//columnas-varibles/crea una propiedad llamada columnas

    if (movimientos.value.length === 0) { //la lista estabvacia?/length=cuantos mov hay
        return [] // si no hay nada en lsta=o devolvemos return
    }

    return Object.keys(movimientos.value[0])//pero si hay mov los mostramos

})

const mostrarValor = (valor) => {//funcion "moswtrarValor"/ preprara un nvalor antes de mostrarlo en cada tabls(mostrarValor)

    if (valor === null || valor === undefined) {// si valor es 0 o nulo retorna texto vacio ''
        return ''
    }

    if (typeof valor === 'object') {//que tipo de dato, si es objeto retornamos texto. si no es null
        //undefined ni objeto retornamos valor original
        return JSON.stringify(valor)
    }

    return valor
}

const mostrarTodos = async () => {// funcion mostrarTodos/obj. cargar mov de todos los uduarios

    errores.value = [] // antes de consultar limpiamos lista de errores, vuelve a estar vacia
    mostrandoMisMovimientos.value = false// q tipo de mov estamos mostrando, si es false=todos mov
    //si es true= misMovimientos
    //como vamosa mostrar todos los mov es "false"

    try {

        await movimientosStore.getMovimientos()//pedimos los movimientos y llamammos getMovimientos()

        movimientos.value = movimientosStore.movimientos// si obtenemos mov lo mostramos enn tabla
        // y si falla? entramos al catch/guardamos mensaje dentro de nuestro array de errores
    } catch (error) {

        errores.value = [
            'No se pudieron cargar los movimientos'
        ]

    }

}

const mostrarMisMovimientos = async () => {// funcion mis mostrarMisMovimientos

    errores.value = []//antees de consulta limpiamos los errores anteriores
    mostrandoMisMovimientos.value = true//true= estamos mostrando nuesttos movimientos

    try {//en este bloque intentaremos mostrar movimientos

        const respuesta = await movimientosStore.getMisMovimientos()//llamamos al store, pero prrimero
        //guardamos en "respuesta" lo que devuelcve el store

        movimientos.value = respuesta //guardamos movimientos

    } catch (error) {// si ocurre error, guardamos mensaje "error"

        errores.value = [
            'No se pudieron cargar tus movimientos'
        ]

    }

}
const cargarProductoSeleccionado = async () => {

    const productoId = route.query.producto_id // Obtiene el ID del libro desde la URL.

    if (!productoId) {
        return // Si no hay producto seleccionado, no hace nada.
    }

    try {

        productoSeleccionado.value =
            await productosStore.getProducto(Number(productoId))
        // Busca en el backend los datos del libro seleccionado.

    } catch (error) {

        errorMovimiento.value =
            'No se pudo cargar el libro seleccionado'
        // Guarda un mensaje si no se pudo obtener el libro.

    }

}
const registrarMovimiento = async () => {
    console.log('Se hizo clic en Registrar venta')

    errorMovimiento.value = ''
    mensajeMovimiento.value = ''

    try {

        const respuesta = await movimientosStore.crearMovimiento({
            tipo_movimiento: 'salida',
            cantidad: cantidad.value,
            motivo: motivo.value,
            producto_id: productoSeleccionado.value.id
        })

        mensajeMovimiento.value = respuesta.message
        if (authStore.rol_user === 'admin') {
        await mostrarTodos()
        } else {
            await mostrarMisMovimientos()
        }

    } catch (error) {

        if (error.response?.data?.message) {

            errorMovimiento.value = error.response.data.message

        } else if (error.response?.data?.errores) {

            errorMovimiento.value =
                error.response.data.errores.join(', ')

        } else {

            errorMovimiento.value =
                'No se pudo registrar el movimiento'

        }

    }

}

onMounted(async () => {

    await cargarProductoSeleccionado()
    // Carga el libro seleccionado desde el producto_id de la URL.

    if (authStore.rol_user === 'admin') {

        await mostrarTodos()
        // Si es admin, muestra todos los movimientos.

    } else {

        await mostrarMisMovimientos()
        // Si es operador, muestra solamente sus movimientos.

    }

})
    


</script>

<style scoped>

.movimientos-page {
    min-height: 100vh;
    padding: 40px;
    background-image:
        linear-gradient(
            rgba(255, 248, 238, 0.65),
            rgba(255, 248, 238, 0.65)
        ),
        url('@/assets/images/fondo-libreria.png');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.movimientos-contenido {
    max-width: 1100px;
    margin: 0 auto;
}

.encabezado-movimientos {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 30px;
}

.encabezado-movimientos h1 {
    color: #392714;
    font-size: 32px;
}

.botones-movimientos {
    display: flex;
    gap: 15px;
}

.btn-movimientos {
    padding: 12px 20px;
    background-color: #896449;
    border: 2px solid #5A4537;
    border-radius: 8px;
    color: white;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
}

.btn-movimientos:hover {
    background-color: #715B4C;
}

.mensaje-error {
    margin-bottom: 20px;
    padding: 15px;
    background-color: rgba(255, 230, 230, 0.95);
    border: 2px solid #8B0000;
    border-radius: 8px;
    color: #8B0000;
}

.lista-movimientos {
    background-color: rgba(255, 250, 243, 0.95);
    padding: 25px;
    border-radius: 12px;
    border: 2px solid #896449;
    overflow-x: auto;
}

.lista-movimientos h2 {
    color: #392714;
    margin-bottom: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th,
td {
    padding: 12px;
    border: 1px solid #5A4537;
    text-align: center;
}

th {
    background-color: #D6B796;
    color: #392714;
}

td {
    color: #392714;
}

</style>