import {createRouter, createWebHistory} from "vue-router";
import admin from "./admin.js";
import login from "./login.js";
import client from "./public.js";

const  routes = [...admin, ...login, ...client]

const router = createRouter({
    history: createWebHistory(),
    routes
});

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("token");
  const role = localStorage.getItem("role");

  if (to.meta.requiresAdmin && role === "True") {
    return next("/");
  }

  next();
});

export default router;