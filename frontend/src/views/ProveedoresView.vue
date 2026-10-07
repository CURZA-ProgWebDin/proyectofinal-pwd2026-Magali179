<template>
    <div class="proveedores-page">

        <h1>Proveedores</h1>

        <p>Gestión de proveedores de Librería Suipacha</p>

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
                v-for="error in errores"
                :key="error"
            >
                {{ error }}
            </p>
        </div>

        <div class="proveedor-formulario">

            <h2>
                {{ editando ? 'Editar proveedor' : 'Nuevo proveedor' }}
            </h2>

            <p>* Campos obligatorios</p>

            <form @submit.prevent="guardarProveedor">

                <div class="campo">
                    <label>Nombre *</label>

                    <input
                        type="text"
                        v-model="formulario.nombre"
                    >
                </div>

                <div class="campo">
                    <label>Contacto</label>

                    <input
                        type="text"
                        v-model="formulario.contacto"
                    >
                </div>

                <div class="campo">
                    <label>Teléfono</label>

                    <input
                        type="text"
                        v-model="formulario.telefono"
                    >
                </div>

                <div class="campo">
                    <label>Email</label>

                    <input
                        type="email"
                        v-model="formulario.email"
                    >
                </div>

                <button type="submit">
                    {{ editando ? 'Modificar' : 'Guardar' }}
                </button>

                <button
                    v-if="editando"
                    type="button"
                    @click="cancelarEdicion"
                >
                    Cancelar
                </button>

            </form>

        </div>

        <div class="proveedores-lista">

            <h2>Proveedores registrados</h2>

            <p v-if="proveedores.length === 0">
                No hay proveedores registrados.
            </p>

            <table v-else>

                <thead>
                    <tr>
                        <th>Nombre</th>
                        <th>Contacto</th>
                        <th>Teléfono</th>
                        <th>Email</th>
                        <th>Acciones</th>
                    </tr>
                </thead>

                <tbody>

                    <tr
                        v-for="proveedor in proveedores"
                        :key="proveedor.id"
                    >

                        <td>{{ proveedor.nombre }}</td>
                        <td>{{ proveedor.contacto }}</td>
                        <td>{{ proveedor.telefono }}</td>
                        <td>{{ proveedor.email }}</td>

                        <td>
                            <button
                                type="button"
                                @click="editarProveedor(proveedor)"
                            >
                                Editar
                            </button>

                            <button
                                type="button"
                                @click="eliminarProveedor(proveedor.id)"
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
import { useProveedoresStore } from '@/stores/proveedores'

const proveedoresStore = useProveedoresStore()

const proveedores = ref([])

const errores = ref([])
const mensaje = ref('')

const editando = ref(false)
const proveedorEditandoId = ref(null)

const formulario = ref({
    nombre: '',
    contacto: '',
    telefono: '',
    email: ''
})

const cargarProveedores = async () => {
    errores.value = []

    try {
        await proveedoresStore.getProveedores()
        proveedores.value = proveedoresStore.proveedores
    } catch (error) {
        errores.value = ['No se pudieron cargar los proveedores']
    }
}

const guardarProveedor = async () => {
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
        contacto: formulario.value.contacto,
        telefono: formulario.value.telefono,
        email: formulario.value.email
    }

    try {
        let respuesta

        if (editando.value) {
            respuesta = await proveedoresStore.actualizarProveedor(
                proveedorEditandoId.value,
                datos
            )
        } else {
            respuesta = await proveedoresStore.crearProveedor(datos)
        }

        mensaje.value = respuesta.message

        limpiarFormulario()

        await proveedoresStore.getProveedores()
        proveedores.value = proveedoresStore.proveedores

    } catch (error) {
        if (error.response?.data?.errores) {
            errores.value = error.response.data.errores
        } else if (error.response?.data?.message) {
            errores.value = [error.response.data.message]
        } else {
            errores.value = [
                editando.value
                    ? 'No se pudo modificar el proveedor'
                    : 'No se pudo crear el proveedor'
            ]
        }
    }
}

const editarProveedor = (proveedor) => {
    editando.value = true
    proveedorEditandoId.value = proveedor.id

    formulario.value = {
        nombre: proveedor.nombre,
        contacto: proveedor.contacto || '',
        telefono: proveedor.telefono || '',
        email: proveedor.email || ''
    }

    errores.value = []
    mensaje.value = ''
}

const eliminarProveedor = async (id) => {
    errores.value = []
    mensaje.value = ''

    try {
        const respuesta = await proveedoresStore.eliminarProveedor(id)

        mensaje.value = respuesta.message

        await proveedoresStore.getProveedores()
        proveedores.value = proveedoresStore.proveedores

    } catch (error) {
        if (error.response?.data?.message) {
            errores.value = [error.response.data.message]
        } else {
            errores.value = ['No se pudo eliminar el proveedor']
        }
    }
}

const limpiarFormulario = () => {
    formulario.value = {
        nombre: '',
        contacto: '',
        telefono: '',
        email: ''
    }

    editando.value = false
    proveedorEditandoId.value = null
}

onMounted(() => {
    cargarProveedores()
})
</script>

<style scoped>
.proveedores-page {
    padding: 30px;
}

.proveedores-page h1 {
    margin-bottom: 10px;
}

.proveedores-page > p {
    margin-bottom: 20px;
}

.proveedor-formulario {
    margin-top: 30px;
    margin-bottom: 40px;
}

.proveedor-formulario h2 {
    margin-bottom: 20px;
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

.botones-formulario {
    display: flex;
    gap: 10px;
    margin-top: 20px;
}

.botones-formulario button {
    padding: 8px 15px;
    border-radius: 4px;
    cursor: pointer;
}

.btn-guardar {
    background-color: #8b5e3c;
    color: white;
    border: none;
}

.btn-cancelar {
    background-color: white;
    color: #8b5e3c;
    border: 1px solid #8b5e3c;
}

.lista-proveedores {
    margin-top: 30px;
}

.lista-proveedores h2 {
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

th {
    font-weight: bold;
}

button {
    cursor: pointer;
}

.btn-editar,
.btn-eliminar {
    padding: 6px 10px;
    margin-right: 5px;
    border-radius: 4px;
    border: 1px solid #8b5e3c;
    background-color: white;
    color: #8b5e3c;
}

.mensaje-error {
    color: red;
    margin-top: 10px;
}

.mensaje-exito {
    color: green;
    margin-top: 10px;
}

.obligatorios {
    margin-top: 10px;
    font-size: 14px;
}
</style>