import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "../stores/auth.js";
import { auth_routes } from "./auth_routes.js";
import { roles_routes } from "./roles_routes.js";
import { users_routes } from "./users_routes.js";
import { storeToRefs } from "pinia";

const routes = [
  {
    path: "/",
    component: () => import("../views/HomeView.vue"),
    name: "Home",
    meta: {
      rol_access: ["admin", "visitor", "editor", "superadmin"],
      required_auth: false,
      orden: -1,
      menu: true,
    },
  },
  {
    path: "/about",
    component: () => import("../views/AboutView.vue"),
    name: "About",
    meta: {
      rol_access: ["admin", "visitor", "editor", "superadmin"],
      required_auth: false,
      orden: 0,
      menu: true,
    },
  },
  {
    path: "/categorias",
    component: () => import("../views/CategoriasView.vue"),
    name: "Categorias",
    children: [
      {
        path: "/categorias/:id",
        component: () => import("../views/CategoriasView.vue"),
        name: "Categoria",
        children: [
          {
            path: "productos",
            name: "CategoriaProducto",
            component: () => import("../views/CategoriasView.vue"),
            meta: {
              rol_access: ["admin", "visitor", "editor", "superadmin"],
              required_auth: true,
              menu: false,
              orden: 1.1,
            },
          },
        ],
        meta: {
          rol_access: ["admin", "editor", "superadmin"],
          required_auth: true,
          orden: 1.01,
          menu: false,
        },
      },
    ],
    meta: {
      rol_access: ["admin", "editor", "superadmin"],
      required_auth: true,
      orden: 1,
      menu: true,
    },
  },

  ...auth_routes,
  ...roles_routes,
  ...users_routes,
];

export const router = createRouter({ history: createWebHistory(), routes });

router.beforeEach((to) => {
  const authStore = useAuthStore();

  if (
    to.meta.required_auth &&
    !authStore.is_authenticated &&
    to.name !== "Login"
  ) {
    return { name: "Login" };
  }

  if (
    to.meta.rol_access &&
    !to.meta.rol_access.includes(authStore.rol_user) &&
    to.name !== "Home"
  ) {
    return { name: "Home" };
  }
});
