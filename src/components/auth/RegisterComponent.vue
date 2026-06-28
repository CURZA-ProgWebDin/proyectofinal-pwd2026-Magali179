<template>
  <section>
    <h1>Registro</h1>
    <form @submit.prevent="submit">
      <div class="input">
        <label>nombre</label>
        <input type="text" v-model="user.nombre" />
      </div>
      <div class="input">
        <label>EMAIL</label>
        <input type="email" v-model="user.email" />
      </div>
      <div class="input">
        <label>PASSWORD</label>
        <input type="password" v-model="user.password" />
      </div>

      <button @submit.prevent="submit">Registrar</button>
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
const { register } = authStore;
const { authenticated } = storeToRefs(authStore);
const user = reactive({
  nombre: "",
  password: "",
  email: "",
});

async function submit() {
  if (!user.password && !user.nombre && !user.email) {
    alert("deben completar todos los campos");
  } else {
    await register(user);
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
button {
  width: 50%;
  color: #fff;
  background-color: green;
  padding: 10px;
  border: none;
  border-radius: 8px;
}
</style>
