<template>
  <nav>
    <ul>
      <li v-for="(link, index) in links" :key="index">
        <router-link
          v-if="!link.meta.rol_access && !is_authenticated"
          :to="link.path"
          >{{ link.name }}
        </router-link>
      </li>

      <li v-for="(link, index) in links" :key="index">
        <router-link
          v-if="
            link.meta.rol_access &&
            is_authenticated &&
            link.meta.rol_access.includes(rol_user)
          "
          :to="link.path"
          >{{ link.name }}
        </router-link>
      </li>
    </ul>
    <template v-if="is_authenticated">
      <button @click="cerrarSesion">
        <mdicon name="logout" />
      </button>
      <p><mdicon name="account-circle" /> {{ auth_user }}</p>
    </template>
  </nav>
</template>
<script setup>
import { useAuthStore } from "../stores/auth";
import { useRouter } from "vue-router";
import { storeToRefs } from "pinia";
import { computed } from "vue";
const authStore = useAuthStore();
const { is_authenticated, auth_user } = storeToRefs(authStore);

const props = defineProps({
  links: {
    type: Array,
    required: true,
  },
  rol_user: {
    type: String,
    required: true,
  },
});
const router = useRouter();
function cerrarSesion() {
  authStore.logout();
  router.push({ name: "Login" });
}
</script>
<style scoped>
nav {
  background-color: #0b7b8d;
  color: #fff;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 30px;
}
ul {
  margin: 0 auto;
  width: 75%;
  padding: 15px;
  display: flex;
  justify-self: center;
  align-items: center;
  background-color: #0b7b8d;
  list-style: none;
  li {
    margin: 10px;

    a {
      color: #fff;
      border-radius: 5px;
      text-decoration: none;

      font-size: 1rem;
    }
  }
}
.router-link-active {
  background-color: #0b7b8d;
}
button {
  background-color: transparent;
  border: none;
  color: #fff;
  cursor: pointer;
}
</style>
