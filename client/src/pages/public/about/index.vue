<script>
export default {
  name: "index"
}
</script>

<template>
<!-- breadcrumb-area -->
  <section class="breadcrumb-area breadcrumb-bg">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="breadcrumb-content">
            <h2>Giới thiệu về chúng tôi</h2>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#"><router-link :to="{ name: 'public-homepage' }">Trang chủ</router-link></a></li>
                <li class="breadcrumb-item active" aria-current="page">Về chúng tôi</li>
              </ol>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- breadcrumb-area-end -->

  <!-- choose-area -->
  <section class="choose-area">
    <div class="container">
      <div class="row">
        <div class="col-lg-6">
          <div class="choose-wrap">
            <div class="section-title title-style-three mb-30">
              <h2 class="title">VÌ SAO NÊN CHỌN CHÚNG TÔI?</h2>
            </div>
            <div class="choose-content">
              <p>   ADARA tự hào là điểm đến lý tưởng cho những tín đồ thời trang đam mê hàng hiệu và phong cách đẳng cấp.
                Chúng tôi chuyên cung cấp các sản phẩm thời trang từ những thương hiệu danh tiếng trên toàn thế giới,
                mang đến cho bạn sự lựa chọn đa dạng và phong phú. Mỗi món đồ tại ADARA đều được tuyển chọn cẩn thận,
                đảm bảo chất lượng vượt trội và thiết kế tinh tế, từ những bộ trang phục hàng ngày đến những bộ sưu tập
                cao cấp dành cho các dịp đặc biệt.</p>
              <p>   Chúng tôi hiểu rằng thời trang không chỉ là vẻ bề ngoài, mà còn là cách để khẳng định phong cách và
                giá trị bản thân. Với sứ mệnh mang đến sự tự tin và sự sang trọng cho khách hàng, ADARA không ngừng cập
                nhật những xu hướng mới nhất từ các thương hiệu hàng đầu, giúp bạn luôn nổi bật và tỏa sáng.</p>
              <p>   Hãy đến với ADARA để trải nghiệm thế giới thời trang hàng hiệu, nơi phong cách và chất lượng luôn song
                hành cùng nhau.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="choose-bg"></div>
  </section>
  <!-- choose-area-end -->

  <!-- exclusive-services -->
  <section class="exclusive-services pt-100 pb-100">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-6 col-md-8">
          <div class="section-title text-center title-style-three mb-60">
            <span class="sub-title">Dịch vụ của chúng tôi</span>
            <h2 class="title">Dịch vụ hấp dẫn</h2>
          </div>
        </div>
      </div>
      <div class="row no-gutters justify-content-center">
        <div class="col-xl-3 col-lg-4 col-md-6 col-sm-8">
          <div class="ex-services-item text-center">
            <div class="content">
              <i class=""><font-awesome-icon :icon="['fas', 'headset']" /></i>
              <h5>Hỗ trợ 24/7</h5>
              <p>Cửa hàng có nhân viên trực 24/7 sẵn sàng giải đáp mọi thắc mắc của khách hàng.</p>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-4 col-md-6 col-sm-8">
          <div class="ex-services-item yellow text-center">
            <div class="overlay-bg" data-background="@/assets/img/images/ex_services_img.jpg"></div>
            <div class="content">
              <i class=""><font-awesome-icon :icon="['fas', 'shirt']" /></i>
              <h5>Đa dạng sản phẩm</h5>
              <p>Cửa hàng đa dạng mẫu mã sản phẩm đến từ nhiều thương hiệu khác nhau.</p>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-4 col-md-6 col-sm-8">
          <div class="ex-services-item text-center">
            <div class="content">
              <i class=""><font-awesome-icon :icon="['fas', 'crown']" /></i>
              <h5>Sản phẩm chính hãng</h5>
              <p>Sản phẩm của cửa hàng được nhập chính hãng từ thương hiệu.</p>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-4 col-md-6 col-sm-8">
          <div class="ex-services-item orange text-center">
            <div class="content">
              <i class=""><font-awesome-icon :icon="['fas', 'truck']" /></i>
              <h5>Vận chuyển hàng toàn quốc</h5>
              <p>Khách hàng trên mọi miền đất nước có thể đặt hàng thông qua trang web, cửa hàng sẽ vận chuyển hàng đến nơi của bạn.</p>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-4 col-md-6 col-sm-8">
          <div class="ex-services-item yellow text-center">
            <div class="content">
              <i class=""><font-awesome-icon :icon="['fas', 'truck-fast']" /></i>
              <h5>Vận chuyển hỏa tốc trong nội thành Hà Nội</h5>
              <p>Trong khu vực nội thành Hà Nội sản phẩm của quý khách có thể đến nơi trong ngày.</p>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-4 col-md-6 col-sm-8">
          <div class="ex-services-item text-center">
            <div class="content">
              <i class=""><font-awesome-icon :icon="['far', 'handshake']" /></i>
              <h5>1 năm bảo hành sản phẩm</h5>
              <p>Mọi sản phẩm mua từ cửa hàng đều được bảo hành 1 năm với những lỗi từ nhà sản xuất.</p>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-4 col-md-6 col-sm-8">
          <div class="ex-services-item orange text-center">
            <div class="content">
              <i class=""><font-awesome-icon :icon="['fas', 'money-bill-wave']" /></i><h5>Trả hàng, hoàn tiền trong 15 ngày</h5><p>Khách hàng nếu không ưng ý với sản phẩm có thể yêu cầu trả hàng trong vòng 15 ngày.</p>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-4 col-md-6 col-sm-8">
          <div class="ex-services-item text-center">
            <div class="content">
              <i class=""><font-awesome-icon :icon="['fas', 'user-check']" /></i>
              <h5>Nhân viên thân thiện</h5>
              <p>Cửa hàng luôn có đội ngũ nhân viên thân thiện sẵn sàng phục vụ quý khách.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- exclusive-services-end -->
</template>

<style scoped>
.breadcrumb-bg{
  background-image: url("@/assets/img/slider/third_slider_bg.jpg");
}
.choose-bg{
  background-image: url("@/assets/img/bg/10_big_brand.png");
}
</style>