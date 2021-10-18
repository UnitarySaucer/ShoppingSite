<template>
  <div>
    <h1>Reviews</h1>
    <form @submit.prevent="handleSubmit()">
      <div>
        <h3>Write A Review</h3>
        <label>Title:</label>
        <input type="text" placeholder="Title" v-model="title" />
        <label>Content:</label>
        <input type="textarea" placeholder="Content" v-model="content" />
        <button type="submit">Submit</button>
      </div>
    </form>
    <div class="border" v-for="review in reviews" :key="review.id">
      <h3>{{review.title}}</h3>
      <p>{{review.content}}</p>
      <button type="submit" @click="deleteReview(review.id)">Delete</button>
      <form>
        <div>
          <label>Change Title:</label>
          <input type="text" placeholder="Update Title" v-model="updated_title" >
          <button type="submit" @click="deleteReview(review.id)">Update</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import {BASE_URL} from '../globals'
import axios from 'axios'
export default {
  name: "Product",
  data: () => ({
    reviews: [],
    title: '',
    content: '',
    updated_title: '',
    updated_content: '',
    product_id: null
  }),
  methods: {
    async getReviews(){
      const queryString = window.location.pathname
      const id = queryString.slice(-1)
      const res = await axios.get(`${BASE_URL}/api/products/${id}`)
      this.reviews = res.data.reviews
      this.product_id = parseInt(id)
    },
    async deleteReview(id){
      await axios.delete(`${BASE_URL}/api/reviews/${id}`)
      location.reload()
    },
    async handleSubmit(){
      await axios.post(`${BASE_URL}/api/reviews`,{
        title: this.title,
        content: this.content,
        product_id: this.product_id,
        user_id: localStorage.getItem('user')
      })
      location.reload()
      this.title = ''
      this.content = ''
    }
  },
  mounted:function(){
    this.getReviews()
  }
}
</script>

<style>
.border {
  border: 1px solid black;
  padding: 10px;
}
</style>