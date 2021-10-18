<template>
  <div>
    <LogIn />
    <Register />
  </div>
</template>

<script>
import LogIn from '../components/LogIn.vue'
import Register from '../components/Register.vue'
export default {
  name: "LogInRegister",
  components: {
    LogIn,
    Register
  }
}
</script>

<style>

</style>