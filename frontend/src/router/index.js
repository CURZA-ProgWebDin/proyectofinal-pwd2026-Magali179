import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  
  routes: [
    // Dirección inicial de la aplicación.
        // Cuando entramos a "/", vamos al formulario de login.
    {
            path: '/',
            redirect: '/login' //Si alguien entra a /, redirigilo a /login.
  },

    { path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
  },
  {
        path: '/inicio',
        name: 'inicio',
        component: () => import('../views/InicioView.vue'),
        meta: {
            requiresAuth: true
        },
    },
  {
      path: '/inicio',/*  Es la dirección que vamos a escribir en el navegador */
      name: 'inicio', /*Es el nombre que Vue Router le da a esta ruta.*/
      component: () => import('../views/InicioView.vue'), /*Cuando alguien entre a /inicio, cargá InicioView.vue.*/
  },
  {
    path: '/libros', /*Es la dirección que usamos en el navegador.*/
    name: 'libros', /*Es el nombre que le damos a esta ruta dentro de Vue Router.*/
    component: () => import('../views/LibroView.vue'), /*Esta línea establece qué componente se debe mostrar cuando entramos a /libros.*/
},
{
    path: '/usuarios', /*Es la dirección que vamos a usar en el navegador:*/
    name: 'usuarios', /*Es el nombre interno de esta ruta dentro de Vue Router.*/
    component: () => import('../views/UsuariosView.vue'), /*Le indicamos a Vue qué vista tiene que mostrar cuando entramos a /usuarios.*/
},

  ],
})
router.beforeEach((to) => { //Antes de cada navegación, revisá si se cumplen las condiciones.

    const authStore = useAuthStore()

    if (to.meta.requiresAuth && !authStore.is_authenticated) { //¿La ruta a la que quiero ir tiene requiresAuth: true?
      //Si la ruta requiere autenticación Y el usuario no está autenticado...entonces redirige al login
        return '/login'
    }
    if (to.name === 'login' && authStore.is_authenticated) {
        return '/inicio'
    }

})

export default router
