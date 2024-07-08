
<template>
  <TheHeader/>

  <div class="container-fluid mt-3">
    <div class="row">
      <div class="col-sm-2 d-none d-sm-flex">
        <TheMenu/>
      </div>

      <div class="col-sm-10 col-12">
        <router-view></router-view>
      </div>
    </div>
  </div>

</template>

<script>
  import TheHeader from "../components/TheHeaderAdmin.vue";
  import TheMenu from "../components/TheMenuAdmin.vue";
  export default {
    components: {
      TheHeader,
      TheMenu
    }
  }
</script>
