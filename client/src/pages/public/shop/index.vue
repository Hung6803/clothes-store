<script setup>
  import TheProduct from "@/components/TheProduct.vue";
  import {ref, reactive} from "vue";
  import TheTopProduct from "@/components/TheTopProduct.vue";

  const products = ref([]);
  const brands = ref([]);
  const categories = ref([]);
  const sizes = ref([]);
  const top_products = ref([]);
  const page_total = ref(0);
  const options = reactive({
    page: 1,
    limit: 12,
    category_id: undefined,
    brand_id: undefined,
    size_id: undefined,
    price_min: 0,
    price_max: 10000,
    search: "",
    sort_by: "price",
    sort_order: "asc"
  });
  const getProduct = (options) => {
    axios.post('http://127.0.0.1:8000/product/', options)
      .then(function (response) {
        products.value = response.data.products;
        page_total.value = response.data.total % options.limit === 0 ? response.data.total / options.limit : Math.floor(response.data.total / options.limit) + 1;
      })
      .catch(function (error) {
        console.log(error);
      });
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

  const getSize = () => {
    axios.get('http://127.0.0.1:8000/size/')
      .then(function (response) {
        sizes.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const getTopProduct = () => {
    axios.get(`http://127.0.0.1:8000/product/top/3`)
      .then(function (response) {
        top_products.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      })
  }

  const selectCategory = (categoryId) => {
    options.category_id = categoryId;
    options.page = 1;
    getProduct(options);
  };
  const selectBrand = (brandId) => {
    options.brand_id = brandId;
    options.page = 1;
    getProduct(options);
  };
  const selectSize = (sizeId) => {
    options.size_id = sizeId;
    options.page = 1;
    getProduct(options);
  };
  const inputSearch = () => {
    options.page = 1;
    getProduct(options);
  };
  const price = ref([0, 100000]);
  const onAfterChange = price => {
    options.price_min = price[0];
    options.price_max = price[1];
    options.page = 1;
    getProduct(options);
  };
  const changePage = (newPage) => {
    if (newPage >= 1 && newPage <= page_total.value) {
      options.page = newPage;
      getProduct(options);
    }
  };

  getTopProduct()
  getSize();
  getCategory();
  getBrand();
  getProduct(options);
</script>

<template>
  <section class="breadcrumb-area breadcrumb-bg">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="breadcrumb-content">
            <h2>Sản phẩm</h2>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href=""><router-link :to="{ name: 'public-homepage' }">Trang chủ</router-link></a></li>
                <li class="breadcrumb-item active" aria-current="page">Sản phẩm</li>
              </ol>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- breadcrumb-area-end -->

  <!-- shop-area -->
  <section class="shop-area pt-100 pb-100">
    <div class="container">
      <div class="row">
        <div class="col-xl-9 col-lg-8">
          <div class="shop-top-meta mb-35">
            <div class="row">
              <div class="col-md-12">
                <div class="shop-top-right">
                  <form action="#">
                    <select name="select" v-model="options.sort_order" @change="getProduct(options)">
                      <option value="asc">Tăng dần</option>
                      <option value="desc">Giảm dần</option>
                    </select>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="col-xl-4 col-sm-6" v-for="(product, index) in products">
              <TheProduct :key="index" :product="product"/>
            </div>
          </div>
          <div class="pagination-wrap">
            <ul>
              <li v-if="options.page > 1" class="prev">
                <a @click="changePage(options.page - 1)">Prev</a>
              </li>
              <li v-if="options.page > 2">
                <a @click="changePage(1)">1</a>
              </li>
              <li v-if="options.page > 3">
                <a>...</a>
              </li>
              <li v-if="options.page > 1">
                <a @click="changePage(options.page - 1)">{{ options.page - 1 }}</a>
              </li>
              <li class="active">
                <a>{{ options.page }}</a>
              </li>
              <li v-if="options.page < page_total">
                <a @click="changePage(options.page + 1)">{{ options.page + 1 }}</a>
              </li>
              <li v-if="options.page < page_total - 2">
                <a>...</a>
              </li>
              <li v-if="options.page < page_total - 1">
                <a @click="changePage(page_total)">{{ page_total }}</a>
              </li>
              <li v-if="options.page < page_total" class="next">
                <a @click="changePage(options.page + 1)">Next</a>
              </li>
            </ul>
          </div>
        </div>
        <div class="col-xl-3 col-lg-4">
          <aside class="shop-sidebar">
            <div class="widget side-search-bar">
              <form action="#">
                <input type="text" v-model="options.search">
                <button @click.prevent="inputSearch()"><font-awesome-icon :icon="['fas', 'magnifying-glass']" /></button>
              </form>
            </div>
            <div class="widget">
              <h4 class="widget-title">Kiểu dáng</h4>
              <div class="shop-cat-list">
                <ul>
                  <li >
                    <a href="#" @click.prevent="selectCategory(undefined)">
                      Tất cả
                    </a>
                  </li>
                  <li v-for="category in categories" :key="category.id">
                    <a href="#" @click.prevent="selectCategory(category.id)">
                      {{ category.category_name }}
                    </a>
                  </li>
                </ul>
              </div>
            </div>
            <div class="widget">
              <h4 class="widget-title">Giá</h4>
              <div class="price_filter">
                <a-slider v-model:value="price" :min="0" :max="10000" :step="10" range @afterChange="onAfterChange" />
                <div class="price_slider_amount">
                  <span>Số tiền:</span>
                  <span>{{price[0]}}.000 VND - {{price[1]}}.000 VND</span>
                </div>
              </div>
            </div>
            <div class="widget">
              <h4 class="widget-title">Thương hiệu</h4>
              <div class="shop-cat-list">
                <ul>
                  <li><a href="#" @click.prevent="selectBrand(undefined)">Tất cả</a></li>
                  <li v-for="brand in brands" :key="brand.id">
                    <a href="#" @click.prevent="selectBrand(brand.id)">
                      {{ brand.brand_name }}
                    </a>
                  </li>
                </ul>

              </div>
            </div>
            <div class="widget has-border">
              <div class="sidebar-product-size mb-30">
                <h4 class="widget-title">Size</h4>
                <div class="shop-size-list">
                  <ul>
                    <li><a href="#" @click.prevent="selectSize(undefined)">All</a></li>
                    <li v-for="size in sizes"><a href="#" @click.prevent="selectSize(size.id)">{{size.size_name}}</a></li>
                  </ul>
                </div>
              </div>
            </div>
            <div class="widget">
              <h4 class="widget-title">Sản phẩm bán chạy</h4>
              <div class="sidebar-product-list">
                <ul>
                  <TheTopProduct v-for="product in top_products" :product="product"/>
                </ul>
              </div>
            </div>
          </aside>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.breadcrumb-bg {
  background-image: url('@/assets/img/slider/third_slider_bg.jpg');
}

</style>