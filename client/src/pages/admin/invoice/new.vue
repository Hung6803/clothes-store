<script setup>
import {useMenu} from "@/store/use-menu-admin.js";
import {ref, createVNode, computed, reactive, toRaw} from "vue";
import ListProduct from "@/pages/admin/invoice/list_product.vue";
import dayjs from "dayjs";
import {message} from "ant-design-vue";


useMenu().onSelectKeys(["admin-invoice-new"])

const invoices = ref([]);

const columns = [
  {
    title: 'STT',
    key: 'index',
  },
  {
    title: 'Mã đơn hàng',
    dataIndex: 'id',
    key: 'id',
  },
  {
    title: 'Tổng đơn giá',
    dataIndex: 'total_price',
    key: 'total_price',
  },
  {
    title: 'Mã khách hàng',
    dataIndex: ['customer', 'id'],
    key: 'customer_id',
  },
  {
    title: 'Tên khách hàng',
    dataIndex: ['customer', 'name'],
    key: 'customer_id',
  },
  {
    title: 'Địa chỉ nhận hàng',
    dataIndex: 'address',
    key: 'address',
  },
  {
    title: 'Ngày tạo',
    dataIndex: 'creation_date',
    key: 'creation_date',
  },
  {
    title: 'Tình trạng',
    dataIndex: 'status',
    key: 'status',
  },
  {
    title: 'Công cụ',
    key: 'action',
    fixed: 'right',
  },
];

const status = ['Chưa xác nhận', 'Đã xác nhận']



const editStatus = (selectedRowKeys) => {
  let list_id = selectedRowKeys.map(item => ({ id: item }));
  if (list_id.length > 0) {
    axios.put(`http://127.0.0.1:8000/invoice/edit/status`, list_id)
        .then(response => {
          if (response) {
            getNewInvoice();
            message.success("Xác nhận đơn hàng thành công!");
          }
        })
        .catch(function (error) {
          console.log(error);
        });
  } else {
    message.warn("Hãy chọn đơn hàng!")
  }
}

const getNewInvoice = () => {
  axios.get('http://127.0.0.1:8000/invoice/new')
      .then(function (response) {
        invoices.value = response.data;
        for(let index = 0; index < invoices.value.length; index++)
        {
          invoices.value[index].creation_date = dayjs(invoices.value[index].creation_date).format('DD-MM-YYYY');
          invoices.value[index].status = parseInt(invoices.value[index].status);
        }
      })
      .catch(function (error) {
        console.log(error);
      });
};

getNewInvoice();

const open = ref(false);
const modalTitleRef = ref(null);
const showModal = () => {
  open.value = true;
};

const selectedRowKeys = ref([]);

const rowSelection = computed(() => ({
  selectedRowKeys: selectedRowKeys.value,
  onChange: (newSelectedRowKeys) => {
    selectedRowKeys.value = newSelectedRowKeys;
  },
}));
</script>

<template>
  <a-card title="Đơn hàng mới" style="width: 100%">
    <div class="row md-3">
      <div class="col-12 d-flex justify-content-start">
        <a-button type="primary" @click="editStatus(selectedRowKeys)">
          <span>Xác nhận đơn hàng</span>
        </a-button>
      </div>
    </div>
    <div class="row md-3">
      <div class="col-12">
        <a-table :dataSource="invoices"
                 :columns="columns"
                 :scroll="{ x: 576}"
                 :row-selection="rowSelection"
                  row-key="id">
          <template #bodyCell="{column, index, record}">
            <template v-if="column.key==='index'">
              <span>{{ index + 1 }}</span>
            </template>
            <template v-if="column.key==='action'">
              <a-button type="primary" @click="showModal" class="me-sm-2 mb-2">
                <font-awesome-icon :icon="['fas', 'info']" />
              </a-button>
              <a-modal ref="modalRef" v-model:open="open" :wrap-style="{ overflow: 'hidden' }" :footer="null" style="width: 70%">
                <ListProduct :id= "record.id"/>
                <template #title>
                  <div ref="modalTitleRef" style="width: 100%; cursor: move">Danh sách sản phẩm</div>
                </template>
              </a-modal>
            </template>
            <template v-if="column.key==='status'">
              <span>{{status[record.status - 1]}}</span>
            </template>
          </template>
        </a-table>
      </div>
    </div>
  </a-card>
</template>
