import { router } from "..";

export const routes = router
  .getRoutes()
  .filter((route) => route.meta && route.meta.menu)

  .sort((a, b) => a.meta.orden - b.meta.orden);
