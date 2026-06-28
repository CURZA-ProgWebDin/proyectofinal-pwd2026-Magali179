export const auth_routes = [
  {
    path: "/login",
    component: () => import("../views/LoginView.vue"),
    name: "Login",
    meta: {
      required_auth: false,
      orden: 101,
      menu: true,
    },
  },
  {
    path: "/register",
    component: () => import("../views/RegisterView.vue"),
    name: "Registrarse",
    meta: {
      required_auth: false,
      orden: 100,
      menu: true,
    },
  },
];
