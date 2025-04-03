import {createRouter, createWebHistory} from "vue-router";
import admin from "./admin.js";
import login from "./login.js";
import client from "./public.js";

const  routes = [...admin, ...login, ...client]

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;