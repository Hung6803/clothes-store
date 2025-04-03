<template>

  <TheHeader/>

  <div class="container-fluid mt-3">
    <router-view></router-view>
  </div>
  <TheFooterClient/>
  <TheScrollTop/>
</template>

<script>
  import TheHeader from "../components/TheHeaderClient.vue";
  import TheMenu from "../components/TheMenuClient.vue";
  import TheScrollTop from "@/components/TheScrollTop.vue";
  import TheFooterClient from "@/components/TheFooterClient.vue";
  export default {
    mounted() {
      const scripts = ['./assets/js/popper.min.js', './assets/js/vendor/jquery-3.5.0.min.js',
                      './assets/js/isotope.pkgd.min.js', './assets/js/imagesloaded.pkgd.min.js',
                      './assets/js/jquery.magnific-popup.min.js', './assets/js/jquery.mCustomScrollbar.concat.min.js',
                      './assets/js/bootstrap-datepicker.min.js', './assets/js/jquery.nice-select.min.js',
                      './assets/js/jquery.countdown.min.js', './assets/js/swiper-bundle.min.js',
                      './assets/js/jarallax.min.js', './assets/js/slick.min.js',
                      './assets/js/wow.min.js', './assets/js/nav-tool.js',
                      './assets/js/plugins.js', './assets/js/main.js'];
      scripts.forEach(src => {
        const script = document.createElement('script');
        script.src = src;
        script.async = false;
        document.body.appendChild(script);
      });
    },
    components: {
      TheFooterClient,
      TheScrollTop,
      TheHeader,
      TheMenu
    }
  }
</script>
