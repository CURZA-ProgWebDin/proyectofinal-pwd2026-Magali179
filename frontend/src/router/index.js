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

  ],
})

export default router
