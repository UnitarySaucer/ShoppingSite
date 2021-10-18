<template>
    <form class="login" @submit.prevent="handleSubmit">
      <div>
        <h3>Log In</h3>
        <label>Username:</label>
        <input type="text" placeholder="Username" v-model="username" />
        <label>Password:</label>
        <input type="password" placeholder="Password" v-model="password" />
        <button type="submit">Log In</button>
      </div>
    </form>
</template>

<script>
import {BASE_URL} from '../globals'
import axios from 'axios'

export default {
  name: "LogIn",
  data: () => ({
    username: '',
    password: ''
  }),
  methods: {
    async handleSubmit(){
      const res = await axios.post(`${BASE_URL}/auth/login`,{
        username: this.username,
        password: this.password
      })
      localStorage.setItem('token', res.data.token)
      localStorage.setItem('user', res.data.user.id)
      console.log(res)
      this.username = ''
      this.password = ''
    }
  }
}
</script>

<style>

</style>