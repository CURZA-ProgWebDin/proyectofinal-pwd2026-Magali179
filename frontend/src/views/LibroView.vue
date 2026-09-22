<template> <!--parte fvisual del componente-->
    <div class="libros-page"> <!--contenedor ppal para toda lapantalla, con css-->

        <div class="libros-contenido"> <!--Contenido de la pantalla-->

            <div class="encabezado-libros"> <!--Agrupa  elementos en l pate superior de la pantalla-->
                <h1>Libros</h1> <!--titulo principal de esta view-->
                <!--B
                oton para agregar libro-->
                <!--class= se le asigna clase css al boton y @clik=escuchar even to-->
                <button 
                    class="btn-agregar" 
                    @click="abrirFormulario">
                    Agregar libro
                </button>
            </div>

            <!--v-if==Mostrar el elemento si la condicion es verdadera-->

            <!--class= paqa css-->
            <!--{{ mensaje }} sirve para mostrar en el HTML elm valor de 1 vriable-->
             <!--Si mensje es falso no se muestra, si es true si-->

             <!--v-if/length= tenemos una constante [] quw guardra los errores -->
             <!--si no hy errores es falso silos hay es veddeo y lo mostrara-->
             <!--class= estulos css-->
             <!--v-for recorre nuestron arreglo, recorre 1 por 1-->
             <!--:key le permite a vue identificar cada elemento de la lista cuandousamos v-for-->
           
           
             <div
                v-if="mensaje"
                class="mensaje-exito"
            >
                {{ mensaje }}
            </div>

             <!--v-if= form se muestr cuando inkivciamos pantalla-->
            <!--usuario ejecuta mostrsr libro y se ejecuta abrirformulario()-->
            <!--Si es falso formulario oculto-->
            <!--css del fomrmulario-->
            <div
                v-if="errores.length"
                class="mensaje-error"
            >
                <p
                    v-for="error in errores"
                    :key="error"
                >
                    {{ error }}
                </p>
            </div>

            <div
                v-if="mostrarFormulario"
                class="formulario-libro"
            >

                <!--Si editando es verdadero, mostrar "Editar libro". Si es falso, mostrar "Nuevo libro"-->
                <h2>
                    {{ editando ? 'Editar libro' : 'Nuevo libro' }}
                </h2>

                <p>* Campos obligatorios</p>

                <!--@submit ocurre cuando se envi el formulario, ennnuestro caso el usuario 
                apretara el boton "guardar-->
                <!-- prevent= evita que se recargue la pagina al enviar formualrio-->
                <!-- Indica la funcion que queremos ejecutar cuando se envia el formulario-->
                <form @submit.prevent="guardarProducto">

                    <!--v-model establece vinculo entre elinput yun propiedad el objeto form-->
                    <!--Por q v-model?=cuandom ejecutemos guardarProducto() obtnemos 
                    formulario.value.nombre-->
                    <div class="campo">
                        <label>Nombre *</label>
                        <input
                            type="text"
                            v-model="formulario.nombre"
                        >
                    </div>
                

                    
                    <div class="campo">
                        <label>Autor *</label>
                        <input
                            type="text"
                            v-model="formulario.autor"
                        >
                    </div>

                    <!--textarea= para que el texto pieda ocpar varias lineas-->
                    <div class="campo">
                        <label>Descripción</label>
                        <textarea
                            v-model="formulario.descripcion"
                        ></textarea>
                    </div>

                    <!--step=podemos trabajar con vlores con 2 decimles-->
                    <div class="campo">
                        <label>Precio de costo *</label>
                        <input
                            type="number"
                            step="0.01"
                            v-model="formulario.precio_costo"
                        >
                    </div>

                    <div class="campo">
                        <label>Precio de venta *</label>
                        <input
                            type="number"
                            step="0.01"
                            v-model="formulario.precio_venta"
                        >
                    </div>

                    <div class="campo">
                        <label>Stock actual *</label>
                        <input
                            type="number"
                            min="0"
                            v-model="formulario.stock_actual"
                        >
                    </div>

                    <div class="campo">
                        <label>Stock mínimo *</label>
                        <input
                            type="number"
                            min="0"
                            v-model="formulario.stock_minimo"
                        >
                    </div>

                    <!-- Select crea lista desplegable-->
                     <!--v-for recorre la lista de categorias, ,en nuestro caso categoriaStore.cat3egorias-->
                     <!--v-model="formulario.categoria_id"= queda fuardada en formulario.caregoria.id-->
                     <!-- {{ categoria.nombre }}= usuario ve en la lista-->
                    <div class="campo">
                        <label>Categoría *</label>

                        <select v-model="formulario.categoria_id">
                            <option value="">
                                Seleccionar categoría
                            </option>

                            <option
                                v-for="categoria in categoriasStore.categorias"
                                :key="categoria.id"
                                :value="categoria.id"
                            >
                                {{ categoria.nombre }}
                            </option>
                        </select>
                    </div>

                    <!--:value="proveedor.id"= nosoros vemos el nombre pero se guarda el ID-->
                    <div class="campo">
                        <label>Proveedor</label>

                        <select v-model="formulario.proveedor_id">
                            <option value="">
                                Sin proveedor
                            </option>

                            <option
                                v-for="proveedor in proveedoresStore.proveedores"
                                :key="proveedor.id"
                                :value="proveedor.id"
                            >
                                {{ proveedor.nombre }}
                            </option>
                        </select>
                    </div>

                    <div class="botones-formulario">

                        <button
                            type="submit"
                            class="btn-guardar"
                        >
                            {{ editando ? 'Modificar' : 'Guardar' }}
                        </button>

                        <button
                            type="button"
                            class="btn-cancelar"
                            @click="cancelarFormulario"
                        >
                            Cancelar
                        </button>

                    </div>
                </form>
                
            </div>


            <!--v-if="productosStore.productos.length === 0"= el array de productos tiene cero elemento?-->
            <!--si nohay elementos aparece "nohy libros registrdos'", si hay aparece tabla-->
            <div class="lista-libros">

                <h2>Libros registrados</h2>

                <p v-if="productosStore.productos.length === 0">
                    No hay libros registrados.
                </p>

                <table v-else>

                    <thead>
                        <tr>
                            <th>Nombre</th>
                            <th>Autor</th>
                            <th>Precio venta</th>
                            <th>Stock</th>
                            <th>Categoría</th>
                            <th>Proveedor</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>

                    <tbody>

                        <tr
                            v-for="producto in productosStore.productos"
                            :key="producto.id"
                        >
                            <td>{{ producto.nombre }}</td>
                            <td>{{ producto.autor }}</td>
                            <td>{{ producto.precio_venta }}</td>
                            <td>{{ producto.stock_actual }}</td>

                            <td>
                                {{ producto.categoria_id }}
                            </td>

                            <td>
                                {{ producto.proveedor_id || 'Sin proveedor' }}
                            </td>

                            <td>

                                <button
                                    @click="editarProducto(producto.id)"
                                >
                                    Editar
                                </button>

                                <button
                                    @click="eliminarProducto(producto.id)"
                                >
                                    Eliminar
                                </button>

                            </td>
                        </tr>

                    </tbody>

                </table>

            </div>

        </div>

    </div>
</template>

<script setup> //javaScript y logica dl componente Vue
import { ref, onMounted } from 'vue' //Traemmos funciones Vue q necesitamos usar eneste componente
                                    // ref = datos reactivos
                                    //onmounted se ejecuta cuqando el omponente ya fue montado en la pagina
// De Vue necesito ref para trabajar con datos reactivos y onMounted para ejecutar código cuando el 
// componente se monta.
import { useProductosStore } from '@/stores/productos' // Imortamos Store de productos
import { useCategoriasStore } from '@/stores/categorias'//Importa Store de cateorias creados con Pinia
import { useProveedoresStore } from '@/stores/proveedores'//Importa Store de cateorias creados con Pinia

const productosStore = useProductosStore()//Lo estamos ejecutando y guardando el Store resutante
//  en: productosStore--obtengo una instancia del Store par usarla en esta View
const categoriasStore = useCategoriasStore()
const proveedoresStore = useProveedoresStore()

//Los 3 son datos reqactivos porque usamos ref
const mostrarFormulario = ref(false)//Controla si form se muestra o no, comienza en false por eso no lo vemosm en pantalla
const editando = ref(false)// En q modo esta el formulario. false → estamos creando un libro
//true  → estamos editando un libro existente
const productoId = ref(null)
//Mostrando form? creandoo modif?, que producto modificamos?

const errores = ref([])// Errores=variable reactiva/ref[]= array vacio
const mensaje = ref('')// Mensaje = variable reactiva / '' = array vacío

const formulario = ref({//Objeto reactivo q contien datos del formulario
    nombre: '',
    autor: '',
    descripcion: '',
    precio_costo: '',
    precio_venta: '',
    stock_actual: 0,
    stock_minimo: 0,
    categoria_id: '',
    proveedor_id: ''
})

const cargarDatos = async () => {//cargar datos=funcion asyncrona q crga los datos necesarios par la vista
    await productosStore.getProductos() // espera a que el store obtenga los productos del backend
    await categoriasStore.getCategorias()
    await proveedoresStore.getProveedores()
}
//cargar datos= // Carga productos, categorías y proveedores necesarios para mostrar y completar la vista.

const limpiarFormulario = () => { // función que restablece el formulario a sus valores iniciales
    formulario.value = {// reemplaza el objeto formulario actual por uno nuevo
        nombre: '',
        autor: '',
        descripcion: '',
        precio_costo: '',
        precio_venta: '',
        stock_actual: 0,
        stock_minimo: 0,
        categoria_id: '',
        proveedor_id: ''
    }

    productoId.value = null  // elimina el ID del producto que se estaba editando
    editando.value = false  // vuelve al modo creación, no edición
    errores.value = [] // elimina todos los errores anteriores
}

const abrirFormulario = () => { // función que muestra el formulario para crear un libro
    limpiarFormulario() // limpia y restablece el formulario antes de abrirlo
    mostrarFormulario.value = true // hace visible el formulario
}

const cancelarFormulario = () => { // función que cancela y cierra el formulario
    limpiarFormulario()  // limpia y restablece los datos del formulario
    mostrarFormulario.value = false // oculta el formulario
}

const guardarProducto = async () => {  // función asíncrona que guarda o modifica un producto
    // funcion conectada con @submit.prevent="guardarProducto"
    errores.value = [] // ref q guarda los errores, limpia errores antriores
    mensaje.value = ''// ref q guarda valores,accedemos a su valor dentro del <sript setup>,
    //  '' array vacio

    const datos = {// cre un objeto de los datos q se van a enviar al backend, estamos preparando
        // los datos del formulario antes de mandrlos

        // Cada propiedad toma el valor correspondiente del formulario para enviarlo al backend
        nombre: formulario.value.nombre,
        autor: formulario.value.autor,
        descripcion: formulario.value.descripcion,
        precio_costo: formulario.value.precio_costo,
        precio_venta: formulario.value.precio_venta,
        stock_actual: formulario.value.stock_actual,
        stock_minimo: formulario.value.stock_minimo,
        categoria_id: formulario.value.categoria_id,
        proveedor_id: formulario.value.proveedor_id || null
        // Si hay proveedor envia su ID, si esta vacio envia null
    }

    try { // intenta ejecutar la opercion de guardado o modificacion, si funciona continua, sino catch
        if (editando.value) {// verificqa si estamos editando un producto existente
            const respuesta = await productosStore.actualizarProducto(// espera respuesta del store alactualizar producto
            //productoStore.actualizarProducto se omnunica con ProductoService
                productoId.value,//id q producto modificar/.value= los nuevos datos
                datos //objeto q armamos ant3riormente con los vlores del formulario(nombre,autor,etc)
            )// si editando es true= modif libro existente, si es false=noestamos editando, continua otro cilco

            mensaje.value = respuesta.message// tomamos mensaje q devuelve el backend y lo guardmos en nuesta variable reactiva "mesaje"
        } else { //ejecuta cuando editando.value es false
            const respuesta = await productosStore.crearProducto(datos)//llama al metodo del store para crear producto

            mensaje.value = respuesta.message//llega mensaje de eexito
        }

        //como acabamos de modificar o crear un libro necesitamos volver a cargar los datos del producto
        //para que la tabla muestre datos actualizados
        await productosStore.getProductos()// vuelve a pedir prod l backen y actualiz lista

        limpiarFormulario()// reestablece los datos y el estado del formulario(vacia campos,quita prodIDD,etc)
        mostrarFormulario.value = false //ocult el formulario despues de guardar
        // despues del guardadom correto, el formulario desaparece y nos queda visible la lista

    } catch (error) {// captura el error si dentro de la operacion el try falla
        if (error.response?.data?.errores) {// verifica si el backend devolvio lista de errores
            errores.value = error.response.data.errores//guarda en errores los errorre recibidos del backend
        } else if (error.response?.data?.message) {// si no hay una lista busca mensaje de error
            errores.value = [error.response.data.message]// convierte el mensqaje unico en un array
        } else { //si no errores ni8 mensajes  enn respuesta del backend mostramos mensaje generico
            errores.value = ['Ocurrió un error al guardar el libro']
        }
    }
}

const editarProducto = async (id) => {// funcion nasyncrona que obtiene productoID para editar
    errores.value = [] // ref q guarda los errores, limpia errores antriores
    mensaje.value = ''// ref q guarda valores,accedemos a su valor dentro del <sript setup>,
    //  '' array vacio

    try {
        const producto = await productosStore.getProducto(id) // obtiene del backend el prod q se quiere editar

        // Carga en el formulario los datos del producto seleccioado para editar
        formulario.value = {
            // los campos del formulario reciben el nombre ddel producto q obtuvimos del backen
            nombre: producto.nombre,
            autor: producto.autor,
            descripcion: producto.descripcion || '',//carga descripc o deja vacio si no eiste
            precio_costo: producto.precio_costo,
            precio_venta: producto.precio_venta,
            stock_actual: producto.stock_actual,
            stock_minimo: producto.stock_minimo,
            categoria_id: producto.categoria_id,
            proveedor_id: producto.proveedor_id || ''//carga ID de proveedor o deja vacio si no existe
        }

        productoId.value = id //guard ID del producto q se esta editando
        editando.value = true //cambia el formulario a modo edicion
        mostrarFormulario.value = true //muetra el formulario

    } catch (error) { // captura el error si dentro de la operacion el try falla en busqueda de producto
        errores.value = ['No se pudo cargar el libro']// guarda mensaje de error enel array
    }
}

const eliminarProducto = async (id) => {// funcion asyncrona q elimina un producto por su ID
    errores.value = [] // ref q guarda los errores, limpia errores antriores
    mensaje.value = '' // ref q guarda valores,accedemos a su valor dentro del <sript setup>,
    //  '' array vacio

    try { // intenta ejecutar la eliminacion
        const respuesta = await productosStore.eliminarProducto(id) // espera la respuesta del store
        //  para eliminar producto

        mensaje.value = respuesta.message // muestra mensaje de exito recibido del backend

        await productosStore.getProductos() // buelve a cargr los productos par actualizar tabla

    } catch (error) { // captura el error si falla la eliminacion
        if (error.response?.data?.message) { // veriica si backend devolvio mensaje de error
            errores.value = [error.response.data.message] //guarda el mensake en el array de errores
        } else { // si no hay mensaje especifico
            errores.value = ['No se pudo eliminar el libro']// se muestra error generico
        }
    }
}

// corresponde al ciclo de vida de Vue
// onmounted=hook de ciclo de vida de Vue
onMounted(async () => { // ejecuta el codigo cuando el componente ya fue montado
    await cargarDatos() // espera a que se cargen productos (get.productos()), categorias(get.cat3gorias())
    //  y proveedores((get.proveedores()))
})
// onmounted== ejecuta este codigo cuando el componente ya fue montado en pantalla
// onmounted determina cuando cargar datos
//"onMounted es un hook del ciclo de vida de Vue 3 que se ejecuta cuando el componente 
// ya fue montado. En esta vista lo utilizamos para llamar a cargarDatos() y obtener 
// automáticamente los productos, categorías y proveedores cuando entramos a la pantalla
//  de libros."
</script>