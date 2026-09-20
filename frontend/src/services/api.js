import axios from 'axios' //traemos axios porque lo usamos para comunicrnos con Flask

const api = axios.create({   //creamos nuestra propia instancia de axios llamad api
    baseURL: 'http://localhost:5001'  //todas las peticiones que haga api comienzan en este localhost
})

export default api  //nos permite importar esta configuracion desde otros archivos