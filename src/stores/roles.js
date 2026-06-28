import ApiService from "../services/ApiService";
import { defineStore } from "pinia";
import { ref } from "vue";

export const useRolesStore = defineStore("roles", () => {
  const rol = ref({});
  const roles = ref([]);
  const loading = ref(false);
  const api_service = new ApiService("/roles/");

  async function listar() {
    loading.value = true;
    const data = await api_service.getAll();
    if (data) {
      roles.value = data;
    }
    loading.value = false;
  }
  async function buscarUno(id) {
    loading.value = true;
    const data = await api_service.findOne(id);
    if (data) {
      rol.value = data;
    }
    loading.value = false;
  }
  async function crear(data) {
    console.log("rol a crear", data.nombre);
    await api_service.create(data);
  }
  async function modificar(data) {
    await api_service.update(data);
  }
  async function eliminar(id) {
    await api_service.destroy(id);
  }
  return { roles, rol, crear, eliminar, modificar, buscarUno, listar };
});
