<script setup>
  import {reactive, ref} from "vue";
  import {useCartStore} from "@/store/use-cart-client.js";

  const provinces = ref([]);
  const districts = ref();
  const wards = ref();
  const products = useCartStore();

  const address = reactive({
    province: { code: "", name: "" },
    district: { code: "", name: "" },
    ward: { code: "", name: "" },
  });

  const customer = reactive({
    name: "",
    phone_number: "",
    address: "",
  });

  const invoice = reactive({
    total_price: products.totalPrice,
    payment_type: "",
    address: "",
    status: 1,
    employee_id: 2,
    customer_id: undefined,
  });

  const createCustomer = () =>{
    customer.address = customer.address + ", " + address.ward.name + ", " + address.district.name + ", " + address.province.name;
     axios.post("http://127.0.0.1:8000/customer/createnoaccount", customer)
    .then(function (response) {
      createInvoice(response.data.id);
    })
    .catch(function (error) {
      console.log(error);
    });
  };

  const createInvoice = (customer_id) =>{
    invoice.address = customer.address;
    invoice.customer_id = customer_id;
    invoice.payment_type = "Trực tiếp"
    axios.post("http://127.0.0.1:8000/invoice/create", invoice)
    .then(function (response) {
      createInvoiceDetail()
    })
    .catch(function (error) {
      console.log(error);
    });
  };

  const createInvoiceDetail = () =>{
    console.log(products.selectedProducts);
    products.selectedProducts.forEach(product => {
      axios.post("http://127.0.0.1:8000/invoice_details/add", invoice)
      .then(function (response) {
        createInvoiceDetail()
      })
      .catch(function (error) {
        console.log(error);
      });
    })
  }
  const submitForm = () => {
    customer.address = customer.address + ", " + address.ward.name + ", " + address.district.name + ", " + address.province.name;
    console.log('Customer data:', customer);
    alert('Form submitted successfully!');
  };

  const getProvinces = () => {
    axios.get('https://vn-public-apis.fpo.vn/provinces/getAll?limit=-1')
      .then(function (response) {
        provinces.value = response.data.data.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const getDistricts = (code) => {
    axios.get(`https://vn-public-apis.fpo.vn/districts/getByProvince?provinceCode=${code}&limit=-1`)
      .then(function (response) {
        districts.value = response.data.data.data;
        address.district = { code: "", name: "" };
        wards.value = [];
        address.ward = { code: "", name: "" };
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const getWards = (code) => {
    axios.get(`https://vn-public-apis.fpo.vn/wards/getByDistrict?districtCode=${code}&limit=-1`)
      .then(function (response) {
        wards.value = response.data.data.data;
        address.ward = { code: "", name: "" };
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  getProvinces();

</script>

<template>
  <main>
    <section class="breadcrumb-area breadcrumb-bg">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="breadcrumb-content">
              <h2>Thông tin đơn hàng</h2>
              <nav aria-label="breadcrumb">
                <ol class="breadcrumb">
                  <li class="breadcrumb-item"><a><router-link :to="{ name: 'public-homepage' }">Trang chủ</router-link></a></li>
                  <li class="breadcrumb-item active" aria-current="page">Đặt hàng</li>
                </ol>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- breadcrumb-area-end -->

    <!-- checkout-area -->
    <section class="checkout-area pt-95 pb-95">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-7">
            <div class="checkout-wrap">
              <div class="checkout-top">
                <h5 class="title">Thông tin đơn hàng</h5>
                <a href="" class="back"><router-link :to="{ name: 'public-cart' }">
                  <font-awesome-icon :icon="['fas', 'arrow-left']" />  Giỏ hàng
                </router-link></a>
              </div>
              <form class="checkout-form">
                <div class="row">
                  <div class="col-12">
                    <div class="form-grp">
                      <label for="fName">HỌ VÀ TÊN<span>*</span></label>
                      <input type="text" v-model="customer.name">
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="form-grp">
                      <label for="address">ĐỊA CHỈ <span>*</span></label>
                      <input type="text" v-model="customer.address">
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="form-grp">
                      <label>TỈNH/ THÀNH PHỐ <span>*</span></label>
                      <select v-model="address.province" class="custom-select" @change="getDistricts(address.province.code)">
                        <option value=""> Chọn tỉnh/thành phố </option>
                        <option v-for="province in provinces" :value="{ code: province.code, name: province.name }">
                          {{ province.name }}
                        </option>
                      </select>
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="form-grp">
                      <label>QUẬN/ HUYỆN <span>*</span></label>
                      <select v-model="address.district" class="custom-select" @change="getWards(address.district.code)">
                        <option value=""> Chọn quận/huyện </option>
                        <option v-for="district in districts" :value="{ code: district.code, name: district.name }">
                          {{ district.name }}
                        </option>
                      </select>
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="form-grp">
                      <label>XÃ/ THỊ TRẤN <span>*</span></label>
                      <select v-model="address.ward" class="custom-select">
                        <option value=""> Chọn xã/thị trấn </option>
                        <option v-for="ward in wards" :value="{ code: ward.code, name: ward.name }">
                          {{ ward.name }}
                        </option>
                      </select>
                    </div>
                  </div>
                  <div class="col-12">
                    <div class="form-grp">
                      <label for="phone">SỐ ĐIỆN THOẠI <span>*</span></label>
                      <input type="text" v-model="customer.phone_number">
                    </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
          <div class="col-lg-5 col-md-8">
            <aside class="checkout-sidebar">
              <h6 class="title">THÔNG TIN GIỎ HÀNG</h6>
              <div class="shop-cart-widget">
                <form @submit.prevent="createCustomer">
                  <ul>
                    <li class="sub-total"><span>TỔNG HÓA ĐƠN</span> {{invoice.total_price}}.000 VND</li>
                  </ul>
                  <div class="payment-method-info">
                    <div class="paypal-method-flex">
                      <div class="custom-control custom-checkbox">
                        <input type="checkbox" class="custom-control-input" id="customCheck5">
                        <label class="custom-control-label" for="customCheck5">Thanh toán khi nhận hàng</label>
                      </div>
                    </div>
                    <div class="paypal-method-flex">
                      <div class="custom-control custom-checkbox">
                        <input type="checkbox" class="custom-control-input" id="customCheck6">
                        <label class="custom-control-label" for="customCheck6">Thanh toán qua ví MoMo</label>
                      </div>
                    </div>
                  </div>
                  <button type="submit" class="btn">Đặt hàng</button>
                </form>
              </div>
            </aside>
          </div>
        </div>
      </div>
    </section>
    <!-- checkout-area-end -->
  </main>
</template>

<style scoped>
  .breadcrumb-bg {
    background-image: url('@/assets/img/slider/third_slider_bg.jpg');
  }
</style>