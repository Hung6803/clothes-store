<template>
  <li>
    <div class="sidebar-product-thumb">
      <router-link :to="{ name: 'public-shop-product', params: { id: product.id }}">
            <img :width="79" :height="86" :src="`http://127.0.0.1:8000/image/${product.product_image.image_path}`" alt="">
      </router-link>
    </div>
    <div class="sidebar-product-content">
      <h5>
        <router-link :to="{ name: 'public-shop-product', params: { id: product.id }}">
          {{ product.product_name }}
        </router-link>
      </h5>
      <span v-if="product.discount === 0">{{ product.price }}.000 VND</span>
      <span v-if="product.discount !== 0">{{ product.price * (1 - product.discount / 100) }}.000 VND</span>
    </div>
  </li>
</template>

<script setup>
  import { defineProps } from 'vue'

  const props = defineProps({
    product: {
      type: Object,
      required: true,
    },
  })
</script>