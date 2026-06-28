<template>
  <section>
    <form @submit.prevent="submit">
      <h2><mdicon name="shield-account" /> Crear Rol</h2>
      <div class="input">
        <label>Nombre rol</label>
        <input type="text" v-model="rol.nombre" placeholder="Rol" required />
      </div>
      <div class="buttons">
        <button type="button" @click="router.push({ name: 'Roles' })">
          <mdicon name="arrow-left"></mdicon> Volver
        </button>
        <button type="submit" @click.prevent="submit">
          <mdicon name="plus"></mdicon> Crear
        </button>
      </div>
    </form>
  </section>
</template>

<script setup>
import { reactive, ref } from "vue";
import { useRolesStore } from "../stores/roles";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";

const router = useRouter();
const { crear } = useRolesStore();

const rol = ref({
  nombre: "",
});

function submit() {
  if (rol.value.nombre) {
    console.log(rol.value);
    crear(rol.value);
  } else {
    alert("debe completar todos los campos");
  }
}
</script>

<style scoped>
section {
  position: relative;
}
.buttons {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
  gap: 20px;
}

.bg {
  position: absolute;
  top: 0;
  left: 0;
}
form {
  position: relative;
  margin: 50px auto;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(52, 50, 50, 0.5);
  padding: 50px 20px;
  border-radius: 10px;
  backdrop-filter: blur(10px);
  width: clamp(40%, 450px, 500px);
}
</style>
