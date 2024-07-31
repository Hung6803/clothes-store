<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRoute, useRouter} from "vue-router";
  import {reactive, ref} from "vue"
  import dayjs from 'dayjs'

  useMenu().onSelectKeys(["admin-customer"])

  const router = useRouter();
  const route = useRoute();

  const customer = reactive({
    name: "",
    address: "",
    date_of_birth: "",
    phone_number: "",
  });

  let account_id = 0;

  const account = reactive({
    email: "",
    password: "",
  })

  const errors = ref([])
  const password_confirmation = reactive({
      password_confirmation: ""
    });

  const error_password = ref("")

  const checked = ref(false)

  const getCustomerbyID = () =>{
    axios.get(`http://127.0.0.1:8000/customer/${route.params.id}`)
    .then(function (response) {
      console.log(response.data);
      customer.name = response.data.name
      customer.address = response.data.address
      customer.date_of_birth = dayjs(response.data.date_of_birth)
      customer.phone_number = response.data.phone_number
      account_id = response.data.account.id
      account.email = response.data.account.email
    })
    .catch(function (error) {
      console.log(error);
    })
  };
  const editCustomerInfor = () => {
    axios.put(`http://127.0.0.1:8000/customer/edit/${route.params.id}`, customer, {
      headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}
    })
    .then(function (response) {
      if (response) {
        console.log(response)
        message.success("Cập nhật thông tin khách hàng thành công!");
        router.push({name: 'admin-customer'});
      }
    })
    .catch(function (error) {
      errors.value = error.response.data.detail;
    });
  }

  const editCustomer = () => {
    if (checked.value) {
      console.log(checked.value);
      if (account["password"] === password_confirmation["password_confirmation"]) {
        axios.put(`http://127.0.0.1:8000/account/edit/${account_id}`, account, {
          headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}
        })
            .then(function (response) {
              if (response) {

                console.log(checked.value)
              }
            })
            .catch(function (error) {
              console.log(error);
            });
        editCustomerInfor();
      } else {
        error_password.value = "Không trùng với mật khẩu!";
      }
    } else {
      editCustomerInfor();
    }
  };


  getCustomerbyID();

</script>

<template>
  <form @submit.prevent="editCustomer()">
    <a-card title="Cập nhật thông tin khách hàng" style="width: 100%">
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

        </div>
        <div class="col-12 col-sm-5">
          <a-checkbox v-model:checked="checked">Đổi thông tin tài khoản</a-checkbox>
        </div>
      </div>

      <div class="row mb-3" v-if="checked === true">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Email:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input placeholder="Email" allow-clear v-model:value="account.email"/>
        </div>
      </div>

      <div class="row mb-3" v-if="checked === true">
        <div class="col-12 col-sm-3 text-start text-sm-end">
          <label>
            <span class="text-danger me-1">*</span>
            <span>Mật khẩu:</span>
          </label>
        </div>
        <div class="col-12 col-sm-5">
          <a-input-password placeholder="Mật khẩu" allow-clear v-model:value="account.password"/>
        </div>
      </div>

      <div class="row mb-3" v-if="checked === true">
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
            <router-link :to="{name: 'admin-customer'}">
              <span>Hủy</span>
            </router-link>
          </a-button>
          <a-button type="primary" html-type="submit"><span>Lưu</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>

