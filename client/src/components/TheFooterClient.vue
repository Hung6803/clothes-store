<script>
export default {
  name: "TheFooterClient"
}
</script>

<template>
  <!-- footer-area -->
  <footer class="dark-bg pt-55 pb-80">
    <div class="container">
      <div class="footer-top-wrap">
        <div class="row">
          <div class="col-12">
            <div class="footer-logo">
              <router-link :to="{ name: 'public-homepage' }"><img src="@/assets/img/logo/w_logo.png" alt=""></router-link>
            </div>
          </div>
        </div>
      </div>
      <div class="footer-middle-wrap">
        <div class="row">
          <div class="col-12">
            <div class="footer-link-wrap">
              <nav class="menu-links">
                <ul>
                  <li><router-link :to="{ name: 'public-about-us' }">Về chúng tôi</router-link></li>
                  <li><router-link :to="{ name: 'public-shop' }">Sản phẩm</router-link></li>
                  <li><router-link :to="{ name: 'public-contact' }">Địa chỉ</router-link></li>
                  <li><router-link :to="{ name: 'public-contact' }">Liên hệ</router-link></li>
                  <li><router-link :to="{ name: 'public-contact' }">Hỗ trợ</router-link></li>
                </ul>
              </nav>
              <div class="footer-social">
                <ul>
                  <li><a href="#"><font-awesome-icon :icon="['fab', 'facebook-f']" /></a></li>
                  <li><a href="#"><font-awesome-icon :icon="['fab', 'instagram']" /></a></li>
                  <li><a href="#"><font-awesome-icon :icon="['fab', 'github']" /></a></li>
                  <li><a href="#"><font-awesome-icon :icon="['fab', 'google']" /></a></li>
                  <li><a href="#"><font-awesome-icon :icon="['fab', 'tiktok']" /></a></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="copyright-wrap">
        <div class="row align-items-center">
          <div class="col-lg-6">
            <div class="copyright-text">
              <p>&copy; 2024 <router-link :to="{ name: 'public-homepage' }">adara</router-link>. All Rights Reserved | Phone (+84) 963 835 703</p>
            </div>
          </div>
          <div class="col-lg-6">
            <div class="pay-method-img">
              <img src="@/assets/img/images/payment_method_img.png" alt="">
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>
  <!-- footer-area-end -->
</template>

<style scoped>

</style>