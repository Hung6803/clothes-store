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
            <h2>Liên hệ</h2>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a><router-link :to="{ name: 'public-homepage' }">Trang chủ</router-link></a></li>
                <li class="breadcrumb-item active" aria-current="page">Liên hệ</li>
              </ol>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- breadcrumb-area-end -->

  <!-- contact-area -->
  <section class="contact-area pt-100 pb-100">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-8">
          <div class="contact-wrap">
            <div class="section-title title-style-three mb-30">
              <h2 class="title">Liên hệ ADARA</h2>
            </div>
            <form action="#" class="contact-form">
              <div class="row">
                <div class="col-md-6">
                  <span>Họ và tên</span>
                  <input type="text" placeholder="Họ và tên đầy đủ *">
                </div>
                <div class="col-md-6">
                  <span>Email</span>
                  <input type="email" placeholder="Địa chỉ email *">
                </div>
                <div class="col-md-6">
                  <span>Số điện thoại</span>
                  <input type="text" placeholder="Số điện thoại liên hệ *">
                </div>
                <div class="col-md-6">
                  <span>Vấn đề</span>
                  <input type="text" placeholder="Vấn đề bạn gặp phải">
                </div>
              </div>
              <span>Nội dung</span>
              <textarea name="message" placeholder="Nội dung gửi"></textarea>
              <button class="btn">Gửi đi</button>
            </form>
          </div>
        </div>
        <div class="col-lg-4 col-md-7">
          <aside class="contact-sidebar">
            <div class="widget">
              <div class="contact-sidebar-img mb-20">
                <img src="@/assets/img/images/contact_img.jpg" alt="">
              </div>
            </div>
            <div class="widget">
              <div class="contact-info-wrap">
                <ul>
                  <li>
                    <div class="icon"><font-awesome-icon :icon="['fas', 'phone-volume']" /></div>
                    <div class="content">
                      <h5>Số điện thoại</h5>
                      <p><a href="tel:0321654987">+84 963 835 703</a></p>
                    </div>
                  </li>
                  <li>
                    <div class="icon"><font-awesome-icon :icon="['fas', 'envelope-open-text']" /></div>
                    <div class="content">
                      <h5>Email</h5>
                      <p><a href="mailto:adara@info.com">hunghung6803@gmail.com</a></p>
                    </div></li>
                  <li>
                    <div class="icon"><font-awesome-icon :icon="['fas', 'location-dot']" /></div>
                    <div class="content">
                      <h5>Địa chỉ</h5>
                      <p>Số 59, đường Phan Đình Phùng<br>
                        Đan Phượng, Hà Nội</p>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </aside>
        </div>
      </div>
    </div>
  </section>
            <!-- contact-area-end -->

            <!-- contact-map -->
  <div id="contact-map"></div>
            <!-- contact-map-end -->
</template>

<style scoped>
.breadcrumb-bg {
  background-image: url('@/assets/img/slider/third_slider_bg.jpg');
}
</style>