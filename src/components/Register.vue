<template>
  <section>
   
    <form @submit.prevent="submit">
    
        <h2><mdicon name="account-circle"/> Registro</h2>
      <div class="input">
        <label for="">usuario</label>
        <input type="text" v-model="user.username" placeholder="usuario" required />
      </div>
      <div class="input">
        <label for="">password</label>
        <input type="password" v-model="user.password" placeholder="password" required />
      </div>
      <div class="input">
        <label for="">email</label>
        <input type="email" v-model="user.email" placeholder="email" required />
      </div>

     <button type="submit">Registrarse</button>
    </form>
  
  </section>
</template>

<script setup>
import { reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";
import { storeToRefs } from "pinia";

const router = useRouter()
const { register } = useAuthStore();
const {  status_code} = storeToRefs(useAuthStore())
const user = reactive({
  username: "",
  password: "",
  email: "",
});

async function submit() {
  if (user.email && user.password && user.username) {

    await register(user);

    if (status_code.value === 201) {
      router.push({ name: "Login" });
    }

    if (status_code.value === 409) {
      alert("el usuario ya existe");
    }

  } else {
    alert("debe completar todos los campos");
  }
}
</script>

<style scoped>
section{
    position: relative;
}

.bg{
    position: absolute;
    top: 0;
    left: 0;
}
form{
    position: relative;
    margin: 0 auto;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(52, 50, 50, 0.5)    ;
    padding: 50px 20px;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    width: clamp(40%, 450px, 500px);

}

</style>
