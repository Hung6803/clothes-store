<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRoute, useRouter} from "vue-router";
  import {reactive} from "vue"

  useMenu().onSelectKeys(["admin-category"])

  const router = useRouter();
  const route = useRoute();

  const category = reactive({
    category_name: "",
  });



  const getCategorybyID = () =>{
    axios.get(`http://127.0.0.1:8000/category/${route.params.id}`)
    .then(function (response) {
      console.log(response.data);
      category.category_name = response.data.category_name
    })
    .catch(function (error) {
      console.log(error);
    })
  }
  const editCategory = () =>{
    axios.put(`http://127.0.0.1:8000/category/edit/${route.params.id}`, category)
    .then(function (response) {
      if (response) {
        message.success("Sửa thông tin thành công!");
        router.push({name: 'admin-category'});
      }
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  getCategorybyID()

</script>

<template>
  <form @submit.prevent="editCategory()">
    <a-card title="Sửa tên kiểu dáng" style="width: 100%">
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
          <a-button type="primary" html-type="submit"><span>Lưu</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>
