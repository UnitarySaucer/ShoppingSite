<template>
  <div id="app">
    <NavBar/>
    <Products/>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
import Products from './components/Products.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    Products
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: 'Josefin Sans', sans-serif;
  font-weight: 400;
}
</style>
