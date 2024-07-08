<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRouter} from "vue-router";

  useMenu().onSelectKeys(["admin-category"])

  const router = useRouter();

  const category = {
    category_name: "",
  };
  const createCategory = () =>{
    axios.post("http://127.0.0.1:8000/category/create", category)
    .then(function (response) {
      if (response) {
        message.success("Tạo mới thành công!");
        router.push({name: 'admin-category'});
      }
    })
    .catch(function (error) {
      console.log(error);
    });
    };

</script>

<template>
  <form @submit.prevent="createCategory()">
    <a-card title="Thêm kiểu dáng mới" style="width: 100%">
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Kiểu dáng:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input placeholder="Kiểu dáng" allow-clear v-model:value="category.category_name"/>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-8 d-sm-flex justify-content-center">
          <a-button class="me-2">
            <router-link :to="{name: 'admin-category'}">
              <span>Hủy</span>
            </router-link>
          </a-button>
          <a-button type="primary" html-type="submit"><span>Thêm mới</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>
