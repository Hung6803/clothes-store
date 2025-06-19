const client = [
    {
        path: "/",
        component: () => import("../layouts/public.vue"),
        children: [
            {
                path:"",
                name: "public-homepage",
                component: () => import("../pages/public/home/index.vue"),
            },
            {
                path:"test",
                name: "public-test",
                component: () => import("../pages/public/home/test.vue"),
            },
            {
                path:"about",
                name: "public-about-us",
                component: () => import("../pages/public/about/index.vue"),
            },
            {
                path:"contact",
                name: "public-contact",
                component: () => import("../pages/public/contact/index.vue"),
            },
            {
                path:"account",
                name: "public-account",
                component: () => import("../pages/public/account/index.vue"),
            },
            {
                path:"account/edit",
                name: "public-account-edit",
                component: () => import("../pages/public/account/edit.vue"),
            },
            {
                path:"shop",
                name: "public-shop",
                component: () => import("../pages/public/shop/index.vue"),
            },
            {
                path:"shop/product/:id",
                name: "public-shop-product",
                component: () => import("../pages/public/shop/product_detail.vue"),
            },
            {
                path:"cart",
                name: "public-cart",
                component: () => import("../pages/public/shop/shopping_cart.vue"),
            },
            {
                path:"order",
                name: "public-order",
                component: () => import("../pages/public/shop/order.vue"),
            },
            {
                path:"success",
                name: "public-successful_order",
                component: () => import("../pages/public/shop/successful_order.vue"),
            },
        ]
    }

]
export default client;
