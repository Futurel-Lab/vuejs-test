import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// Install bootstrap first
import "bootstrap/dist/css/bootstrap.css";

createApp(App).use(router).mount("#app");
