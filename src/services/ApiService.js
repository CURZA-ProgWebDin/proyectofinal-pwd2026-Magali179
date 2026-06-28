import { instance as axios } from "../plugins/axios";

class ApiService {
  url = "";
  errors = [];

  constructor(url) {
    this.url = url;
  }
  async getAll() {
    const data = await axios
      .get(this.url)
      .then((response) => response.data)
      .catch((error) => this.errors.push(error.response.data));
    if (this.errors.length === 0) {
      return data;
    } else {
      alert("error al listar");
    }
  }
  async findOne(id) {
    const data = (await axios.get(`${this.url}/${id}`))
      .then((response) => response.data)
      .catch((error) => this.errors.push(error.response.data));
    if (this.errors.length === 0) {
      return data;
    }
  }
  async create(data) {
    await axios
      .post(this.url, data)
      .then((response) => alert(response.data.message))
      .catch((error) =>
        error.code === "ERR_NETWORK"
          ? alert("Error de red")
          : error.response.data,
      );
  }
  async update(data) {
    await axios
      .put(this.url, data)
      .then((response) => alert(response.data.message))
      .catch((error) =>
        error.code === "ERR_NETWORK"
          ? alert("Error de red")
          : error.response.data,
      );
  }
  async destroy(id) {
    await axios
      .delete(`${this.url}/${id}`)
      .then((response) => alert(response.data.message))
      .catch((error) =>
        error.code === "ERR_NETWORK"
          ? alert("Error de red")
          : error.response.data,
      );
  }
}

export default ApiService;
