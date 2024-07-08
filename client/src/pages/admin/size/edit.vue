<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRoute, useRouter} from "vue-router";
  import {reactive} from "vue"

  useMenu().onSelectKeys(["admin-size"])

  const router = useRouter();
  const route = useRoute();

  const size = reactive({
    size_name: "",
  });



  const getSizebyID = () =>{
    axios.get(`http://127.0.0.1:8000/size/${route.params.id}`)
    .then(function (response) {
      console.log(response.data);
      size.size_name = response.data.size_name
    })
    .catch(function (error) {
      console.log(error);
    })
  }
  const editSize = () =>{
    axios.put(`http://127.0.0.1:8000/size/edit/${route.params.id}`, size)
    .then(function (response) {
      if (response) {
        message.success("Sửa thông tin thành công!");
        router.push({name: 'admin-size'});
      }
    })
    .catch(function (error) {
      console.log(error);
    });
  }

  getSizebyID()

</script>

<template>
  <form @submit.prevent="editSize()">
    <a-card title="Sửa tên thương hiệu" style="width: 100%">
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Tên thương hiệu:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input placeholder="Tên thương hiệu" allow-clear v-model:value="size.size_name"/>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-8 d-sm-flex justify-content-center">
          <a-button class="me-2">
            <router-link :to="{name: 'admin-size'}">
              <span>Hủy</span>
            </router-link>
          </a-button>
          <a-button type="primary" html-type="submit"><span>Lưu</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>
