<template>
    <div class="roles-page">

        <h1>Roles</h1>

        <p>Gestión de roles de Librería Suipacha</p>

        <!-- Mensaje de éxito -->
        <div
            v-if="mensaje"
            class="mensaje-exito"
        >
            {{ mensaje }}
        </div>

        <!-- Mensajes de error -->
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

        <!-- Formulario -->
        <div class="rol-formulario">

            <h2>
                {{ editando ? 'Editar rol' : 'Nuevo rol' }}
            </h2>

            <p>* Campos obligatorios</p>

            <form @submit.prevent="guardarRol">

                <div class="campo">
                    <label for="nombre">
                        Nombre *
                    </label>

                    <input
                        id="nombre"
                        type="text"
                        v-model="formulario.nombre"
                    >
                </div>

                <div class="campo">
                    <label for="descripcion">
                        Descripción
                    </label>

                    <input
                        id="descripcion"
                        type="text"
                        v-model="formulario.descripcion"
                    >
                </div>

                <button type="submit">
                    {{ editando ? 'Modificar' : 'Crear rol' }}
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

        <!-- Lista de roles -->
        <div class="roles-lista">

            <h2>Listado de roles</h2>

            <p v-if="roles.length === 0">
                No hay roles registrados.
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
                        v-for="rol in roles"
                        :key="rol.id"
                    >
                        <td>
                            {{ rol.nombre }}
                        </td>

                        <td>
                            {{ rol.descripcion || '' }}
                        </td>

                        <td>

                            <button
                                type="button"
                                @click="editarRol(rol)"
                            >
                                Editar
                            </button>

                            <button
                                type="button"
                                @click="eliminarRol(rol.id)"
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

import { useRolesStore } from '@/stores/roles'


const rolesStore = useRolesStore()


const roles = ref([])

const errores = ref([])

const mensaje = ref('')

const editando = ref(false)

const rolEditandoId = ref(null)


const formulario = ref({
    nombre: '',
    descripcion: ''
})


const cargarRoles = async () => {

    errores.value = []

    try {

        await rolesStore.getRoles()

        roles.value = rolesStore.roles

    } catch (error) {

        errores.value = [
            'No se pudieron cargar los roles'
        ]

    }

}


const limpiarFormulario = () => {

    formulario.value = {
        nombre: '',
        descripcion: ''
    }

    editando.value = false

    rolEditandoId.value = null

}


const cancelarEdicion = () => {

    limpiarFormulario()

    errores.value = []

    mensaje.value = ''

}


const guardarRol = async () => {

    errores.value = []

    mensaje.value = ''


    if (!formulario.value.nombre) {

        errores.value.push(
            'El nombre es requerido'
        )

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

            respuesta = await rolesStore.actualizarRol(
                rolEditandoId.value,
                datos
            )

        } else {

            respuesta = await rolesStore.crearRol(
                datos
            )

        }


        mensaje.value = respuesta.message


        limpiarFormulario()


        await rolesStore.getRoles()

        roles.value = rolesStore.roles


    } catch (error) {

        if (error.response?.data?.errores) {

            errores.value =
                error.response.data.errores

        } else if (error.response?.data?.message) {

            errores.value = [
                error.response.data.message
            ]

        } else {

            errores.value = [
                editando.value
                    ? 'No se pudo modificar el rol'
                    : 'No se pudo crear el rol'
            ]

        }

    }

}


const editarRol = (rol) => {

    editando.value = true

    rolEditandoId.value = rol.id


    formulario.value = {

        nombre: rol.nombre,

        descripcion: rol.descripcion || ''

    }


    errores.value = []

    mensaje.value = ''

}


const eliminarRol = async (id) => {

    errores.value = []

    mensaje.value = ''


    try {

        const respuesta =
            await rolesStore.eliminarRol(id)


        mensaje.value = respuesta.message


        await rolesStore.getRoles()

        roles.value = rolesStore.roles


    } catch (error) {

        if (error.response?.data?.message) {

            errores.value = [
                error.response.data.message
            ]

        } else {

            errores.value = [
                'No se pudo eliminar el rol'
            ]

        }

    }

}


onMounted(() => {

    cargarRoles()

})

</script>


<style scoped>

.roles-page {
    padding: 30px;
}

.roles-page h1 {
    margin-bottom: 10px;
}

.roles-page > p {
    margin-bottom: 20px;
}

.rol-formulario {
    margin-top: 30px;
    margin-bottom: 40px;
}

.rol-formulario h2 {
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

.campo input {
    padding: 8px;
    border: 1px solid #8b5e3c;
    border-radius: 4px;
}

button {
    padding: 8px 15px;
    margin-right: 8px;
    background-color: #8b5e3c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

.mensaje-error {
    color: red;
}

.mensaje-exito {
    color: green;
}

.roles-lista {
    margin-top: 30px;
}

.roles-lista h2 {
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