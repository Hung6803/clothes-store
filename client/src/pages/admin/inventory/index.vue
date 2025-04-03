<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {ref, createVNode} from "vue";
  import {ExclamationCircleOutlined} from "@ant-design/icons-vue";
  import {message, Modal} from 'ant-design-vue';

  useMenu().onSelectKeys(["admin-inventory"])

  const inventory = ref([]);

  const columns = [
    {
      title: 'STT',
      key: 'index',
    },
    {
      title: 'Mã sản phẩm',
      dataIndex: ['product', 'id'],
      key: 'product_id',
    },
    {
      title: 'Tên sản phẩm',
      dataIndex: ['product', 'product_name'],
      key: 'product_name',
    },
    {
      title: 'Size',
      dataIndex: ['size', 'size_name'],
      key: 'size_name',
    },
    {
      title: 'Giá nhập',
      dataIndex: 'import_price',
      key: 'import_price',
    },
    {
      title: 'Số lượng',
      dataIndex: 'quantity',
      key: 'quantity',
    },
    {
      title: 'Công cụ',
      key: 'action',
      fixed: 'right',
    },
  ];

  const deleteInventory = (prodcut_id, size_id) =>{
    axios.delete(`http://127.0.0.1:8000/inventory/${prodcut_id}/${size_id}`,{
    headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
        .then(function (response) {
          if (response.status === 200) {
            getInventory();
            message.success("Xóa thành công!")
          }
        })
        .catch(function (error) {
          message.error("Đã có hóa đơn mua sản phẩm này!")
        })
  };

  const showConfirm = (prodcut_id, size_id) => {
    Modal.confirm({
      title: 'Bạn chắc chắn muốn xóa sản phẩm này?',
      icon: createVNode(ExclamationCircleOutlined),
      content: 'Nếu sản phẩm này đã từng được bán thì không thể xóa được!',
      onOk() {
        deleteInventory(prodcut_id, size_id)
      },
      onCancel() {},
    });
  };

  const getInventory = () => {
    axios.get('http://127.0.0.1:8000/inventory/')
      .then(function (response) {
        inventory.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  getInventory();

</script>

<template>
  <a-card title="Sản phẩm trong kho" style="width: 100%">
    <div class="row mb-3">
      <div class="col-12 d-flex justify-content-end">
        <a-button type="primary">
          <router-link :to="{name: 'admin-inventory-create'}">
            <font-awesome-icon :icon="['fas', 'plus']" />
          </router-link>
        </a-button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <a-table :dataSource="inventory" :columns="columns" :scroll="{ x: 576}">
          <template #bodyCell="{column, index, record}">
            <template v-if="column.key==='index'">
              <span>{{ index + 1 }}</span>
            </template>
            <template v-if="column.key==='action'">
              <router-link :to="{ name: 'admin-inventory-edit', params: { product_id: record.product.id, size_id: record.size.id }}" >
                <a-button type="primary" class="me-sm-2 mb-2">
                  <font-awesome-icon :icon="['fas', 'pen-to-square']" />
                </a-button>
              </router-link>
              <a-button type="primary" danger @click="showConfirm(record.product.id, record.size.id)">
                  <font-awesome-icon :icon="['fas', 'trash']" />
              </a-button>
            </template>
          </template>
        </a-table>
      </div>
    </div>
  </a-card>
</template>