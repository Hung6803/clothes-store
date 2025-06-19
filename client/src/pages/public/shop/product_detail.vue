<script setup>
  import {useRoute} from "vue-router";
  import {reactive, ref, watch} from "vue";
  import TheProduct from "@/components/TheProduct.vue";
  import {useCartStore} from "@/store/use-cart-client.js";
  import {message} from "ant-design-vue";

  const route = useRoute();
  const cartStore = useCartStore();

  const product = reactive({
    id: "",
    product_name: "",
    product_description: "",
    price: undefined,
    discount: undefined,
    category_name: "",
    brand_name: "",
    product_image: [],
  });
  const cart_product = reactive({
    id: "",
    product_name: "",
    price: undefined,
    discount: undefined,
    product_image: "",
    total_quantity: undefined,
    quantity: 1,
    size_id: undefined,
  });
  const image_path = ref();
  const product_sizes = reactive({
    product: {
      id: undefined,
      product_name: "",
    },
    sizes: [],
    quantity: [],
  });
  const selected_size = ref(0);
  const selected_size_index = ref(0);
  const quantity = ref(1);
  const products = ref([]);
  const productId = ref(route.params.id);
  const getProductbyID = async (id) =>{
    axios.get(`http://127.0.0.1:8000/product/${id}`)
    .then(function (response) {
      product.id = response.data.id;
      product.product_name = response.data.product_name
      product.product_description = response.data.product_description
      product.brand_name = response.data.brand.brand_name
      product.category_name = response.data.category.category_name
      product.price = response.data.price
      product.discount = response.data.discount
      product.product_image = response.data.product_image
      image_path.value = product.product_image[0].image_path;
      cart_product.product_name = response.data.product_name;
      cart_product.id = response.data.id;
      cart_product.price = response.data.price;
      cart_product.discount = response.data.discount;
      cart_product.product_image = response.data.product_image[0].image_path;

      const options = {
        page: 1,
        limit: 4,
        category_id: response.data.category.id,
        brand_id: response.data.brand.id,
        size_id: undefined,
        price_min: 0,
        price_max: 10000,
        search: "",
        sort_by: "",
        sort_order: "asc"
      };
      getProduct(options);
    })
    .catch(function (error) {
      console.log(error);
    })
  };

  const getProduct = (options) => {
    axios.post('http://127.0.0.1:8000/product/', options)
      .then(function (response) {
        products.value = response.data.products;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const selectImage = (path) => {
    image_path.value = path;
  };

  const getProductSize = async (id) => {
    axios.get(`http://127.0.0.1:8000/inventory/${id}`)
    .then(function (response) {
      product_sizes.product = response.data.product;
      product_sizes.sizes = response.data.sizes;
      product_sizes.quantity = response.data.quantity;
    })
    .catch(function (error) {
      console.log(error);
    })
  };

  const selectSize = (size_id, index) => {
    selected_size.value = size_id;
    selected_size_index.value = index;
    cart_product.size_id = size_id;
    cart_product.total_quantity = product_sizes.quantity[index];
  };

  const upQuantity = () => {
    if (quantity.value < product_sizes.quantity[selected_size_index.value])
    {
      quantity.value += 1;
    }
  };

  const downQuantity = () => {
    if (quantity.value > 1){
      quantity.value -= 1;
    }
  };

  const addToCart = () => {
    if (selected_size.value !== 0){
      cart_product.quantity = quantity.value;
      cartStore.addProduct(cart_product);
    } else{
      message.warn("Bạn cần chọn size của sản phẩm!");
    }
  }

  getProductbyID(productId.value);
  getProductSize(productId.value);

  watch(() => route.params.id, async (newId) => {
    productId.value = newId;
    selected_size.value = 0;
    selected_size_index.value = 0;
    quantity.value = 1;
    await getProductbyID(newId);
    await getProductSize(newId);
    window.scrollTo({top: 0, behavior: 'smooth'});
  })
</script>

<template>
  <!-- shop-details-area -->
  <section class="shop-details-area pt-100 pb-95">
    <div class="container">
      <div class="row">
        <div class="col-lg-7">
          <div class="shop-details-flex-wrap">
            <div class="shop-details-nav-wrap">
              <ul class="nav nav-tabs">
                <li class="nav-item" v-for="image in product.product_image">
                  <a class="nav-link" :class="{ active: image.image_path === image_path }" @click="selectImage(image.image_path)">
                    <img :src="`http://127.0.0.1:8000/image/${ image.image_path }`" alt="">
                  </a>
                </li>
              </ul>
            </div>
            <div class="shop-details-img-wrap">
              <div class="tab-content">
                <div class="tab-pane fade show active">
                  <div class="shop-details-img">
                    <img v-if="image_path" :src="`http://127.0.0.1:8000/image/${ image_path }`" alt="">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-5">
          <div class="shop-details-content">
            <a href="#" class="product-cat">{{ product.brand_name }}</a>
            <h3 class="title">{{ product.product_name }}</h3>
            <p class="style-name">Kiểu dáng : {{ product.category_name}}</p>
            <div class="price" v-if="product.discount === 0">Giá : {{ product.price }}.000 VND</div>
            <div class="price" v-if="product.discount !== 0">Giá :
              <span class="del-price">{{ product.price }}.000</span>
              {{ product.price * (1 - product.discount / 100) }}.000 VND
            </div>
            <div class="product-details-info">
              <div class="sidebar-product-size mb-30">
                <h4 class="widget-title">Size</h4>
                <div class="shop-size-list">
                  <ul>
                    <li v-for="(size, index) in product_sizes.sizes">
                      <a :class="{ active: size.id === selected_size }" @click.prevent="selectSize(size.id, index)">
                        {{size.size_name}}
                      </a>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="perched-info">
              <div class="cart-plus-minus">
                <form action="#" class="num-block">
                  <input type="text" class="in-num" :value="quantity" readonly="">
                  <div class="qtybutton-box">
                    <span class="plus" @click.prevent="upQuantity()">
                      <img src="@/assets/img/icon/plus.png" alt="">
                    </span>
                    <span class="minus" @click.prevent="downQuantity()"><img src="@/assets/img/icon/minus.png" alt=""></span>
                  </div>
                </form>
              </div>
              <a class="btn" @click.prevent="addToCart()">Thêm vào giỏ hàng</a>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <div class="product-desc-wrap">
            <ul class="nav nav-tabs" role="tablist">
              <li class="nav-item" role="presentation">
                <a class="nav-link active" id="description-tab" data-toggle="tab" href="#description" role="tab" aria-controls="description"
                   aria-selected="true">Thông tin sản phẩm</a>
              </li>
            </ul>
            <div class="tab-content">
              <div class="tab-pane fade show active" id="description" role="tabpanel" aria-labelledby="description-tab">
                <div class="product-desc-title mb-30">
                  <h4 class="title">Thông tin chi tiết :</h4>
                </div>
                <p>{{product.product_description}}</p>
                <div class="product-desc-title mb-30">
                  <h4 class="title">Hướng dẫn chọn size :</h4>
                </div>
                <div class="additional-table">
                  <div class="table-responsive">
                    <table class="table table-bordered">
                      <tbody>
                        <tr>
                          <th scope="row">Size</th>
                          <td>XS</td>
                          <td>S</td>
                          <td>M</td>
                          <td>L</td>
                          <td>XL</td>
                          <td>XXL</td>
                        </tr>
                        <tr>
                          <th scope="row">Chiều cao</th>
                          <td>1m55 - 1m59</td>
                          <td>1m60 - 1m65</td>
                          <td>1m66 - 1m72</td>
                          <td>1m73 - 1m77</td>
                          <td>1m78 - 1m83</td>
                          <td>1m84 - 1m88</td>
                        </tr>
                        <tr>
                          <th scope="row">Cân nặng</th>
                          <td>48kg - 54kg</td>
                          <td>55kg - 61kg</td>
                          <td>62kg - 68kg</td>
                          <td>69kg - 75kg</td>
                          <td>76kg - 82kg</td>
                          <td>83kg - 87kg</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
                <p></p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="related-product-wrap">
        <div class="row">
          <div class="col-12">
            <div class="related-product-title">
              <h4 class="title">Có thể bạn sẽ thích!</h4>
            </div>
          </div>
        </div>
        <div class="row related-product-active">
          <div class="col-xl-3" v-for="(product, index) in products">
            <TheProduct :key="index" :product="product"/>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- shop-details-area-end -->
</template>

<style scoped>
  .shop-size-list ul li a.active{
    background: #ff5400;
  }
  .del-price{
    text-decoration: line-through;
    color: #676565;
  }
</style>