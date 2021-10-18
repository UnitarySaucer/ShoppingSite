<template>
    <form class="login" @submit.prevent="handleSubmit">
      <div>
        <h3>Register</h3>
        <label>Username:</label>
        <input type="text" placeholder="Username" v-model="username" />
        <label>Email:</label>
        <input type="email" placeholder="Email" v-model="email" />
        <label>Password:</label>
        <input type="password" placeholder="Password" v-model="password" />
        <button type="submit">Register</button>
      </div>
    </form>
</template>

<script>
import {BASE_URL} from '../globals'
import axios from 'axios'

export default {
  name: "Register",
  data: () => ({
    username: '',
    email: '',
    password: ''
  }),
  methods: {
    async handleSubmit(){
      await axios.post(`${BASE_URL}/auth/register`,{
        username: this.username,
        email: this.email,
        password: this.password
      })
      this.username = ''
      this.email = ''
      this.password = ''
    }
  }
}
</script>

<style>

</style>