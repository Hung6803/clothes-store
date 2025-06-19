<script setup>
  import {reactive, ref} from "vue";
  import {useCartStore} from "@/store/use-cart-client.js";

  const provinces = ref([]);
  const districts = ref([]);
  const wards = ref([]);
  const products = useCartStore();
  const payment_method = ref('cod');

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

  const createCustomer = () => {
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
    invoice.payment_type = payment_method.value;
    console.log(invoice);
    axios.post("http://127.0.0.1:8000/invoice/create", invoice)
    .then(function (response) {
      createInvoiceDetail(response.data.id)
    })
    .catch(function (error) {
      console.log(error);
    });
  };

  const createInvoiceDetail = (invoice_id) =>{
    products.selectedProducts.forEach(product => {
      const add_product = reactive({
        product_id: product.id,
        size_id: product.size_id,
        invoice_id: invoice_id,
        quantity: product.quantity,
        discount: product.discount,
        price: product.price,
      });
      axios.post("http://127.0.0.1:8000/invoice_details/add", add_product)
      .then(function (response) {

      })
      .catch(function (error) {
        console.log(error);
      });
    })
    if (payment_method.value === "cod") {

    }
  }

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
                <h5 class="title">Thông tin người nhận</h5>
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
                      <div class="w-100"></div>
                      <small class="text-danger"></small>
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
                      <label for="address">ĐỊA CHỈ <span>*</span></label>
                      <input type="text" v-model="customer.address">
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
              <h6 class="title">THÔNG TIN ĐƠN HÀNG</h6>
              <div class="shop-cart-widget">
                <form @submit.prevent="createCustomer">
                  <ul>
                    <li class="sub-total"><span>TỔNG HÓA ĐƠN</span> {{invoice.total_price}}.000 VND</li>
                  </ul>
                  <div class="payment-method-info">
                    <div class="paypal-method-flex">
                      <div class="custom-control custom-radio">
                        <input
                          type="radio"
                          class="custom-radio-input"
                          id="radio-cod"
                          value="cod"
                          v-model="payment_method"
                        >
                        <label class="custom-radio-label" for="radio-cod">
                          Thanh toán khi nhận hàng
                        </label>
                      </div>
                    </div>

                    <div class="paypal-method-flex">
                      <div class="custom-control custom-radio">
                        <input
                          type="radio"
                          class="custom-radio-input"
                          id="radio-momo"
                          value="momo"
                          v-model="payment_method"
                        >
                        <label class="custom-radio-label" for="radio-momo">
                          Thanh toán qua ví MoMo
                        </label>
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

  .custom-radio {
    position: relative;
    padding-left: 2rem;
    cursor: pointer;
    display: flex;
    align-items: center;
  }

  .custom-radio-input {
    position: absolute;
    opacity: 0;
    cursor: pointer;
    left: 0;
    z-index: -1;
    width: 1rem;
    height: 1.25rem;
  }

  .custom-radio-label{
    text-transform: capitalize;
    color: #544842;
    font-family: 'Jost', sans-serif;
    font-size: 14px;
    font-weight: 500;
  }

  .custom-radio-label::after {
    content: "";
    position: absolute;
    left: 0;
    top: 50%;
    transform: translateY(-50%);
    width: 1rem;
    height: 1rem;
    border: 2px solid #676565;
    border-radius: 50%;
    background-color: white;
    transition: background-color 0.3s, border-color 0.3s;
    box-sizing: border-box;
  }

  .custom-radio-input:checked + .custom-radio-label::before {
    content: "";
    position: absolute;
    left: 0.25rem;
    top: 50%;
    transform: translateY(-50%);
    width: 0.5rem;
    height: 0.5rem;
    background-color: white;
    border-radius: 50%;
    z-index: 2;
  }

  .custom-radio-input:checked + .custom-radio-label::after {
    background-color: #ff5400;
    border-color: #ff5400;
  }
</style>