<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRouter} from "vue-router";
  import {ref, reactive} from "vue";

  useMenu().onSelectKeys(["admin-product"])

  const router = useRouter();

  const product = reactive({
    product_name: "",
    product_description: "",
    price: undefined,
    category_id: undefined,
    brand_id: undefined,
  });

  const brands = ref([]);
  const categories = ref([]);

  const createProduct = () =>{
    axios.post("http://127.0.0.1:8000/product/create", product,{
    headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
    .then(function (response) {
      if (response) {
        message.success("Tạo mới thành công!");
        router.push({name: 'admin-product'});
      }
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

  getCategory();

  getBrand();

</script>

<template>
  <form @submit.prevent="createProduct()">
    <a-card title="Thêm sản phẩm mới" style="width: 100%">
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Tên sản phẩm:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input placeholder="Tên sản phẩm" allow-clear v-model:value="product.product_name"/>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Thương hiệu:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-select
            ref="select"
            v-model:value="product.brand_id"
            placeholder="Thương hiệu"
            style="width: 100%"
            :options="brands"
            :field-names="{label: 'brand_name', value: 'id'}"
          ></a-select>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Kiểu dáng:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-select
            ref="select"
            v-model:value="product.category_id"
            placeholder="Kiểu dáng"
            style="width: 100%"
            :options="categories"
            :field-names="{label: 'category_name', value: 'id'}"
          ></a-select>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Giá bán:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input-number
              style="width: 100%"
              placeholder="Giá bán"
              v-model:value="product.price"
              addon-after="VND"></a-input-number>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span>Mô tả sản phẩm:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-textarea v-model:value="product.product_description" placeholder="Mô tả sản phẩm" :rows="4" />
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-8 d-sm-flex justify-content-center">
          <a-button class="me-2">
            <router-link :to="{name: 'admin-product'}">
              <span>Hủy</span>
            </router-link>
          </a-button>
          <a-button type="primary" html-type="submit"><span>Thêm mới</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>
