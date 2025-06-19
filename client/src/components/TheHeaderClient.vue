<template>
  <div class="header-style-three">
    <div id="sticky-header" class="main-header menu-area">
      <div class="container custom-container-two">
        <div class="row">
          <div class="col-12">
            <div class="mobile-nav-toggler"><font-awesome-icon :icon="['fas', 'bars']" /></div>
            <div class="menu-wrap">
              <nav class="menu-nav show">
                <div class="logo">
                  <router-link :to="{ name: 'public-homepage' }"><img src="@/assets/img/logo/logo.png" alt="Logo"></router-link>
                </div>
                <div class="navbar-wrap main-menu d-none d-lg-flex">
                  <ul class="navigation">
                    <li>
                      <router-link :to="{ name: 'public-homepage'}" :class="{ active: store.page === 'A' }" @click="store.onSelectPage('A')">
                        Trang chủ
                      </router-link>
                    </li>
                    <li>
                      <router-link :to="{ name: 'public-shop'}" :class="{ active: store.page === 'B' }" @click="store.onSelectPage('B')">
                        Sản phẩm
                      </router-link>
                    </li>
                    <li >
                      <router-link :to="{ name: 'public-about-us'}" :class="{ active: store.page === 'C' }" @click="store.onSelectPage('C')">
                        Về chúng tôi
                      </router-link>
                    </li>
                    <li>
                      <router-link :to="{ name: 'public-contact'}" :class="{ active: store.page === 'D' }" @click="store.onSelectPage('D')">
                        Liên hệ
                      </router-link>
                    </li>
                  </ul>
                </div>
                <div class="header-action d-none d-md-block">
                  <ul>
                    <li v-if="token_login" class="header-profile" @mouseover="showProfile = true" @mouseleave="showProfile = false">
                      <router-link :to="{ name: 'public-account' }">
                        <font-awesome-icon :icon="['far', 'user']" />
                      </router-link>
                      <ul v-if="showProfile" class="miniprofile">
                        <li>
                          <router-link :to="{ name: 'public-account' }">Thông tin tài khoản</router-link>
                        </li>
                        <li>
                          <a href="#" @click.prevent="logout">Đăng xuất</a>
                        </li>
                      </ul>
                    </li>

                    <li v-else class="header-profile" @mouseover="showProfile = true" @mouseleave="showProfile = false">
                      <font-awesome-icon :icon="['far', 'user']" />
                      <ul v-if="showProfile" class="miniprofile">
                        <li>
                          <router-link :to="{ name: 'login' }">Đăng nhập</router-link>
                        </li>
                        <li>
                          <router-link :to="{ name: 'login-register' }">Đăng ký</router-link>
                        </li>
                      </ul>
                    </li>

                    <li class="header-shop-cart">
                      <router-link :to="{ name: 'public-cart'}">
                        <font-awesome-icon :icon="['fas', 'cart-shopping']" />
                        <span>{{cart.totalItems}}</span>
                      </router-link>
                      <ul class="minicart">
                        <li class="d-flex align-items-start" v-for="product in cart.selectedProducts" :key="product.id">
                          <div class="cart-img">
                            <a><router-link :to="{ name: 'public-shop-product', params: { id: product.id }}">
                              <img :src="`http://127.0.0.1:8000/image/${product.product_image}`" alt="">
                            </router-link></a>
                          </div>
                          <div class="cart-content">
                            <h4><a><router-link :to="{ name: 'public-shop-product', params: { id: product.id }}">
                              {{ product.product_name }}
                            </router-link></a></h4>
                            <div class="cart-price">
                              <span class="new" v-if="product.discount === 0">{{product.price}}.000 VND</span>
                              <span class="new" v-if="product.discount !== 0">
                                {{ product.price * (1 - product.discount / 100) }}.000 VND
                              </span>
                            </div>
                          </div>
                          <div class="del-icon">
                            <a @click.prevent="cart.removeProduct(product.id)">
                              <font-awesome-icon :icon="['fas', 'trash']" />
                            </a>
                          </div>
                        </li>
                        <li>
                          <div class="total-price">
                            <span class="f-left">Total:</span>
                            <span class="f-right">{{cart.totalPrice}}.000 VND</span>
                          </div>
                        </li>
                        <li>
                          <div class="checkout-link">
                            <router-link :to="{ name: 'public-cart'}">Giỏ hàng</router-link>
                            <router-link class="black-color" :to="{ name: 'public-order'}">Thanh toán</router-link>
                          </div>
                        </li>
                      </ul>
                    </li>
                  </ul>
                </div>
              </nav>
            </div>
            <!-- Mobile Menu  -->
            <div class="mobile-menu">
              <div class="close-btn"><font-awesome-icon :icon="['fas', 'xmark']" /></div>
              <nav class="menu-box">
                <div class="nav-logo">
                  <router-link :to="{ name: 'public-homepage' }">
                    <img src="@/assets/img/logo/logo.png" alt="" title="">
                  </router-link>
                </div>
                <div class="menu-outer">
                  <ul class="navigation">
                    <li :class="{ active: store.page === 'A' }" @click="store.onSelectPage('A')"><router-link :to="{ name: 'public-homepage' }">Trang chủ</router-link></li>
                    <li :class="{ active: store.page === 'B' }" @click="store.onSelectPage('B')"><router-link :to="{ name: 'public-shop' }">Sản phẩm</router-link></li>
                    <li :class="{ active: store.page === 'C' }" @click="store.onSelectPage('C')"><router-link :to="{ name: 'public-about-us' }">Về chúng tôi</router-link></li>
                    <li :class="{ active: store.page === 'D' }" @click="store.onSelectPage('D')"><router-link :to="{ name: 'public-contact' }">Liên hệ</router-link></li>
                  </ul>
                </div>
              </nav>
            </div>
            <div class="menu-backdrop"></div>
            <!-- End Mobile Menu -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.header-profile {
  position: relative;
  display: inline-block;
  cursor: pointer;
}

.miniprofile {
  display: block;
  position: absolute;
  top: 100%;
  right: 0;
  background: white;
  border: 1px solid #ddd;
  border-radius: 5px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  padding: 10px 0;
  min-width: 180px;
  z-index: 9;
  text-align: center;
}

.miniprofile li {
  list-style: none;
  padding: 10px 0;
  border-bottom: 1px solid #eee;
}

.miniprofile li:last-child {
  border-bottom: none;
}

.miniprofile a {
  text-decoration: none;
  color: #333;
  font-weight: 500;
  display: block;
  padding: 8px 0;
}

.miniprofile a:hover {
  color: #ff6600;
}

</style>

<script setup>
  import {ref, onMounted } from "vue";
  import { useHeader } from '@/store/use-header-client.js';
  import {useCartStore} from "@/store/use-cart-client.js";

  const cart = useCartStore();
  const store = useHeader();
  const brands = ref([]);
  const categories = ref([]);
  const showProfile = ref(false);
  const token_login = ref(false); // Giả lập đã đăng nhập, thay đổi theo logic thực tế

  const logout = () => {
    // Thực hiện đăng xuất
    token_login.value = true;
  };
  const getBrand = () => {
    axios.get('http://127.0.0.1:8000/brand/')
      .then(function (response) {
        brands.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const getCategory = () => {
    axios.get('http://127.0.0.1:8000/category/')
    .then(function (response) {
      categories.value = response.data;
    })
    .catch(function (error) {
      console.log(error);
    });
  };

  onMounted(() => {
    getCategory();
    getBrand();
  });

</script>