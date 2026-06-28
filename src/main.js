import { createApp } from "vue";
import "./style.css";
import App from "./App.vue";
import { router } from "./routes";
import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import mdiVue from "mdi-vue/v3";
import * as mdijs from "@mdi/js";

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);
const app = createApp(App);

app.use(mdiVue, { icons: mdijs });
app.use(pinia);
app.use(router);

app.mount("#app");
