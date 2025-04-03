<script setup>
  import {message} from 'ant-design-vue';
  import {useRouter} from "vue-router";
  import {ref, reactive} from "vue";

  const router = useRouter();

  const customer = reactive({
    name: "",
    phone_number: "",
    address: "",
    date_of_birth: "",
    email: "",
    password: "",
  });

  const error_email = ref("")
  const password_confirmation = reactive({
      password_confirmation: ""
    });

  const error_password = ref("")

  const createCustomer = () =>{
    if(customer["password"] === password_confirmation["password_confirmation"]){
      axios.post("http://127.0.0.1:8000/customer/create", customer,{
      headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
      .then(function (response) {
        if (response) {
          message.success("Tạo mới thành công!");
          router.push({name: 'login'});
        }
      })
      .catch(function (error) {
        error_email.value = error.response.data.detail;
      });
    } else {
      error_password.value = "Không trùng với mật khẩu!";
    }

  };

</script>

<template>
  <div class="register-container">
    <form @submit.prevent="createCustomer()" class="register-form">
      <a-card title="Đăng ký" style="width: 100%">
        <div class="row mb-3">
          <div class="col-12 col-sm-3 text-start text-sm-end">
            <label>
              <span class="text-danger me-1">*</span>
              <span>Họ và tên:</span>
            </label>
          </div>
          <div class="col-12 col-sm-5">
            <a-input placeholder="Họ và tên" allow-clear v-model:value="customer.name"/>
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
            <a-date-picker v-model:value="customer.date_of_birth" style="width: 100%" placeholder="Ngày sinh"/>
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
            <a-input placeholder="Số điện thoại" allow-clear v-model:value="customer.phone_number"/>
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
            <a-textarea v-model:value="customer.address" placeholder="Địa chỉ" :rows="3" />
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
            <a-input placeholder="Email" allow-clear v-model:value="customer.email"/>
            <div class="w-100"></div>
            <small class="text-danger">{{error_email}}</small>
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
            <a-input-password placeholder="Mật khẩu" allow-clear v-model:value="customer.password"/>
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
              <router-link :to="{name: 'login'}">
                <span>Hủy</span>
              </router-link>
            </a-button>
            <a-button type="primary" html-type="submit"><span>Tạo tài khoản</span></a-button>
          </div>
        </div>
      </a-card>
    </form>
  </div>
</template>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 25px;
}

.register-form {
  width: 50%;
}
</style>
