import { ref } from 'vue' // Traemos ref de Vue, para uardqr productos en variable reactiva ref([])
import { defineStore } from 'pinia' //Trae defineStore(crrear store de pinia) desde  pinia
import ProductoService from '@/services/ProductoService'//Importa el ProductoService. ProductoService.js 
                                                        // se comunica con backend por medio de xios.
//@ representa carpeta src/== @/services/ProductoService== src/services/ProductoService.js

export const useProductosStore = defineStore('productos', () => { //Creamos el Store d eproductos
    //export= que este Store pueda ser utilizado desde otros archivos
    //const= Estamos creando una constante llamada: useProductosStore
    //Definestore, funcion de pinia importada antes q usamos para crear nuestro store
    //() => {= sintaxis setup de Pinia

    const productos = ref([]) //Sera nuestra lista de productos, importamos ref de Vue
                            //El array se llenara con productos que devuelva Flask

    const getProductos = async () => {//Linea q crea funcion llamada getProductos, obtendremos "productos"
                                        //Async= operacion asincrona, nos comunicamos con varias instancias
                                        //y eso nomes i9nstantaneo: Store → Service → Axios → Flask
                                        //productos.js ↓ ProductoService.js ↓backend Flask
        const respuesta = await ProductoService.getAll() //Le pedimos al backend todos los productos
        productos.value = respuesta.data//Guardamos en el store los productos que llegan del backend
    }

    const getProducto = async (id) => {//Obtener producto especifico por su ID
        const respuesta = await ProductoService.getById(id)
        return respuesta.data
    }

    const crearProducto = async (datos) => { //Creando funcion Producto, la func recibe "datos"
                                            //Async x q se va a comunicar con backend y debe esperar resp.
        
        const respuesta = await ProductoService.create(datos)//await espera resp. de Flask antes de continuar
        return respuesta.data//Contiene lo que devolvio Flask
    }

    const actualizarProducto = async (id, datos) => {//Modificar producto que ya existe, recibe parametros ID y data
        const respuesta = await ProductoService.update(id, datos)
        return respuesta.data
    }

    const eliminarProducto = async (id) => {//Recibe ID del producto a elimninar
        const respuesta = await ProductoService.delete(id)
        return respuesta.data
    }

    return { //expone hacia afuera del Store todo lo que queremos que puedan utilizar nuestras 
            // vistas u otros componentes
        productos, //Expone funcion que obtiene productos
        getProductos, //Expone funcion que obtiene ztodos los productos
        getProducto,//Expone funcion que obtiene 1 producto x su ID
        crearProducto,//Expone funcion q permite crear 1 producto
        actualizarProducto,//Expone funcion que permite modificar un producto existente
        eliminarProducto//Expone funcion q permite eliminar 1 producto
    }
})