<template>
  <div id="app">
    <div class="box">
      <Products/>
    </div>
  </div>
</template>

<script>
import Products from '../components/Products.vue'

export default {
  name: 'Home',
  components: {
    Products
  }
}
</script>

<style>
.box {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}
</style>
