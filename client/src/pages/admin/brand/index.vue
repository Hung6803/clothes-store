<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {ref, createVNode} from "vue";
  import {ExclamationCircleOutlined} from "@ant-design/icons-vue";
  import {message, Modal} from 'ant-design-vue';

  useMenu().onSelectKeys(["admin-brand"])

  const brand = ref([]);

  const columns = [
      {
        title: 'STT',
        key: 'index',
      },
      {
        title: 'Tên thương hiệu',
        dataIndex: 'brand_name',
        key: 'brand_name',
      },
      {
        title: 'Công cụ',
        key: 'action',
        fixed: 'right',
      },
  ];

  const deleteBrand = (id) =>{
    axios.delete(`http://127.0.0.1:8000/brand/${id}`,{
    headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
        .then(function (response) {
          if (response.status === 200) {
            getBrand();
            message.success("Xóa thành công!")
          }
        })
        .catch(function (error) {
          console.log(error);
          message.error("Hiện còn sản phẩm thuộc thương hiệu này!!!")
        })
  };

  const showConfirm = (id) => {
    Modal.confirm({
      title: 'Bạn chắc chắn muốn xóa thương hiệu này?',
      icon: createVNode(ExclamationCircleOutlined),
      content: 'Nếu vẫn còn sản phẩm của thương hiệu này trong kho thì không thể xóa được!',
      onOk() {
        deleteBrand(id)
      },
      onCancel() {},
    });
  };

  const getBrand = () => {
    axios.get('http://127.0.0.1:8000/brand/')
      .then(function (response) {
        brand.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  getBrand();

</script>

<template>
  <a-card title="Thương hiệu" style="width: 100%">
    <div class="row md-3">
      <div class="col-12 d-flex justify-content-end">
        <a-button type="primary">
          <router-link :to="{name: 'admin-brand-create'}">
            <font-awesome-icon :icon="['fas', 'plus']" />
          </router-link>
        </a-button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <a-table :dataSource="brand" :columns="columns" :scroll="{ x: 576}">
          <template #bodyCell="{column, index, record}">
            <template v-if="column.key==='index'">
              <span>{{ index + 1 }}</span>
            </template>
            <template v-if="column.key==='action'">
              <router-link :to="{ name: 'admin-brand-edit', params: { id: record.id }}" >
                <a-button type="primary" class="me-sm-2 mb-2">
                  <font-awesome-icon :icon="['fas', 'pen-to-square']" />
                </a-button>
              </router-link>
              <a-button type="primary" danger @click="showConfirm(record.id)">
                  <font-awesome-icon :icon="['fas', 'trash']" />
              </a-button>
            </template>
          </template>
        </a-table>
      </div>
    </div>
  </a-card>
</template>
