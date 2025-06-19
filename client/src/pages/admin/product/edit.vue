<script setup>
  import {useMenu} from "@/store/use-menu-admin.js";
  import {message} from 'ant-design-vue';
  import {useRoute, useRouter} from "vue-router";
  import {reactive, ref} from "vue"

  useMenu().onSelectKeys(["admin-product"])

  const router = useRouter();
  const route = useRoute();

  const product = reactive({
    product_name: "",
    product_description: "",
    price: undefined,
    discount: undefined,
    category_id: undefined,
    brand_id: undefined,
  });

  const baseURL = "http://127.0.0.1:8000/image/";
  const previewVisible = ref(false);
  const previewImage = ref('');
  const previewTitle = ref('');
  const fileList = ref([]);

  const brands = ref([]);
  const categories = ref([]);

  const getProductbyID = () =>{
    axios.get(`http://127.0.0.1:8000/product/${route.params.id}`)
    .then(function (response) {
      product.product_name = response.data.product_name
      product.product_description = response.data.product_description
      product.brand_id = response.data.brand.id
      product.category_id = response.data.category.id
      product.price = response.data.price
      product.discount = response.data.discount
      fileList.value = response.data.product_image.map((image, index) => ({
        uid: `${index}`,
        name: image.image_path,
        status: "done",
        url: `${baseURL}${image.image_path}`,
      }));
    })
    .catch(function (error) {
      console.log(error);
    })
  };

  const editProduct = () =>{
    axios.put(`http://127.0.0.1:8000/product/edit/${route.params.id}`, product,{
    headers: {Authorization: `Bearer ${localStorage.getItem('token')}`}})
    .then(function (response) {
      if (response) {
        editFile(response.data.id)
      }
    })
    .catch(function (error) {
      console.log(error);
    });
  };

  getProductbyID();

  const getBrand = () => {
    axios.get('http://127.0.0.1:8000/brand/')
      .then(function (response) {
        brands.value = response.data;
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const getCategory = () => {
    axios.get('http://127.0.0.1:8000/category/')
    .then(function (response) {
      categories.value = response.data;
    })
    .catch(function (error) {
      console.log(error);
    });
  };

  getCategory();
  getBrand();

  function getBase64(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result);
      reader.onerror = error => reject(error);
    });
  }

  const beforeUpload = (file) => {
    return false
  };

  const handleChange = (info) => {
    if (info.fileList.length > 6) {
      info.fileList = info.fileList.slice(-6)
    }
    fileList.value = [...info.fileList]
  };

  const handleCancel = () => {
    previewVisible.value = false;
    previewTitle.value = '';
  };

  const handlePreview = async (file) => {
    if (!file.url && !file.preview) {
      file.preview = await getBase64(file.originFileObj);
    }
    previewImage.value = file.url || file.preview;
    previewVisible.value = true;
    previewTitle.value = file.name || file.url.substring(file.url.lastIndexOf('/') + 1);
  };

  const editFile = async () => {
    const formData = new FormData();

    fileList.value.forEach((file) => {
      if (!file.originFileObj) {
        formData.append('old_image', file.name);
      }
      else {
        formData.append('request', file.originFileObj);
      }
    });

    axios.put(`http://localhost:8000/image/edit/${route.params.id}`, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
        Authorization: `Bearer ${localStorage.getItem('token')}`
      },
    })
    .then(function (response){
      if (response) {
        message.success("Sửa thông tin thành công!");
        router.push({name: 'admin-product'});
      }
    })
    .catch(function (error) {
      console.error('Error uploading image:', error)
    })
  }
</script>

<template>
  <form @submit.prevent="editProduct()">
    <a-card title="Sửa thông tin sản phẩm" style="width: 100%">
      <div class="row mb-3">
        <div class="col-12 col-sm-4">
          <div class="row">
            <div class="col-12 d-flex justify-content-center">
              <a-upload list-type="picture-card"
                :fileList="fileList"
                :beforeUpload="beforeUpload"
                @change="handleChange"
                @preview="handlePreview"
                accept="image/*"
                multiple
                :maxCount="6"
              >
                <div v-if="fileList.length < 6">
                  <font-awesome-icon :icon="['fas', 'plus']" />
                  <div style="margin-top: 8px">Upload</div>
                </div>
              </a-upload>
              <a-modal :open="previewVisible" :title="previewTitle" :footer="null" @cancel="handleCancel">
                <img alt="example" style="width: 100%" :src="previewImage" />
              </a-modal>
            </div>
          </div>
        </div>
        <div class="col-12 col-sm-8">
          <div class="row mb-3">
            <div class="col-12 col-sm-3 text-start text-sm-end">
              <label>
                <span class="text-danger me-1">*</span>
                <span>Tên sản phẩm:</span>
              </label>
            </div>
            <div class="col-12 col-sm-5">
              <a-input placeholder="Tên sản phẩm" allow-clear v-model:value="product.product_name"/>
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-12 col-sm-3 text-start text-sm-end">
              <label>
                <span class="text-danger me-1">*</span>
                <span>Thương hiệu:</span>
              </label>
            </div>
            <div class="col-12 col-sm-5">
              <a-select
                ref="select"
                v-model:value="product.brand_id"
                placeholder="Thương hiệu"
                style="width: 100%"
                :options="brands"
                :field-names="{label: 'brand_name', value: 'id'}"
              ></a-select>
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-12 col-sm-3 text-start text-sm-end">
              <label>
                <span class="text-danger me-1">*</span>
                <span>Kiểu dáng:</span>
              </label>
            </div>
            <div class="col-12 col-sm-5">
              <a-select
                ref="select"
                v-model:value="product.category_id"
                placeholder="Kiểu dáng"
                style="width: 100%"
                :options="categories"
                :field-names="{label: 'category_name', value: 'id'}"
              ></a-select>
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-12 col-sm-3 text-start text-sm-end">
              <label>
                <span class="text-danger me-1">*</span>
                <span>Giá bán:</span>
              </label>
            </div>
            <div class="col-12 col-sm-5">
              <a-input-number
                  style="width: 100%"
                  placeholder="Giá bán"
                  v-model:value="product.price"
                  addon-after="VND"></a-input-number>
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-12 col-sm-3 text-start text-sm-end">
              <label>
                <span class="text-danger me-1">*</span>
                <span>Giảm giá:</span>
              </label>
            </div>
            <div class="col-12 col-sm-5">
              <a-input-number
                v-model:value="product.discount"
                :min="0"
                :max="100"
                :formatter="value => `${value}%`"
                :parser="value => value.replace('%', '')"
              />
            </div>
          </div>
          <div class="row mb-3">
            <div class="col-12 col-sm-3 text-start text-sm-end">
              <label>
                <span>Mô tả sản phẩm:</span>
              </label>
            </div>
            <div class="col-12 col-sm-5">
              <a-textarea v-model:value="product.product_description" placeholder="Mô tả sản phẩm" :rows="4" />
            </div>
          </div>
        </div>
      </div>
      <div class="row mb-3">
        <div class="col-12 col-sm-8 d-sm-flex justify-content-center">
          <a-button class="me-2">
            <router-link :to="{name: 'admin-product'}">
              <span>Hủy</span>
            </router-link>
          </a-button>
          <a-button type="primary" html-type="submit"><span>Lưu</span></a-button>
        </div>
      </div>
    </a-card>
  </form>
</template>

