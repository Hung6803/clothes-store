<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRoute, useRouter} from "vue-router";
  import {reactive, ref} from "vue"

  useMenu().onSelectKeys(["admin-inventory"])

  const router = useRouter();
  const route = useRoute();

  const inventory = reactive({
    product_id: undefined,
    size_id: undefined,
    import_price: undefined,
    quantity: undefined,
  });

  const products = ref([]);
  const size = ref([]);
  const getInventorybyID = () =>{
    axios.get(`http://127.0.0.1:8000/inventory/${route.params.product_id}/${route.params.size_id}`)
    .then(function (response) {
      inventory.product_id = response.data.product.id;
      inventory.size_id = response.data.size.id;
      inventory.import_price = response.data.import_price
      inventory.quantity = response.data.quantity
    })
    .catch(function (error) {
      console.log(error);
    })
  };

  const editInventory = () =>{
    axios.put(`http://127.0.0.1:8000/inventory/edit/${route.params.product_id}/${route.params.size_id}`, inventory,{
    headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
    .then(function (response) {
      if (response) {
        message.success("Sửa thông tin thành công!");
        router.push({name: 'admin-inventory'});
      }
    })
    .catch(function (error) {
      console.log(error);
    });
  };

  getInventorybyID();

   const getProductName = () => {
    axios.get('http://127.0.0.1:8000/product/product_name')
      .then(function (response) {
        products.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const getSize = () => {
    axios.get('http://127.0.0.1:8000/size/')
      .then(function (response) {
        size.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  getSize();

  getProductName();

  const filterOption = (input, option) => {
    return option.product_name.toLowerCase().indexOf(input.toLowerCase()) >= 0;
  };

</script>

<template>
  <form @submit.prevent="editInventory()">
    <a-card title="Sửa thông tin sản phẩm" style="width: 100%">
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Tên sản phẩm:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-select
            v-model:value="inventory.product_id"
            show-search
            placeholder="Tên sản phẩm"
            style="width: 100%"
            :options="products"
            :filter-option="filterOption"
            :field-names="{label: 'product_name', value: 'id'}"
          ></a-select>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Size:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-select
            ref="select"
            v-model:value="inventory.size_id"
            placeholder="Size"
            style="width: 100%"
            :options="size"
            :field-names="{label: 'size_name', value: 'id'}"
          ></a-select>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Giá nhập:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input-number
              style="width: 100%"
              placeholder="Giá nhập"
              v-model:value="inventory.import_price"
              addon-after="VND"></a-input-number>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span>Số lượng:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input-number
              style="width: 100%"
              placeholder="Số lượng"
              v-model:value="inventory.quantity"></a-input-number>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-8 d-sm-flex justify-content-center">
          <a-button class="me-2">
            <router-link :to="{name: 'admin-inventory'}">
              <span>Hủy</span>
            </router-link>
          </a-button>
          <a-button type="primary" html-type="submit"><span>Lưu</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>

