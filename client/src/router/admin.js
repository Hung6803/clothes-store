const admin = [
    {
        path: "/admin",
        component: () => import("../layouts/admin.vue"),
        children: [
            {
                path:"invoice/new",
                name: "admin-invoice-new",
                component: () => import("../pages/admin/invoice/new.vue"),
            },
            {
                path:"invoice",
                name: "admin-invoice",
                component: () => import("../pages/admin/invoice/index.vue"),
            },
            {
                path:"employee",
                name: "admin-employee",
                component: () => import("../pages/admin/employee/index.vue"),
            },
            {
                path:"employee/create",
                name: "admin-employee-create",
                component: () => import("../pages/admin/employee/create.vue"),
            },
            {
                path:"employee/:id/edit",
                name: "admin-employee-edit",
                component: () => import("../pages/admin/employee/edit.vue"),
            },
            {
                path:"customer",
                name: "admin-customer",
                component: () => import("../pages/admin/customer/index.vue"),
            },
            {
                path:"customer/create",
                name: "admin-customer-create",
                component: () => import("../pages/admin/customer/create.vue"),
            },
            {
                path:"customer/:id/edit",
                name: "admin-customer-edit",
                component: () => import("../pages/admin/customer/edit.vue"),
            },
            {
                path:"inventory",
                name: "admin-inventory",
                component: () => import("../pages/admin/inventory/index.vue"),
            },
            {
                path:"inventory/create",
                name: "admin-inventory-create",
                component: () => import("../pages/admin/inventory/create.vue"),
            },
            {
                path:"inventory/:product_id/:size_id/edit",
                name: "admin-inventory-edit",
                component: () => import("../pages/admin/inventory/edit.vue"),
            },
            {
                path:"product",
                name: "admin-product",
                component: () => import("../pages/admin/product/index.vue"),
            },
            {
                path:"product/create",
                name: "admin-product-create",
                component: () => import("../pages/admin/product/create.vue"),
            },
            {
                path:"product/:id/edit",
                name: "admin-product-edit",
                component: () => import("../pages/admin/product/edit.vue"),
            },
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