<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRouter} from "vue-router";
  import {reactive} from "vue";

  useMenu().onSelectKeys(["admin-size"])

  const router = useRouter();

  const size = reactive({
    size_name: "",
  });
  const createSize = () =>{
    axios.post("http://127.0.0.1:8000/size/create", size)
    .then(function (response) {
      if (response) {
        message.success("Tạo mới thành công!");
        router.push({name: 'admin-size'});
      }
    })
    .catch(function (error) {
      console.log(error);
    });
    };

</script>

<template>
  <form @submit.prevent="createSize()">
    <a-card title="Thêm size mới" style="width: 100%">
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Size:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input placeholder="Size" allow-clear v-model:value="size.size_name"/>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-8 d-sm-flex justify-content-center">
          <a-button class="me-2">
            <router-link :to="{name: 'admin-size'}">
              <span>Hủy</span>
            </router-link>
          </a-button>
          <a-button type="primary" html-type="submit"><span>Thêm mới</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>
