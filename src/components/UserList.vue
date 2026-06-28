<template>
  <section>
    <h3><mdicon name="account"></mdicon> Lista de Usuarios</h3>

    <RouterLink to="/"
      ><button>
        <mdicon name="account-plus"></mdicon> Crear usuario
      </button></RouterLink
    >

    <template v-if="list_users.length === 0">No users found</template>

    <DataTable
      v-else
      :data="list_users"
      :headers="['ID', 'NOMBRE', 'EMAIL', 'ACTIVO']"
    />
  </section>
</template>
<script setup>
import { onMounted, ref, computed } from "vue";
import { useUserStore } from "../stores/users";
import { storeToRefs } from "pinia";
import DataTable from "./DataTable.vue";
import { mdiCone } from "@mdi/js";
const userStore = useUserStore();
const { listar, eliminar } = userStore;

const { users } = storeToRefs(userStore);
const list_users = computed(() => {
  if (users.value.length === 0) {
    return [];
  }
  return users.value.map((user) => {
    return {
      id: user.id,
      nombre: user.nombre,
      email: user.email,
      activo: user.activo ? "activo" : "inactivo",
    };
  });
});
onMounted(() => {
  listar();
});
</script>
<style scoped>
button {
  margin: 1rem 0;
  padding: 0.5rem 1rem;
  background-color: #4caf50;
  color: white;
  border: none;
  text-decoration: none;
  border-radius: 5px;
  cursor: pointer;
  text-align: center;
  display: inline-block;
  font-size: 16px;
}
</style>
