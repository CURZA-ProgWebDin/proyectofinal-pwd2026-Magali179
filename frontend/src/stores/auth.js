import { ref } from 'vue'  //datos reactivos
import { defineStore } from 'pinia' //trae la función que necesitamos para crear nuestro store de Pinia.

// crear store
export const useAuthStore = defineStore('auth', () => {
    //usuario autenticado
    const auth_user = ref('')
    const jwt = ref('')
    const rol_user = ref('')
    const is_authenticated = ref(false)
    // login
    const login = (data) => {

        auth_user.value = data.nombre
        jwt.value = data.access_token
        //. Guardamos el rol
        rol_user.value = data.rol
        //Guardamos el JWT
        is_authenticated.value = true

    }

    return {  //"Estas son las cosas del Store que quiero 
    // que estén disponibles para los componentes que lo utilicen."
        auth_user,
        jwt,
        rol_user,
        is_authenticated,
        login
    }

})