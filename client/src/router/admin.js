const admin = [
    {
        path: "/admin",
        component: () => import("../layouts/admin.vue"),
        meta: { requiresAdmin: true },
        children: [
            {
                path:"invoice/new",
                name: "admin-invoice-new",
                component: () => import("../pages/admin/invoice/new.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"invoice",
                name: "admin-invoice",
                component: () => import("../pages/admin/invoice/index.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"employee",
                name: "admin-employee",
                component: () => import("../pages/admin/employee/index.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"employee/create",
                name: "admin-employee-create",
                component: () => import("../pages/admin/employee/create.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"employee/:id/edit",
                name: "admin-employee-edit",
                component: () => import("../pages/admin/employee/edit.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"customer",
                name: "admin-customer",
                component: () => import("../pages/admin/customer/index.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"customer/create",
                name: "admin-customer-create",
                component: () => import("../pages/admin/customer/create.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"customer/:id/edit",
                name: "admin-customer-edit",
                component: () => import("../pages/admin/customer/edit.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"inventory",
                name: "admin-inventory",
                component: () => import("../pages/admin/inventory/index.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"inventory/create",
                name: "admin-inventory-create",
                component: () => import("../pages/admin/inventory/create.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"inventory/:product_id/:size_id/edit",
                name: "admin-inventory-edit",
                component: () => import("../pages/admin/inventory/edit.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"product",
                name: "admin-product",
                component: () => import("../pages/admin/product/index.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"product/create",
                name: "admin-product-create",
                component: () => import("../pages/admin/product/create.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"product/:id/edit",
                name: "admin-product-edit",
                component: () => import("../pages/admin/product/edit.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"brand",
                name: "admin-brand",
                component: () => import("../pages/admin/brand/index.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"brand/create",
                name: "admin-brand-create",
                component: () => import("../pages/admin/brand/create.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"brand/:id/edit",
                name: "admin-brand-edit",
                component: () => import("../pages/admin/brand/edit.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"category",
                name: "admin-category",
                component: () => import("../pages/admin/category/index.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"category/create",
                name: "admin-category-create",
                component: () => import("../pages/admin/category/create.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"category/:id/edit",
                name: "admin-category-edit",
                component: () => import("../pages/admin/category/edit.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"size",
                name: "admin-size",
                component: () => import("../pages/admin/size/index.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"size/create",
                name: "admin-size-create",
                component: () => import("../pages/admin/size/create.vue"),
                meta: { requiresAdmin: true }
            },
            {
                path:"size/:id/edit",
                name: "admin-size-edit",
                component: () => import("../pages/admin/size/edit.vue"),
                meta: { requiresAdmin: true }
            },
        ]
    }
]

export default admin;