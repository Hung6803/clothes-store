<script setup>
  import TheProduct from "@/components/TheProduct.vue";
  import {ref} from "vue";

  const products = ref([]);

  const activeButton = ref(null);

  const handleClick = (buttonName) => {
    activeButton.value = buttonName;
    if (buttonName === 'A') {
      axios.get(`http://127.0.0.1:8000/product/top/8`)
      .then(function (response) {
        products.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      })
    } else if (buttonName === 'B') {
      axios.get(`http://127.0.0.1:8000/product/discount/8`)
      .then(function (response) {
        products.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      })
    }
  };

  handleClick('A');

</script>

<template>
  <main>
    <section class="slider-area position-relative">
      <div class="third-slider-active">
        <div class="third-slider-item third-slider-bg">
          <div class="container custom-container-two">
            <div class="third-slider-wrap">
              <div class="row align-items-center">
                <div class="col-lg-6">
                  <div class="slider-content">
                    <h3 class="sub-title" data-animation-in="fadeInUp" data-delay-in=".2" data-duration-in="1.5">Sản phẩm chất lương !</h3>
                    <h2 class="title" data-animation-in="fadeInUp" data-delay-in=".4" data-duration-in="1.5">Mẫu mã đa dạng</h2>
                    <p data-animation-in="fadeInUp" data-delay-in=".6" data-duration-in="1.5">Giảm giá lên đến 50%</p>
                    <router-link :to="{ name: 'public-shop' }" class="btn" data-animation-in="fadeInUp" data-delay-in=".8" data-duration-in="1.5">Mua ngay</router-link>
                  </div>
                </div>
                <div class="col-lg-6">
                  <div class="third-slider-img">
                    <div class="img-shape" data-animation-in="zoomIn"
                         data-delay-in="1" data-duration-in="1.5"></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- slider-area-end -->

    <!-- new-arrival-area -->
    <section class="new-arrival-area pt-95 pb-45">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-xl-4 col-lg-6">
            <div class="section-title title-style-two text-center mb-45">
              <h3 class="title">Bộ sưu tập</h3>
            </div>
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-lg-6">
            <div class="new-arrival-nav mb-35">
              <button @click="handleClick('A')" :class="{ active: activeButton === 'A' }">Sản phẩm bán chạy</button>
              <button @click="handleClick('B')" :class="{ active: activeButton === 'B' }">Sản phẩm giảm giá</button>
            </div>
          </div>
        </div>
        <div class="row new-arrival-active">
          <div class="col-xl-3 col-lg-4 col-sm-6 grid-item grid-sizer cat-two" v-for="(product, index) in products">
            <TheProduct :key="index" :product="product"/>
          </div>
        </div>
      </div>
    </section>
    <!-- new-arrival-area-end -->

    <!-- promo-services -->
    <section class="promo-services pt-70 pb-25">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-3 col-md-6 col-sm-8">
            <div class="promo-services-item mb-40">
              <div class="icon"><img src="@/assets/img/icon/promo_icon01.png" alt=""></div>
              <div class="content">
                <h6>thanh toán & giao hàng</h6>
                <p>Giao hàng trên toàn quốc</p>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-8">
            <div class="promo-services-item mb-40">
              <div class="icon"><img src="@/assets/img/icon/promo_icon02.png" alt=""></div>
              <div class="content">
                <h6>Hoàn trả sản phẩm</h6>
                <p>Nhận hoàn trả sản phẩm</p>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-8">
            <div class="promo-services-item mb-40">
              <div class="icon"><img src="@/assets/img/icon/promo_icon03.png" alt=""></div>
              <div class="content">
                <h6>Chính sách hoàn tiền</h6>
                <p>Hoàn tiền trong 24h sau khi nhận hàng</p>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 col-sm-8">
            <div class="promo-services-item mb-40">
              <div class="icon"><img src="@/assets/img/icon/promo_icon04.png" alt=""></div>
              <div class="content">
                <h6>Hỗ trợ chất lượng</h6>
                <p>Nhân viên tư vấn thường trực 24/7</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- promo-services-end -->
  </main>
</template>

<style scoped>
.third-slider-bg {
  background-image: url('@/assets/img/slider/third_slider_bg.jpg');
}
.img-shape{
  background-image: url('@/assets/img/slider/third_slide_shape.png');
}
</style>