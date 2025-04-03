
<template>

  <div class="container-fluid">
    <div class="row text-white header-background">
      <div class="col-1 d-flex d-sm-none align-items-center justify-content-center">
        <span @click="showDrawer"><menu-outlined /></span>
      </div>
      
      <div class="col-10 col-sm-9 d-flex align-items-center justify-content-center justify-content-sm-start">
        <img src="../assets/img/logo.png" alt="logo" class="logo ms-3 me-3"/>
        <span class="d-none d-sm-flex">ADMIN</span>
      </div>

      <div class="col-sm-3 d-none d-sm-flex align-items-center justify-content-sm-end">
        <a-dropdown>
    <a class="ant-dropdown-link" @click.prevent>
      <font-awesome-icon :icon="['fas', 'user']" />
    </a>
    <template #overlay>
      <a-menu>
        <a-menu-item key="logout">
          <router-link :to="{ name: '' }">
            <span>Đăng xuất</span>
          </router-link>
        </a-menu-item>
      </a-menu>
    </template>
  </a-dropdown>
      </div>
      <div class="col-1 d-flex d-sm-none align-items-center justify-content-center">
        <span @click="showDrawerAccount"><font-awesome-icon :icon="['fas', 'user-tie']" /></span>
      </div>
    </div>
  </div>

  <a-drawer
    v-model:open="open"
    title="Danh mục"
    placement="left"
  >
    <TheMenuAdmin />
  </a-drawer>

  <a-drawer
    v-model:open="open_account"
    title="Tài khoản"
    placement="right"
  >
    <p>Some contents...</p>
    <p>Some contents...</p>
    <p>Some contents...</p>
  </a-drawer>
</template>

<style scoped>
  .header-background{
    background-color: deepskyblue;
    padding: 1rem;
  }
  .logo{
    height: 40px;
    width: 140px
  }
  .avatar{
    background-color: azure;
  }
</style>

<script setup>
import TheMenuAdmin from "@/components/TheMenuAdmin.vue";
import {MenuOutlined, DownOutlined} from "@ant-design/icons-vue"
import { ref } from 'vue';
const open = ref(false);
const open_account = ref(false);
const showDrawer = () => {
  open.value = true;
};
const showDrawerAccount = () => {
  open_account.value = true;
};

</script>