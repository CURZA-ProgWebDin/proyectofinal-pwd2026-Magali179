import { instance as axios } from "../plugins/axios";

class AuthServices {
  auth_user = null;
  errors = [];

  async login(user) {
    await axios
      .post("login", user)
      .then((response) => {
        this.auth_user = response.data;
      })
      .catch((error) => {
        console.log("LOGIN ERROR:", error);

        if (error.response) {
          this.errors.push(error.response.data);
        } else {
          this.errors.push({
            message: "Error de conexión con el backend",
          });
        }
      });
  }

  async register(new_user) {
    const response = await axios
      .post("register", new_user)
      .then((response) => response.status)
      .catch((error) => {
        console.log("REGISTER ERROR:", error);

        if (error.response) {
          this.errors.push(error.response.data);
        } else {
          this.errors.push({
            message: "Error de conexión con el backend",
          });
        }
      });

    return response;
  }

  async resetPassword(user) {
    await axios
      .post("reset_password", user)
      .then((response) => console.log(response.data))
      .catch((error) => console.log(error));
  }
}

export default AuthServices;
