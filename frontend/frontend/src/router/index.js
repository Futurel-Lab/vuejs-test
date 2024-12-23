import { createRouter, createWebHistory } from "vue-router";
import Shark from "../components/Shark.vue";
import GamesLibrary from "../components/GamesLibrary.vue";
import HomePage from "../components/HomePage.vue";

const routes = [
  {
    path: "/shark",
    name: "Shark",
    component: Shark,
  },
  {
    path: "/games",
    name: "Games",
    component: GamesLibrary,
  },
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
