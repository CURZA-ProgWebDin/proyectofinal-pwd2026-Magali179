import { instance as axios } from "../plugins/axios";

class AuthService {
  auth_user = null;

  async login(user) {
    await axios
      .post("login", user)
      .then((response) => (this.auth_user = response.data))
      .catch((error) => console.error(error.status));
  }
  async register(new_user) {
    await axios
      .post("register", new_user)
      .then((response) => console.log(response.data))
      .catch((error) => console.error(error.status));
  }
}

export default AuthService;
