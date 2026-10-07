import axios from 'axios' //traemos axios porque lo usamos para comunicrnos con Flask
import { useAuthStore } from '@/stores/auth'//permite acceder al jwt q guardamos al iniciar sesion

const api = axios.create({   //creamos nuestra propia instancia de axios llamada api
    baseURL: 'http://localhost:5001'  //todas las peticiones que haga api comienzan en este localhost
})

api.interceptors.request.use((config) => {//antes de enviar la petición, ejecuta esta función

    const authStore = useAuthStore()//obtenemos store de autenticacion

    if (authStore.jwt) {//preguntamos si tenemos un jwt guardado en el store de autenticacion
        config.headers.Authorization = `Bearer ${authStore.jwt}`//si tenemos jwt, lo agregamos 
        // a la cabecera de la petición
    }

    return config
})

export default api  //permite importar esta configuración desde otros archivos