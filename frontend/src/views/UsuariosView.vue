<template>
    <div class="usuarios-page"> <!--  es un contenedor.La class nos permite identificar este div desde CSS. -->

        <h1>Usuarios</h1>

        <p>Gestión de usuarios de Librería Suipacha</p>

        <div class="usuario-formulario">
    <h2>{{ editando ? 'Editar usuario' : 'Nuevo usuario' }}</h2>

    <form @submit.prevent="guardarUsuario">

        <div class="campo">
            <label for="nombre">Nombre *</label>
            <input
                id="nombre"
                type="text"
                v-model="formulario.nombre"
            >
        </div>

        <div class="campo">
            <label for="email">Email *</label>
            <input
                id="email"
                type="email"
                v-model="formulario.email"
            >
        </div>

        <div class="campo">
            <label for="rol">Rol *</label>
            <select
                id="rol"
                v-model="formulario.rol_id"
            >
                <option value="">Seleccione un rol</option>

                <option
                    v-for="rol in roles"
                    :key="rol.id"
                    :value="rol.id"
                >
                    {{ rol.nombre }}
                </option>
            </select>
        </div>

        <div class="campo">
            <label for="password">Contraseña *</label>
            <input
                id="password"
                type="password"
                v-model="formulario.password"
            >
        </div>

        <button type="submit">
            Crear usuario
        </button>

        <p class="obligatorios">* Campos obligatorios</p>

        <div v-if="errores.length > 0" class="mensaje-error">
            <p v-for="(error, index) in errores" :key="index">
                {{ error }}
            </p>
        </div>

        <p v-if="mensaje" class="mensaje-exito">
            {{ mensaje }}
        </p>

    </form>
</div>
       
        <div class="usuarios-lista">

            <h2>Listado de usuarios</h2>

            <table>
                <thead>
                    <tr>
                        <th>Usuario</th>
                        <th>Email</th>
                        <th>Rol</th>
                        <th>Acciones</th>
                    </tr>
                </thead>

                <tbody>
                    <tr v-for="usuario in usuarios" :key="usuario.id">
                        <td>{{ usuario.nombre }}</td>
                        <td>{{ usuario.email }}</td>
                        <td>{{ usuario.rol ? usuario.rol.nombre : '' }}</td>
                        <td>
                            <button
                                type="button"
                                @click="editarUsuario(usuario)"
    >
                                Editar
                            </button>

                            <button
                                type="button"
                                @click="eliminarUsuario(usuario.id)"
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
import { useUsuariosStore } from '@/stores/usuarios'
import { useRolesStore } from '@/stores/roles'

const usuariosStore = useUsuariosStore()
const rolesStore = useRolesStore()

const usuarios = ref([])
const roles = ref([])

const errores = ref([])
const mensaje = ref('')

const editando = ref(false)
const usuarioEditandoId = ref(null)

const formulario = ref({
    nombre: '',
    email: '',
    rol_id: '',
    password: ''
})

const cargarDatos = async () => {
    errores.value = []

    try {
        await usuariosStore.getUsuarios()
        usuarios.value = usuariosStore.usuarios

        await rolesStore.getRoles()
        roles.value = rolesStore.roles
    } catch (error) {
        errores.value = ['No se pudieron cargar los usuarios']
    }
}

const guardarUsuario = async () => {
    errores.value = []
    mensaje.value = ''

    // Validaciones de campos obligatorios
    if (!formulario.value.nombre) {
        errores.value.push('El nombre es requerido')
    }

    if (!formulario.value.email) {
        errores.value.push('El email es requerido')
    }

    if (!formulario.value.rol_id) {
        errores.value.push('El rol es requerido')
    }

    if (!formulario.value.password) {
        errores.value.push('La contraseña es requerida')
    }

    if (errores.value.length > 0) {
        return
    }

   const datos = {
    nombre: formulario.value.nombre,
    email: formulario.value.email,
    rol_id: formulario.value.rol_id,
    password: formulario.value.password
}

try {
    let respuesta

    if (editando.value) {
        respuesta = await usuariosStore.actualizarUsuario(
            usuarioEditandoId.value,
            datos
        )
    } else {
        respuesta = await usuariosStore.crearUsuario(datos)
    }

    mensaje.value = respuesta.message

    formulario.value = {
        nombre: '',
        email: '',
        rol_id: '',
        password: ''
    }

    editando.value = false
    usuarioEditandoId.value = null

    await usuariosStore.getUsuarios()
    usuarios.value = usuariosStore.usuarios

} catch (error) {
    if (error.response?.data?.errores) {
        errores.value = error.response.data.errores
    } else if (error.response?.data?.message) {
        errores.value = [error.response.data.message]
    } else {
        errores.value = [
            editando.value
                ? 'No se pudo modificar el usuario'
                : 'No se pudo crear el usuario'
        ]
    }
}
}

const editarUsuario = (usuario) => {
    editando.value = true
    usuarioEditandoId.value = usuario.id

    formulario.value = {
        nombre: usuario.nombre,
        email: usuario.email,
        rol_id: usuario.rol ? usuario.rol.id : '',
        password: ''
    }

    errores.value = []
    mensaje.value = ''
}

const eliminarUsuario = async (id) => {
    errores.value = []
    mensaje.value = ''

    try {
        const respuesta = await usuariosStore.eliminarUsuario(id)

        mensaje.value = respuesta.message

        await usuariosStore.getUsuarios()
        usuarios.value = usuariosStore.usuarios

    } catch (error) {
        if (error.response?.data?.message) {
            errores.value = [error.response.data.message]
        } else {
            errores.value = ['No se pudo eliminar el usuario']
        }
    }
}


onMounted(() => {
    cargarDatos()
})
</script>

<style>
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
.usuario-formulario {
    margin-top: 30px;
    margin-bottom: 40px;
}

.usuario-formulario h2 {
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
.campo select {
    padding: 8px;
    border: 1px solid #8b5e3c;
    border-radius: 4px;
}

.usuario-formulario button {
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
</style>