<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRouter} from "vue-router";
  import {ref, reactive} from "vue";

  useMenu().onSelectKeys(["admin-employee"])

  const router = useRouter();

  const employee = reactive({
    name: "",
    phone_number: "",
    address: "",
    date_of_birth: "",
    start_date: "",
    salary: undefined,
    email: "",
    password: "",
  });

  const errors = ref("")
  const password_confirmation = reactive({
      password_confirmation: ""
    });

  const error_password = ref("")

  const createEmployee = () =>{
    if(employee["password"] === password_confirmation["password_confirmation"]){
      axios.post("http://127.0.0.1:8000/employee/create", employee,{
      headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
      .then(function (response) {
        if (response) {
          message.success("Tạo mới thành công!");
          router.push({name: 'admin-employee'});
        }
      })
      .catch(function (error) {
        errors.value = error.response.data.detail;
      });
    } else {
      error_password.value = "Không trùng với mật khẩu!";
    }
  };

</script>

<template>
  <form @submit.prevent="createEmployee()">
    <a-card title="Thêm nhân viên mới mới" style="width: 100%">
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Họ và tên:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input placeholder="Họ và tên" allow-clear v-model:value="employee.name"/>
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Ngày sinh:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-date-picker v-model:value="employee.date_of_birth" style="width: 100%" placeholder="Ngày sinh"/>
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Ngày bắt đầu làm:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-date-picker v-model:value="employee.start_date" style="width: 100%" placeholder="Ngày bắt đầu làm"/>
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Tiền lương:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input-number
            style="width: 100%"
            placeholder="Tiền lương"
            v-model:value="employee.salary"
            addon-after="VND"></a-input-number>
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Số điện thoại:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input placeholder="Số điện thoại" allow-clear v-model:value="employee.phone_number"/>
        </div>
      </div>

      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Địa chỉ:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-textarea v-model:value="employee.address" placeholder="Địa chỉ" :rows="3" />
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Email:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input placeholder="Email" allow-clear v-model:value="employee.email"/>
          <div class="w-100"></div>
          <small class="text-danger">{{errors}}</small>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Mật khẩu:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input-password placeholder="Mật khẩu" allow-clear v-model:value="employee.password"/>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Xác nhận mật khẩu:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input-password placeholder="Xác nhận mật khẩu" allow-clear v-model:value="password_confirmation.password_confirmation"/>
          <div class="w-100"></div>
          <small class="text-danger">{{error_password}}</small>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-8 d-sm-flex justify-content-center">
          <a-button class="me-2">
            <router-link :to="{name: 'admin-employee'}">
              <span>Hủy</span>
            </router-link>
          </a-button>
          <a-button type="primary" html-type="submit"><span>Thêm mới</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>
