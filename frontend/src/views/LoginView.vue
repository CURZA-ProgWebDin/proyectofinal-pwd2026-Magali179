<template>
    <div class="login-page">

        <div class="login-container">

            <h1 class="titulo-login">Libreria Suipacha</h1>
            <h2 class="subtitulo-login">Iniciar Sesion</h2>

            <form @submit.prevent="iniciarSesion">
                <div class="formulario">
                    <label class="label-login">Usuario</label>
                    <input type="text" v-model="usuario">
                </div>
                <div class="formulario">

                    <label class="label-login">Contraseña</label>
                    <input type="password" v-model="password">
                </div>

            <button class="btn-login" type="submit" >Iniciar</button>
            
            </form>
        </div>
    </div>
    
</template>


<script setup>
import { ref } from 'vue'
import AuthService from '@/services/AuthService'
import { useAuthStore } from '@/stores/auth' //trae la función que nos permite
//  acceder al store de autenticación.
import { useRouter } from 'vue-router' //es una función que nos proporciona Vue Route
//Nos permite obtener acceso al Router desde nuestro componente LoginView.vue.

const usuario = ref('')
const password = ref('')
const authStore = useAuthStore()
const router = useRouter() //Obtenemos el objeto router, que nos permite utilizar las funciones del Router.

const iniciarSesion = async () => {

    

    console.log(usuario.value)
    console.log(password.value)

    const datos = {
        nombre: usuario.value,
        password: password.value
    }

    const respuesta = await AuthService.login(datos)
    
    authStore.login(respuesta.data)

    router.push('/inicio')


}
</script>
<style scoped>

    .login-page {
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}
   .login-container {
    width: 380px; /*  Define el ancho de nuestra tarjeta. */
    padding: 30px;  /* espacio entre el contenido y los bordes de la tarjeta. */
    background-color: white;
    border-radius: 10px;
}
.formulario {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
}
.btn-login {
    width: 100%; /*boton ocupa todo el ancho disponible*/
    padding: 10px; /* agregfa espqcio interno y qumenta altur*/
    border: none; /*elinina borfde predeterminado por el navegdor*/
    border-radius: 6px; /*redonde esquinas*/
    cursor: pointer; /*pasamos el mauose por eriba del bton y e[se conviete en icono mamo que puede clicker*/
}
.btn-login:hover {
    opacity: 0.8; /* Hace que el botón sea un poco transparente al pasar el mouse */
}
.titulo-login {
    text-align: center; /*Centra el texto dentro del espacio disponible:*/
    margin-bottom: 10px; /*Agrega espacio por debajo del elemento.*/
}

.subtitulo-login {
    text-align: center;
    margin-bottom: 25px;
}
.label-login {
    margin-bottom: 5px;
}
</style>