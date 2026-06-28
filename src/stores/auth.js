import AuthServices from "../services/AuthService";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore(
  "auth",
  () => {
    const auth_user = ref(null);
    const is_authenticated = ref(false);
    const jwt = ref("");
    const rol_user = ref("");
    const service = new AuthServices();
    const errors = ref([]);
    const status_code = ref(null);

    async function login(user) {
      await service.login(user);

      if (service.auth_user) {
        auth_user.value = service.auth_user.nombre;
        jwt.value = service.auth_user.access_token;
        rol_user.value = service.auth_user.rol;
        is_authenticated.value = true;
      }

      if (service.errors.length > 0) {
        errors.value = service.errors;
      }
    }

    async function register(new_user) {
      const response = await service.register(new_user);

      if (response) {
        status_code.value = response;
      }
    }

    function logout() {
      auth_user.value = null;
      is_authenticated.value = false;
      jwt.value = "";
      rol_user.value = "";
      errors.value = [];
    }

    return {
      auth_user,
      is_authenticated,
      jwt,
      rol_user,
      errors,
      status_code,
      login,
      register,
      logout,
    };
  },
  { persist: true },
);
