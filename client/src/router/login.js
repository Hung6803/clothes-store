const login = [
    {
        path: "/login",
        component: () => import("../layouts/login.vue"),
        children: [
            {
                path:"",
                name: "login",
                component: () => import("../pages/login/index.vue"),
            },
            {
                path:"register",
                name: "login-register",
                component: () => import("../pages/login/register.vue"),
            },
        ]
    }
]

export default login;