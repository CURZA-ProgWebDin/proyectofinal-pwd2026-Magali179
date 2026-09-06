<template>
    <div class="login-page">

        <div class="login-container">

            <h1>Libreria Suipacha</h1>
            <h2>Iniciar Sesion</h2>

            <form>
                <div class="formulario">
                    <label>Usuario</label>
                    <input type="text"v-model="usuario">
                </div>
                <div class="formulario">

                    <label>Contraseña</label>
                    <input type="password" v-model="password">
                </div>

            <button type="submit">Ingresar</button>
            
            </form>
        </div>
    </div>
    
</template>


<script setup>
import { ref } from 'vue'

const usuario = ref('')
const password = ref('')
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
</style>