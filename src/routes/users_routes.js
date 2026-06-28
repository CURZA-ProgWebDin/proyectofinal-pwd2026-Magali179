export const users_routes = [
  {
    path: "/users",
    name: "Usuarios",
    component: () => import("../views/UsersView.vue"),
    meta: {
      orden: 9,
      rol_access: ["admin", "editor", "superadmin"],
      required_auth: true,
      menu: true,
    },
  },
];
