export const roles_routes = [
  {
    path: "/roles",
    name: "Roles",
    component: () => import("../views/RolesView.vue"),
    meta: {
      orden: 4,
      rol_access: ["admin", "editor", "superadmin"],
      required_auth: true,
      menu: true,
    },
  },
  {
    path: "/roles/create",
    name: "RolesCreate",
    component: () => import("../components/RolesCreate.vue"),
    meta: {
      orden: 4,
      rol_access: ["admin", "superadmin"],
      required_auth: true,
      menu: false,
    },
  },
];
