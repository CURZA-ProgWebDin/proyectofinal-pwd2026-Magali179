import { ref } from "vue";
import ApiService from "../services/ApiService";
import { defineStore } from "pinia";

export const useUserStore = defineStore("users", () => {
  const user = ref({});
  const users = ref([]);
  const loading = ref(false);
  const api_service = new ApiService("users");

  async function listar() {
    loading.value = true;
    const data = await api_service.getAll();
    if (data) {
      users.value = data;
    }
    loading.value = false;
  }
  async function buscarUno(id) {
    loading.value = true;
    const data = await api_service.findOne(id);
    if (data) {
      user.value = data;
    }
    loading.value = false;
  }
  async function crear(data) {
    await api_service.create(data);
  }
  async function modificar(data) {
    await api_service.update(data);
  }
  async function eliminar(id) {
    await api_service.destroy(id);
  }
  return { users, user, crear, eliminar, modificar, buscarUno, listar };
});
