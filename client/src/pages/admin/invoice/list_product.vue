<template>
    <div class="row">
      <div class="col-12">
        <a-table :dataSource="list_product" :columns="columns" :scroll="{ x: 576}">
          <template #bodyCell="{column, index}">
            <template v-if="column.key==='index'">
              <span>{{ index + 1 }}</span>
            </template>
            <template v-if="column.key==='payable'">
              <span>{{payable[index].toString()}}</span>
            </template>
          </template>
        </a-table>
      </div>
    </div>
</template>

<script setup>
  import {ref} from "vue";

  const props = defineProps({
    id: {
      type: Number,
      required: true
    }
  });
  const list_product = ref([]);
  const columns = [
    {
      title: 'STT',
      key: 'index',
    },
    {
      title: 'Mã sản phẩm',
      dataIndex: ['inventory', 'product', 'id'],
      key: 'product_id',
    },
    {
      title: 'Tên sản phẩm',
      dataIndex: ['inventory', 'product', 'product_name'],
      key: 'product_name',
    },
    {
      title: 'Size',
      dataIndex: ['inventory', 'size', 'size_name'],
      key: 'size_name',
    },
    {
      title: 'Số lượng',
      dataIndex: 'quantity',
      key: 'quantity',
    },
    {
      title: 'Giá',
      dataIndex: 'price',
      key: 'price',
    },
    {
      title: 'Giảm giá',
      dataIndex: 'discount',
      key: 'discount',
    },
    {
      title: 'Thành tiền',
      key: 'payable',
    }
  ];
  const payable = ref([])

  const getInvoiceDetail = () => {
    axios.get(`http://127.0.0.1:8000/invoice_details/${props.id}`)
        .then(function (response) {
          list_product.value = response.data;
          console.log(list_product)
          let length = list_product.value.length
          for(let index = 0; index < length; index++)
          {
            let price = parseInt(list_product.value[index].price)
            payable.value[index] = price - (parseInt(list_product.value[index].discount) * price / 100);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
  };

  getInvoiceDetail();
</script>
