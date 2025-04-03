<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {ref, createVNode} from "vue";
  import {ExclamationCircleOutlined} from "@ant-design/icons-vue";
  import {message, Modal} from 'ant-design-vue';

  useMenu().onSelectKeys(["admin-product"])

  const products = ref([]);

  const columns = [
    {
      title: 'STT',
      key: 'index',
    },
    {
      title: 'Ảnh sản phẩm',
      key: 'product_image',
    },
    {
      title: 'Tên sản phẩm',
      dataIndex: 'product_name',
      key: 'product_name',
    },
    {
      title: 'Kiểu dáng',
      dataIndex: ['category', 'category_name'],
      key: 'category_name',
    },
    {
      title: 'Thương hiệu',
      dataIndex: ['brand', 'brand_name'],
      key: 'brand_name',
    },
    {
      title: 'Giá bán',
      dataIndex: 'price',
      key: 'price',
    },
    {
      title: 'Giảm giá',
      dataIndex: 'discount',
      key: 'discount',
    },
    {
      title: 'Mô tả',
      dataIndex: 'product_description',
      key: 'product_description',
    },
    {
      title: 'Công cụ',
      key: 'action',
      fixed: 'right',
    },
  ];

  const deleteProduct = (id) =>{
    axios.delete(`http://127.0.0.1:8000/product/${id}`,{
    headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
        .then(function (response) {
          if (response.status === 200) {
            getProduct();
            message.success("Xóa thành công!")
          }
        })
        .catch(function (error) {
          message.error("Sản phẩm này vẫn còn trong kho!")
        })
  };

  const showConfirm = (id) => {
    Modal.confirm({
      title: 'Bạn chắc chắn muốn xóa sản phẩm này?',
      icon: createVNode(ExclamationCircleOutlined),
      content: 'Nếu sản phẩm này vẫn còn trong kho thì không thể xóa được!',
      onOk() {
        deleteProduct(id)
      },
      onCancel() {},
    });
  };

  const getProduct = () => {
    axios.get('http://127.0.0.1:8000/product/')
      .then(function (response) {
        products.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  getProduct();

</script>

<template>
  <a-card title="Sản phẩm" style="width: 100%">
    <div class="row mb-3">
      <div class="col-12 d-flex justify-content-end">
        <a-button type="primary">
          <router-link :to="{name: 'admin-product-create'}">
            <font-awesome-icon :icon="['fas', 'plus']" />
          </router-link>
        </a-button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <a-table :dataSource="products" :columns="columns" :scroll="{ x: 576}">
          <template #bodyCell="{column, index, record}">
            <template v-if="column.key==='index'">
              <span>{{ index + 1 }}</span>
            </template>
            <template v-if="column.key==='product_image'">
              <img :width="60" :height="100" :src="`http://127.0.0.1:8000/image/${record.product_image.image_path}`" alt="Product Image">
            </template>
            <template v-if="column.key==='action'">
              <router-link :to="{ name: 'admin-product-edit', params: { id: record.id }}" >
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