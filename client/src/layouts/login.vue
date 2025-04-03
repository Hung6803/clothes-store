<script setup>

import TheHeader from "@/components/TheHeaderClient.vue";
import TheFooterClient from "@/components/TheFooterClient.vue";
</script>

<template>
  <TheHeader/>
  <div class="container-fluid mt-3">
    <router-view></router-view>
  </div>
  <TheFooterClient/>
</template>

<style scoped>

</style>