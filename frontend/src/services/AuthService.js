import api from './api' //trae nuestro api desde api.js/ "./" =Buscá api.js en la misma carpeta donde estoy

const AuthService = {   // Creamos la constante, servicio de autenticacion.operaciones 
                        // relacionadas con inicio de sesion

    login(datos) { //Funcion login q recibe parametro "datos". los datos salen de loginView.vue
        return api.post('/login', datos) //Linea q se comunica con Flask
                                        //El backend espera una petición HTTP POST para iniciar sesión
                        //Hacé una petición POST al endpoint /login y enviá estos datos
    }

}
//La dirección completa termina siendo: http://localhost:5001/login

export default AuthService 
//Esta line hace que AuthServiceService.js pueda ser utilizado desde otros archivos
//de otra manera no podemos importar el objeto