<script setup>
import { useRoute } from "vue-router";
import MenuNav from "./components/MenuNav.vue";
import { routes } from "./routes/configs/navegation";
import { useAuthStore } from "./stores/auth";

const route = useRoute();

const { rol_user, authenticated } = useAuthStore();
</script>

<template>
  <menu-nav
    :links="routes"
    :rol_user="rol_user"
    :authenticated="authenticated"
  />
  <router-view v-slot="{ Component }">
    <transition name="fade" mode="out-in">
      <component :is="Component" />
    </transition>
  </router-view>
</template>

<style scoped>
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
.fade-enter-active,
.fade-leave-active {
  transition: 0.5s all ease-in-out;
}

nav,
ul {
  display: flex;
}
ul {
  list-style: none;
  li {
    margin: 20px;

    a {
      color: #fff;
      border-radius: 5px;
      text-decoration: none;
      padding: 10px 20px;
    }
  }
}
.router-link-active {
  background-color: #0b7b8d;
}
</style>
