import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue'),
  },
  {
      ath: '/inicio',/*  Es la dirección que vamos a escribir en el navegador */
      name: 'inicio', /*Es el nombre que Vue Router le da a esta ruta.*/
      component: () => import('../views/InicioView.vue'), /*Cuando alguien entre a /inicio, cargá InicioView.vue.*/
  },
  {
    path: '/libros', /*Es la dirección que usamos en el navegador.*/
    name: 'libros', /*Es el nombre que le damos a esta ruta dentro de Vue Router.*/
    component: () => import('../views/LibroView.vue'), /*Esta línea establece qué componente se debe mostrar cuando entramos a /libros.*/
},

  ],
})

export default router
