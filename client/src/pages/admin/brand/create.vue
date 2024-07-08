<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRouter} from "vue-router";

  useMenu().onSelectKeys(["admin-brand"])

  const router = useRouter();

  const brand = {
    brand_name: "",
  };
  const createBrand = () =>{
    axios.post("http://127.0.0.1:8000/brand/create", brand)
    .then(function (response) {
      if (response) {
        message.success("Tạo mới thành công!");
        router.push({name: 'admin-brand'});
      }
    })
    .catch(function (error) {
      console.log(error);
    });
    };

</script>

<template>
  <form @submit.prevent="createBrand()">
    <a-card title="Thêm thương hiệu mới" style="width: 100%">
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
          <a-button type="primary" html-type="submit"><span>Thêm mới</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>
