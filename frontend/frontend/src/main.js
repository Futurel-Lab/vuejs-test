import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

// Install bootstrap first
import "bootstrap/dist/css/bootstrap.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

createApp(App).use(router).mount("#app");
