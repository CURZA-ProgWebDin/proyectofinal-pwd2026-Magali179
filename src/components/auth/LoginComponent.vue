<template>
  <section>
    <h1>ingreso</h1>
    <form @submit.prevent="submit">
      <div class="input">
        <label>nombre</label>
        <input type="text" v-model="user.nombre" />
      </div>
      <div class="input">
        <label>PASSWORD</label>
        <input type="password" v-model="user.password" />
      </div>

      <button @submit.prevent="submit">ingresar</button>
    </form>
  </section>
</template>
<script setup>
import { reactive } from "vue";
import { useAuthStore } from "../../stores/auth";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";

const router = useRouter();
const authStore = useAuthStore();
const { login } = authStore;
const { authenticated } = storeToRefs(authStore);
const user = reactive({
  nombre: "",
  password: "",
});

async function submit() {
  if (!user.password && !user.nombre) {
    alert("deben completar todos los campos");
  } else {
    await login(user);
    if (authenticated.value) {
      router.replace({ name: "Home" });
    } else {
      alert("acceso denegado, credenciales incorrectas");
    }
  }
}
</script>
<style scoped>
form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.input {
  display: flex;
  margin: 20px 10px;
  flex-direction: column;
  width: 50%;
}
</style>
