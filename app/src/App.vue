<template>
  <div>
    <NavBar/>
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'
// import Home from './pages/Home.vue'
// import LogInRegister from './pages/LogInRegister.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    // Home,
    // LogInRegister
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
