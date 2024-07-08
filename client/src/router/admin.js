const admin = [
    {
        path: "/admin",
        component: () => import("../layouts/admin.vue"),
        children: [
            {
                path:"brand",
                name: "admin-brand",
                component: () => import("../pages/admin/brand/index.vue"),
            },
            {
                path:"brand/create",
                name: "admin-brand-create",
                component: () => import("../pages/admin/brand/create.vue"),
            },
            {
                path:"brand/:id/edit",
                name: "admin-brand-edit",
                component: () => import("../pages/admin/brand/edit.vue"),
            },
            {
                path:"category",
                name: "admin-category",
                component: () => import("../pages/admin/category/index.vue"),
            },
            {
                path:"category/create",
                name: "admin-category-create",
                component: () => import("../pages/admin/category/create.vue"),
            },
            {
                path:"category/:id/edit",
                name: "admin-category-edit",
                component: () => import("../pages/admin/category/edit.vue"),
            },
            {
                path:"size",
                name: "admin-size",
                component: () => import("../pages/admin/size/index.vue"),
            },
            {
                path:"size/create",
                name: "admin-size-create",
                component: () => import("../pages/admin/size/create.vue"),
            },
            {
                path:"size/:id/edit",
                name: "admin-size-edit",
                component: () => import("../pages/admin/size/edit.vue"),
            },
        ]
    }
]

export default admin;