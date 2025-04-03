<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {ref, createVNode} from "vue";
  import {ExclamationCircleOutlined} from "@ant-design/icons-vue";
  import {message, Modal} from 'ant-design-vue';
  import dayjs from "dayjs";

  useMenu().onSelectKeys(["admin-customer"])

  const customers = ref([]);

  const columns = [
    {
      title: 'STT',
      key: 'index',
    },
    {
      title: 'Họ và tên',
      dataIndex: 'name',
      key: 'name',
    },
    {
      title: 'Địa chỉ',
      dataIndex: 'address',
      key: 'address',
    },
    {
      title: 'Ngày sinh',
      dataIndex: 'date_of_birth',
      key: 'date_of_birth',
    },
    {
      title: 'Số điện thoại',
      dataIndex: 'phone_number',
      key: 'phone_number',
    },
    {
      title: 'Email',
      dataIndex: ['account', 'email'],
      key: 'email',
    },
    {
      title: 'Ngày tạo',
      dataIndex: ['account', 'createDate'],
      key: 'email',
    },
    {
      title: 'Công cụ',
      key: 'action',
      fixed: 'right',
    },
  ];

  const deleteCustomer = (id) =>{
    axios.delete(`http://127.0.0.1:8000/customer/${id}`,{
    headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
        .then(function (response) {
          if (response.status === 200) {
            getCustomer();
            message.success("Xóa thành công!")
          }
        })
        .catch(function (error) {
          message.error("Khách hàng đã mua hàng!")
        })
  };

  const showConfirm = (id) => {
    Modal.confirm({
      title: 'Bạn chắc chắn muốn xóa khách hàng này?',
      icon: createVNode(ExclamationCircleOutlined),
      content: 'Nếu khách hàng đã mua hàng của cửa hàng thì không thể xóa được!',
      onOk() {
        deleteCustomer(id)
      },
      onCancel() {},
    });
  };

  const getCustomer = () => {
    axios.get('http://127.0.0.1:8000/customer/')
      .then(function (response) {
        customers.value = response.data;
        for(let index = 0; index < customers.value.length; index++)
        {
          customers.value[index].date_of_birth = dayjs(customers.value[index].date_of_birth).format('DD-MM-YYYY');
          customers.value[index].account.createDate = dayjs(customers.value[index].account.createDate).format('DD-MM-YYYY');
        }
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  getCustomer();

</script>

<template>
  <a-card title="Khách hàng" style="width: 100%">
    <div class="row mb-3">
      <div class="col-12 d-flex justify-content-end">
        <a-button type="primary">
          <router-link :to="{name: 'admin-customer-create'}">
            <font-awesome-icon :icon="['fas', 'plus']" />
          </router-link>
        </a-button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <a-table :dataSource="customers" :columns="columns" :scroll="{ x: 576}">
          <template #bodyCell="{column, index, record}">
            <template v-if="column.key==='index'">
              <span>{{ index + 1 }}</span>
            </template>
            <template v-if="column.key==='action'">
              <router-link :to="{ name: 'admin-customer-edit', params: { id: record.id }}" >
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