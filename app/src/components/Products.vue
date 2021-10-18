<template>
  <div class="product-box">
    <div class="product" v-for="product in products" :key="product.id" >
      <p>{{product.name}}</p>
      <p>${{product.price}}</p>
    </div>
  </div>
</template>

<script>
import {BASE_URL} from '../globals'
import axios from 'axios'
export default {
  name: 'Products',
  data: () =>({
    products: []
  }),
  methods: {
    async getProducts(){
      const res = await axios.get(`${BASE_URL}/api/products`)
      console.log(res.data)
      this.products = res.data
    }
  },
  mounted:function(){
    this.getProducts()
  }
}
</script>

<style>
.product-box {
  width: 111.188rem;
  height: 53.063rem;
  background-color: #C4C4C4;
}

.product {
  padding: 2rem;
}

</style>