<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {ref, createVNode} from "vue";
  import {ExclamationCircleOutlined} from "@ant-design/icons-vue";
  import {message, Modal} from 'ant-design-vue';
  import dayjs from "dayjs";

  useMenu().onSelectKeys(["admin-employee"])

  const employees = ref([]);

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
      title: 'Ngày bắt đầu làm',
      dataIndex: 'start_date',
      key: 'start_date',
    },
    {
      title: 'Lương',
      dataIndex: 'salary',
      key: 'salary',
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

  const deleteEmployee = (id) =>{
    axios.delete(`http://127.0.0.1:8000/employee/${id}`,{
    headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
      .then(function (response) {
        if (response.status === 200) {
          getEmployee();
          message.success("Xóa thành công!")
        }
      })
      .catch(function (error) {
        message.error("Không thể xóa nhân viên này!")
      })
  };

  const showConfirm = (id) => {
    Modal.confirm({
      title: 'Bạn chắc chắn muốn xóa nhân viên này?',
      icon: createVNode(ExclamationCircleOutlined),
      content: 'Nếu nhân viên đã bán được đơn hàng thì không thể xóa được!',
      onOk() {
        deleteEmployee(id)
      },
      onCancel() {},
    });
  };

  const getEmployee = () => {
    axios.get('http://127.0.0.1:8000/employee/')
      .then(function (response) {
        employees.value = response.data;
        employees.value[0].date_of_birth = dayjs(employees.value[0].date_of_birth).format('DD-MM-YYYY');
        employees.value[0].start_date = dayjs(employees.value[0].start_date).format('DD-MM-YYYY');
        employees.value[0].account.createDate = dayjs(employees.value[0].account.createDate).format('DD-MM-YYYY');
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  getEmployee();

</script>

<template>
  <a-card title="Nhân viên" style="width: 100%">
    <div class="row mb-3">
      <div class="col-12 d-flex justify-content-end">
        <a-button type="primary">
          <router-link :to="{name: 'admin-employee-create'}">
            <font-awesome-icon :icon="['fas', 'plus']" />
          </router-link>
        </a-button>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <a-table :dataSource="employees" :columns="columns" :scroll="{ x: 576}">
          <template #bodyCell="{column, index, record}">
            <template v-if="column.key==='index'">
              <span>{{ index + 1 }}</span>
            </template>
            <template v-if="column.key==='action'">
              <router-link :to="{ name: 'admin-employee-edit', params: { id: record.id }}" >
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