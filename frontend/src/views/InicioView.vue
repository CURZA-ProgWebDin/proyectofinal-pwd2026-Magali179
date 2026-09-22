<template> <!--parte visual del componente-->
    <div class="inicio-page"> <!--Contenedor principal de la pagina de  inicio-->

        <div class="inicio-contenido"> <!--Contenedor q sirve para organizar y centrar contenido de pantalla-->

            <div v-if="!authStore.is_authenticated">

                <div class="mensaje-bienvenida">
                    Bienvenido al sistema de gestión
                </div>

                <button class="btn-login-inicio" @click="irALogin">
                    Iniciar sesión
                </button>

            </div>
            
        </div>

    </div>
</template>

<script setup>

import { useAuthStore } from '@/stores/auth'// permite importar desde otro archivo la funcion storeAuth.j
import { useRouter } from 'vue-router'// importamos userRouter de Vue Router, para inicio--> login

const authStore = useAuthStore() // Funcio que nos permite acceder al store
const router = useRouter()// Representa el Router de nuestra aplicacion

const irALogin = () => {//Funcion nllamada irALogin
    router.push('/login') // push la dice a login, quiero ir a esa ruta, la ruta q le pasamos es '/login'
}

</script>

<style scoped>

.mensaje-bienvenida {
    display: inline-block;  /* permite que el elemento se comporte como bloque
     pero ocupe solo el espacio necesario */
    padding: 20px 40px; /* espacio interno: 20px arriba/abajo y 40px izquierda/derecha */
    background-color: rgba(255, 250, 243, 0.90); /* fondo claro con 90% de opacidad */
    border: 2px solid #392714;  /* borde de 2px, sólido y color marrón oscuro */
    border-radius: 10px; /* redondea esquinas */
    color: #392714; /* color del texto */
    font-size: 28px; /* tamaño del texto */
    font-weight: 500; /* establece el grosor de la letra */
}

/*hace que la pantalla ocupe toda la ventana, agregar espacio interno y colocar el fondo de la
 librería con una capa clara encima.*/
.inicio-page {
    min-height: 100vh; /* altura mínima igual a toda la pantalla */
    padding: 40px; /* espacio interno de 40px alrededor del contenido */
    background-image: 
        linear-gradient(rgba(255, 248, 238, 0.65), rgba(255, 248, 238, 0.65)),
        url('@/assets/images/fondo-libreria.png'); /* indica donde esta la imagen que usamos como contenido*/
    background-size: cover;
    background-position: center;
    background-attachment: fixed; /* mantiene el fondo fijo al desplazarse */
}

.inicio-contenido {
    max-width: 900px; /* establece un ancho máximo de 900px */
    margin: 0 auto; /* centra horizontalmente el contenedor */
    text-align: center; /* centra horizontalmente el texto */
    padding-top: 120px; /* deja 120px de espacio arriba */
}

.btn-login-inicio {
    display: block;
    margin: 25px auto;
    padding: 14px 40px;
    background-color: #896449;
    border: 2px solid #5A4537;
    border-radius: 8px;
    color: white;
    font-size: 20px;
    font-weight: bold;
    cursor: pointer;
}

</style>