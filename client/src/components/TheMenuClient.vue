<template>
  <div class="mobile-menu">
    <div class="close-btn"><i class="flaticon-targeting-cross"></i></div>
    <nav class="menu-box">
      <div class="nav-logo"><a href="index.html"><img src="" alt="" title=""></a>
      </div>
      <div class="menu-outer">
        <ul class="navigation">
          <li class="active menu-item-has-children"><a href="#">Home</a></li>
          <li class="menu-item-has-children"><a href="#">Sản phẩm</a></li>
          <li><a href="#">Về chúng tôi</a></li>
          <li><a href="#">Liên hệ</a></li>
        </ul>
      </div>
      <div class="social-links">
        <ul class="clearfix">
            <li><a href="#"><span class="fab fa-twitter"></span></a></li>
            <li><a href="#"><span class="fab fa-facebook-square"></span></a></li>
            <li><a href="#"><span class="fab fa-pinterest-p"></span></a></li>
            <li><a href="#"><span class="fab fa-instagram"></span></a></li>
            <li><a href="#"><span class="fab fa-youtube"></span></a></li>
        </ul>
      </div>
    </nav>
</div>
<div class="menu-backdrop"></div>
</template>

<script>
import {UserOutlined, ShoppingOutlined, SkinOutlined} from "@ant-design/icons-vue"
import { defineComponent } from 'vue';
import {storeToRefs} from "pinia";
import {useMenu} from "@/store/use-menu-admin.js";

export default defineComponent({
  components: {
    UserOutlined,
    ShoppingOutlined,
    SkinOutlined
  },
  setup() {
    const store = useMenu();

    return {
      ...storeToRefs(store)
    };
  },
});
</script>

<style scoped>
.menu{
  width: 100%;
}
</style>