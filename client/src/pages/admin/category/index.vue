<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {ref, createVNode} from "vue";
  import {ExclamationCircleOutlined} from "@ant-design/icons-vue";
  import {message, Modal} from 'ant-design-vue';

  useMenu().onSelectKeys(["admin-category"])

  const category = ref([]);

  const columns = [
      {
        title: 'STT',
        key: 'index',
      },
      {
        title: 'Tên kiểu dáng',
        dataIndex: 'category_name',
        key: 'category_name',
      },
      {
        title: 'Công cụ',
        key: 'action',
        fixed: 'right',
      },
  ];

  const deleteCategory = (id) =>{
    axios.delete(`http://127.0.0.1:8000/category/${id}`,{
    headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
        .then(function (response) {
          if (response.status === 200) {
            getCategory();
            message.success("Xóa thành công!")
          }
        })
        .catch(function (error) {
          console.log(error);
          message.error("Hiện còn sản phẩm thuộc kiểu dáng này!!!")
        })
  };

  const showConfirm = (id) => {
    Modal.confirm({
      title: 'Bạn chắc chắn muốn xóa kiểu dáng này?',
      icon: createVNode(ExclamationCircleOutlined),
      content: 'Nếu vẫn còn sản phẩm thuộc kiểu dáng này trong kho thì không thể xóa được!',
      onOk() {
        deleteCategory(id)
      },
      onCancel() {},
    });
  };

  const getCategory = () => {
    axios.get('http://127.0.0.1:8000/category/')
      .then(function (response) {
        category.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  getCategory();

</script>

<template>
  <a-card title="Kiểu dáng" style="width: 100%">
    <div class="row mb-3">
      <div class="col-12 d-flex justify-content-end">
        <a-button type="primary">
          <router-link :to="{name: 'admin-category-create'}">
            <font-awesome-icon :icon="['fas', 'plus']" />
          </router-link>
        </a-button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <a-table :dataSource="category" :columns="columns" :scroll="{ x: 576}">
          <template #bodyCell="{column, index, record}">
            <template v-if="column.key==='index'">
              <span>{{ index + 1 }}</span>
            </template>
            <template v-if="column.key==='action'">
              <router-link :to="{ name: 'admin-category-edit', params: { id: record.id }}" >
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
