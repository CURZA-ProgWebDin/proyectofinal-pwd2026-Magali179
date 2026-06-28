export const categorias_routes = [
  {
    path: "/categorias",
    component: () => import("../views/CategoriasView.vue"),
    name: "Categorias",
    children: [
      {
        path: "create",
        name: "CategoriasCreate",
      },
      {
        path: "",
        name: "CategoriasList",
        component: () => import("../components/CategoriasList.vue"),
        meta: {
          rol_access: ["admin", "editor", "superadmin"],
          required_auth: true,
          menu: false,
        },
      },
      {
        path: ":id",
        name: "CategoriaDetail",
        meta: {
          rol_access: ["admin", "editor", "superadmin"],
          required_auth: true,
          menu: false,
        },
        children: [
          {
            path: "productos",
            name: "CategoriasProductos",
            meta: {
              rol_access: ["admin", "editor", "superadmin"],
              required_auth: true,
              menu: false,
            },
          },
        ],
      },
    ],
    meta: {
      rol_access: ["admin", "editor", "superadmin"],
      required_auth: true,
      menu: true,
    },
  },
];
