<template>
  <div class="menu">
    <a-menu
      v-model:openKeys="openKeys"
      v-model:selectedKeys="selectedKeys"
      mode="inline"
    >
      <a-sub-menu key="portfolio">
        <template #title><skin-outlined class="me-2"/>Danh mục</template>
        <a-menu-item key="admin-product">
          <router-link :to="{ name: '' }">
            <span>Sản phẩm</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="admin-brand">
          <router-link :to="{ name: 'admin-brand' }">
            <span>Thương hiệu</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="admin-category">
          <router-link :to="{ name: 'admin-category' }">
            <span>Kiểu dáng</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="admin-size">
          <router-link :to="{ name: 'admin-size' }">
            <span>Size</span>
          </router-link>
        </a-menu-item>
      </a-sub-menu>

      <a-sub-menu key="account">
        <template #title><user-outlined class="me-2"/>Tài khoản</template>
        <a-menu-item key="admin-customer">
          <router-link :to="{ name: '' }">
            <span>Khách hàng</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="admin-employee">
          <router-link :to="{ name: '' }">
            <span>Nhân viên</span>
          </router-link>
        </a-menu-item>
      </a-sub-menu>

      <a-sub-menu key="invoice">
        <template #title><shopping-outlined class="me-2"/>Hóa đơn</template>
        <a-menu-item key="admin-invoice-new">
          <router-link :to="{ name: '' }">
            <span>Hóa đơn mới</span>
          </router-link>
        </a-menu-item>
        <a-menu-item key="admin-invoice">
          <router-link :to="{ name: '' }">
            <span>Danh sách hóa đơn</span>
          </router-link>
        </a-menu-item>
      </a-sub-menu>
    </a-menu>
  </div>
</template>

<script>
import {UserOutlined, ShoppingOutlined, SkinOutlined} from "@ant-design/icons-vue"
import { defineComponent } from 'vue';
import {storeToRefs} from "pinia";
import {useMenu} from "@/store/use-menu-admin.js";

export default defineComponent({
  components: {
    UserOutlined,
    ShoppingOutlined,
    SkinOutlined
  },
  setup() {
    const store = useMenu();

    return {
      ...storeToRefs(store)
    };
  },
});
</script>

<style scoped>
.menu{
  width: 100%;
}
</style>