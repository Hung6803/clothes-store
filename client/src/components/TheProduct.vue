<template>
    <div class="new-arrival-item text-center mb-50">
      <div class="thumb mb-25">
        <div class="discount-tag" v-if="product.discount !== 0">- {{ product.discount }}%</div>
        <router-link :to="{ name: 'public-shop-product', params: { id: product.id }}">
          <img :width="296" :height="344" :src="`http://127.0.0.1:8000/image/${product.product_image.image_path}`" alt="">
        </router-link>
      </div>
      <div class="content">
        <h5><router-link :to="{ name: 'public-shop-product', params: { id: product.id } }">{{ product.product_name }}</router-link></h5>
        <span class="price" v-if="product.discount === 0">{{ product.price }}.000 VND</span>
        <span class="del-price" v-if="product.discount !== 0">{{ product.price }}.000 VND</span>
        <span class="price" v-if="product.discount !== 0">{{ product.price * (1 - product.discount / 100) }}.000 VND</span>
      </div>
    </div>

</template>

<style scoped>
.del-price{
  text-decoration: line-through;
  color: #676565;
  display: block;
  font-size: 14px;
  font-weight: 600;
  font-family: 'Jost', sans-serif;
}
</style>

<script setup>
  import { defineProps } from 'vue'

  const props = defineProps({
    product: {
      type: Object,
      required: true,
    },
  })
</script>