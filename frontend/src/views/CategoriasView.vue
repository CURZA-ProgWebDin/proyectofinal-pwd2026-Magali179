<template>
    <div class="categorias-page">

        <h1>Categorías</h1>

        <p>Gestión de categorías de Librería Suipacha</p>

        <div
            v-if="mensaje"
            class="mensaje-exito"
        >
            {{ mensaje }}
        </div>

        <div
            v-if="errores.length"
            class="mensaje-error"
        >
            <p
                v-for="(error, index) in errores"
                :key="index"
            >
                {{ error }}
            </p>
        </div>

        <div class="categoria-formulario">

            <h2>
                {{ editando ? 'Editar categoría' : 'Nueva categoría' }}
            </h2>

            <p>* Campos obligatorios</p>

            <form @submit.prevent="guardarCategoria">

                <div class="campo">
                    <label>Nombre *</label>

                    <input
                        type="text"
                        v-model="formulario.nombre"
                    >
                </div>

                <div class="campo">
                    <label>Descripción</label>

                    <textarea
                        v-model="formulario.descripcion"
                    ></textarea>
                </div>

                <div class="botones-formulario">

                    <button
                        type="submit"
                        class="btn-guardar"
                    >
                        {{ editando ? 'Modificar' : 'Guardar' }}
                    </button>

                    <button
                        v-if="editando"
                        type="button"
                        class="btn-cancelar"
                        @click="cancelarFormulario"
                    >
                        Cancelar
                    </button>

                </div>

            </form>

        </div>

        <div class="lista-categorias">

            <h2>Categorías registradas</h2>

            <p v-if="categorias.length === 0">
                No hay categorías registradas.
            </p>

            <table v-else>

                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Descripción</th>
                        <th>Acciones</th>
                    </tr>
                </thead>

                <tbody>

                    <tr
                        v-for="categoria in categorias"
                        :key="categoria.id"
                    >
                        <td>{{ categoria.nombre }}</td>

                        <td>
                            {{ categoria.descripcion || 'Sin descripción' }}
                        </td>

                        <td>

                            <button
                                type="button"
                                @click="editarCategoria(categoria)"
                            >
                                Editar
                            </button>

                            <button
                                type="button"
                                @click="eliminarCategoria(categoria.id)"
                            >
                                Eliminar
                            </button>

                        </td>
                    </tr>

                </tbody>

            </table>

        </div>

    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCategoriasStore } from '@/stores/categorias'

const categoriasStore = useCategoriasStore()

const categorias = ref([])

const errores = ref([])
const mensaje = ref('')

const editando = ref(false)
const categoriaEditandoId = ref(null)

const formulario = ref({
    nombre: '',
    descripcion: ''
})

const cargarCategorias = async () => {
    errores.value = []

    try {
        await categoriasStore.getCategorias()
        categorias.value = categoriasStore.categorias
    } catch (error) {
        errores.value = ['No se pudieron cargar las categorías']
    }
}

const guardarCategoria = async () => {
    errores.value = []
    mensaje.value = ''

    if (!formulario.value.nombre) {
        errores.value.push('El nombre es requerido')
    }

    if (errores.value.length > 0) {
        return
    }

    const datos = {
        nombre: formulario.value.nombre,
        descripcion: formulario.value.descripcion
    }

    try {
        let respuesta

        if (editando.value) {
            respuesta = await categoriasStore.actualizarCategoria(
                categoriaEditandoId.value,
                datos
            )
        } else {
            respuesta = await categoriasStore.crearCategoria(datos)
        }

        mensaje.value = respuesta.message

        formulario.value = {
            nombre: '',
            descripcion: ''
        }

        editando.value = false
        categoriaEditandoId.value = null

        await categoriasStore.getCategorias()
        categorias.value = categoriasStore.categorias

    } catch (error) {
        if (error.response?.data?.errores) {
            errores.value = error.response.data.errores
        } else if (error.response?.data?.message) {
            errores.value = [error.response.data.message]
        } else {
            errores.value = [
                editando.value
                    ? 'No se pudo modificar la categoría'
                    : 'No se pudo crear la categoría'
            ]
        }
    }
}

const editarCategoria = (categoria) => {
    editando.value = true
    categoriaEditandoId.value = categoria.id

    formulario.value = {
        nombre: categoria.nombre,
        descripcion: categoria.descripcion || ''
    }

    errores.value = []
    mensaje.value = ''
}

const cancelarFormulario = () => {
    formulario.value = {
        nombre: '',
        descripcion: ''
    }

    editando.value = false
    categoriaEditandoId.value = null

    errores.value = []
    mensaje.value = ''
}

const eliminarCategoria = async (id) => {
    errores.value = []
    mensaje.value = ''

    try {
        const respuesta = await categoriasStore.eliminarCategoria(id)

        mensaje.value = respuesta.message

        await categoriasStore.getCategorias()
        categorias.value = categoriasStore.categorias

    } catch (error) {
        if (error.response?.data?.message) {
            errores.value = [error.response.data.message]
        } else {
            errores.value = ['No se pudo eliminar la categoría']
        }
    }
}

onMounted(() => {
    cargarCategorias()
})
</script>

<style scoped>
.categorias-page {
    padding: 30px;
}

.categorias-page h1 {
    margin-bottom: 10px;
}

.categorias-page > p {
    margin-bottom: 20px;
}

.categoria-formulario {
    margin-top: 30px;
    margin-bottom: 40px;
}

.categoria-formulario h2 {
    margin-bottom: 15px;
}

.campo {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
    max-width: 500px;
}

.campo label {
    margin-bottom: 5px;
    font-weight: bold;
}

.campo input,
.campo textarea {
    padding: 8px;
    border: 1px solid #8b5e3c;
    border-radius: 4px;
}

.campo textarea {
    min-height: 80px;
    resize: vertical;
}

.categoria-formulario button {
    padding: 8px 15px;
    background-color: #8b5e3c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.obligatorios {
    margin-top: 10px;
    font-size: 14px;
}

.mensaje-error {
    color: red;
}

.mensaje-exito {
    color: green;
}

.lista-categorias {
    margin-top: 30px;
}

.lista-categorias h2 {
    margin-bottom: 15px;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th,
td {
    padding: 8px 10px;
    border: 3px solid #8b5e3c;
    text-align: left;
}
</style>