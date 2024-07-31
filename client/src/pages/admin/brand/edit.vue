<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRoute, useRouter} from "vue-router";
  import {reactive} from "vue"

  useMenu().onSelectKeys(["admin-brand"])

  const router = useRouter();
  const route = useRoute();

  const brand = reactive({
    brand_name: "",
  });



  const getBrandbyID = () =>{
    axios.get(`http://127.0.0.1:8000/brand/${route.params.id}`)
    .then(function (response) {
      console.log(response.data);
      brand.brand_name = response.data.brand_name
    })
    .catch(function (error) {
      console.log(error);
    })
  }
  const editBrand = () =>{
    axios.put(`http://127.0.0.1:8000/brand/edit/${route.params.id}`, brand,{
    headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
    .then(function (response) {
      if (response) {
        message.success("Sửa thông tin thành công!");
        router.push({name: 'admin-brand'});
      }
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  getBrandbyID()

</script>

<template>
  <form @submit.prevent="editBrand()">
    <a-card title="Sửa tên thương hiệu" style="width: 100%">
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Tên thương hiệu:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input placeholder="Tên thương hiệu" allow-clear v-model:value="brand.brand_name"/>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-8 d-sm-flex justify-content-center">
          <a-button class="me-2">
            <router-link :to="{name: 'admin-brand'}">
              <span>Hủy</span>
            </router-link>
          </a-button>
          <a-button type="primary" html-type="submit"><span>Lưu</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>
