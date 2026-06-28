<template>
  <section>
    <form @submit.prevent="submit">
      <h2><mdicon name="login" /> Login</h2>
      <div class="input">
        <label>usuario</label>
        <input
          type="text"
          v-model="user.nombre"
          placeholder="usuario"
          required
        />
      </div>
      <div class="input">
        <label>password</label>
        <input
          type="password"
          v-model="user.password"
          placeholder="password"
          required
        />
      </div>

      <input type="submit" @click.prevent="submit" />
    </form>
  </section>
</template>

<script setup>
import { reactive, ref } from "vue";
import { useAuthStore } from "../stores/auth";
import { storeToRefs } from "pinia";
import { useRouter } from "vue-router";

const router = useRouter();
const { login } = useAuthStore();
const { is_authenticated } = storeToRefs(useAuthStore());
const user = reactive({
  nombre: "",
  password: "",
});

function submit() {
  if (user.password && user.nombre) {
    login(user);
    if (is_authenticated.value === true) {
      alert("Acceso correcto");
      router.push({ name: "Home" });
    } else {
      alert("Acceso denegado usuario o contraseña incorrectos");
    }
  } else {
    alert("debe completar todos los campos");
  }
}
</script>

<style scoped>
section {
  position: relative;
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
