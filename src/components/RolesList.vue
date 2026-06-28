<template>
  <section>
    <h3><mdicon name="shield-account"></mdicon> Lista de Roles</h3>
    <RouterLink :to="{ name: 'RolesCreate' }"
      ><button><mdicon name="plus"></mdicon> Crear Rol</button></RouterLink
    >
    <template v-if="roles.length === 0">No roles found</template>

    <DataTable v-else :data="roles" :headers="['NOMBRE']" />
  </section>
</template>

<script setup>
import { useRolesStore } from "../stores/roles";
import { onMounted } from "vue";
import { storeToRefs } from "pinia";
import DataTable from "./DataTable.vue";

const store = useRolesStore();
const { roles } = storeToRefs(store);
onMounted(async () => {
  await store.listar();
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
