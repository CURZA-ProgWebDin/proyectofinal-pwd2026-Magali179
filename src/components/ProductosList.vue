<template>
  <section>
    <template v-if="listProductos.length === 0"> <p>cargando...</p> </template>
    <template v-else>
      <h3 v-if="listProductos.length === 0">SIN DATOS</h3>
      <DataTable
        v-else
        :headers="[
          'ID',
          'NOMBRE',
          'PRECIO',
          'STOCK',
          'ACTIVO',
          'CATEGORIA',
          'ACCIONES',
        ]"
        :data="listProductos"
        @editar="edita"
        @eliminar="elimina"
      />
    </template>
  </section>
</template>
<script setup>
import { productos } from "../service/productos.js";
import DataTable from "./DataTable.vue";
import { categoriasProductos } from "../service/categorias.js";
import { onMounted, ref } from "vue";
const listProductos = ref([]);

onMounted(() => {
  setTimeout(() => {
    listProductos.value = productos;
    listProductos.value = listProductos.value.map((prod) => {
      const categoria = categoriasProductos.find(
        (cat) => cat.id === prod.categoria_id,
      );
      return {
        ...prod,
        categoria: categoria ? categoria.nombre : "SIN CATEGORIA",
      };
    });
  }, 1000);
});
function elimina(id) {
  console.log(id);
}
function edita(id) {
  console.log(id);
}
</script>
<style scoped></style>
