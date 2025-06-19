<script setup>
  import {useCartStore} from "@/store/use-cart-client.js";
  import {ref} from "vue";

  const products = useCartStore();
  const product_sizes = ref([]);
  const getSizesForProducts = () => {
    for (let i = 0; i < products.selectedProducts.length; i++) {
      axios.get (`http://127.0.0.1:8000/inventory/${products.selectedProducts[i].id}`)
      .then(function (response) {
        product_sizes.value[i] = response.data.sizes;
      })
      .catch(function (error) {
        console.log(error);
      });
    }
  };

  const handleSizeChange = (product, newSizeId) => {
    const oldSizeId = product.size_id

    if (newSizeId === oldSizeId) return

    // Gọi hàm updateSize trong store
    products.updateSize(product.id, oldSizeId, newSizeId)
  }

  getSizesForProducts();
</script>

<template>
  <main>
    <!-- breadcrumb-area -->
    <section class="breadcrumb-area breadcrumb-bg">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="breadcrumb-content">
              <h2>Giỏ hàng</h2>
              <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item"><a><router-link :to="{ name: 'public-homepage' }">Trang chủ</router-link></a></li>
                  <li class="breadcrumb-item active" aria-current="page">Giỏ hàng</li>
                </ol>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- breadcrumb-area-end -->
    <div class="cart-area pt-100 pb-100">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="cart-wrapper">
              <div class="table-responsive">
                <table class="table mb-0">
                  <thead>
                    <tr>
                      <th class="product-thumbnail"></th>
                      <th class="product-name">Sản phẩm</th>
                      <th class="product-price">Giá</th>
                      <th class="product-size">Size</th>
                      <th class="product-quantity">Số lượng</th>
                      <th class="product-subtotal">Đơn giá</th>
                      <th class="product-delete"></th>
                    </tr>
                  </thead>
                  <tbody v-for="(product, index) in products.selectedProducts" :key="product.id">
                    <tr>
                      <td class="product-thumbnail">
                        <a><router-link :to="{ name: 'public-shop-product',  params: { id: product.id }}">
                          <img :src="`http://127.0.0.1:8000/image/${product.product_image}`" alt="">
                        </router-link></a>
                      </td>
                      <td class="product-name">
                        <h4><a><router-link :to="{ name: 'public-shop-product',  params: { id: product.id }}">
                          {{ product.product_name }}
                        </router-link></a></h4>
                      </td>
                      <td class="product-price" v-if="product.discount === 0">{{product.price}}.000 VND</td>
                      <td class="product-price" v-else>{{product.price/100*product.discount}}.000 VND</td>
                      <th class="product-quantity">
                        <a-select
                          ref="select"
                          class="custom-select-style"
                          :value="product.size_id"
                          placeholder="Size"
                          :options="product_sizes[index]"
                          :field-names="{label: 'size_name', value: 'id'}"
                          @change="(newSizeId) => handleSizeChange(product, newSizeId)"
                        ></a-select>
                      </th>
                      <td class="product-quantity">
                        <div class="cart-plus-minus">
                          <form action="#" class="num-block">
                            <input type="text" class="in-num" :value="product.quantity" readonly="">
                            <div class="qtybutton-box">
                              <span class="plus" @click.prevent="products.updateQuantity(product.id, product.size_id, product.quantity+1)">
                                <img src="@/assets/img/icon/plus.png" alt="">
                              </span>
                              <span class="minus" @click.prevent="products.updateQuantity(product.id, product.size_id, product.quantity-1)">
                                <img src="@/assets/img/icon/minus.png" alt="">
                              </span>
                            </div>
                          </form>
                        </div>
                      </td>
                      <td class="product-subtotal" v-if="product.discount === 0"><span>
                        {{product.price * product.quantity}}.000 VND
                      </span></td>
                      <td class="product-subtotal" v-else><span>
                        {{(product.price * (1 - product.discount / 100)) * product.quantity}}.000 VND
                      </span></td>
                      <td class="product-delete"><a @click.prevent="products.removeProduct(product.id, product.size_id)">
                        <font-awesome-icon :icon="['fas', 'trash']" />
                      </a></td>
                    </tr>
                  </tbody>
                  <thead>
                    <tr>
                      <th class="product-thumbnail">Tổng đơn giá</th>
                      <th class="product-name"></th>
                      <th class="product-price"></th>
                      <th class="product-quantity"></th>
                      <th class="product-subtotal">{{products.totalPrice}}.000 VND</th>
                      <th class="product-delete"></th>
                    </tr>
                  </thead>
                </table>
              </div>
              <div class="shop-cart-bottom mt-20">
                <div class="cart-coupon">
                  <router-link :to="{name: 'public-order'}"><button class="btn">Đặt hàng</button></router-link>
                </div>
                <div class="continue-shopping">
                  <router-link :to="{ name: 'public-shop'}"><a href="" class="btn">Tiếp tục mua hàng</a></router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- cart-area-end -->
  </main>
  <!-- main-area-end -->
</template>

<style scoped>
  .breadcrumb-bg {
    background-image: url('@/assets/img/slider/third_slider_bg.jpg');
  }

  .cart-total .btn{
    background: #36363b;
    color: #fff;
    box-shadow: none;
  }

  .cart-coupon .btn{
    background: #ff5400;
    color: #fff;
    box-shadow: none;
    margin-top: 20px;
  }

  :deep(.custom-select-style .ant-select-selector) {
    width: 100%;
    border: 1px solid #f0f0f0;
    border-radius: 0;
    padding: 15px 45px 15px 15px;
    text-align: center;
    height: 55px;
    font-family: 'Jost', sans-serif;
    color: #544842;
    font-weight: 500;
  }
</style>