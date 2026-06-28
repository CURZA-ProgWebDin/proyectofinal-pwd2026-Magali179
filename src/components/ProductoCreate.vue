<template>
  <form @submit.prevent="crearProducto">
    <input type="text" placeholder="Nombre" />
    <input type="number" placeholder="Precio" />
    <input type="number" placeholder="Stock" />
    <button type="submit">Crear Producto</button>
  </form>
</template>
<script setup>
import { ref } from "vue";

const nombre = ref("");
const precio = ref(0);
const stock = ref(0);

function crearProducto() {
  // Lógica para crear el producto
}
</script>
<style scoped></style>
