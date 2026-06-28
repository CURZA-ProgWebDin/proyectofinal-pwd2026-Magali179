<template>
  <main>
    <h2>LISTA DE PRODUCTOS</h2>
    <nav>
      <ul>
        <li><routerLink to="/productos/create">Crear Producto</routerLink></li>
        <li>
          <routerLink to="/productos">Lista de Productos</routerLink>
        </li>
        <RouterView />
      </ul>
    </nav>
  </main>
</template>

<script setup>
import ProductoList from "../components/ProductosList.vue";
import ProductoCreate from "../components/ProductoCreate.vue";
import { routeLocationKey } from "vue-router";
</script>

<style scoped></style>
