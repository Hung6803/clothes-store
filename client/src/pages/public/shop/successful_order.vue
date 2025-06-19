<script>
export default {
  name: "success_order"
}
</script>

<template>
   <div class="success-container">
    <div class="success-icon"><font-awesome-icon :icon="['fas', 'circle-check']" /></div>
    <h1>Đặt hàng thành công!</h1>
    <p>Cảm ơn bạn đã mua hàng. Chúng tôi sẽ xử lý đơn hàng sớm nhất.</p>
    <div class="cart-coupon">
      <router-link :to="{ name: 'public-homepage'}"><a href="" class="btn">Về trang chủ</a></router-link>
    </div>
  </div>
</template>

<style scoped>
  .success-container {
    background-color: #ffffff;
    padding-bottom: 100px;
    text-align: center;
  }

  .success-container h1 {
    color: #ff5400;
    margin-bottom: 10px;
  }

  .success-container p {
    color: black;
    margin-bottom: 20px;
  }

  .success-icon {
    font-size: 50px;
    color: #ff5400;
    margin-bottom: 20px;
  }
</style>