import VueRouter from 'vue-router'
import Home from './pages/Home.vue'
import LogInRegister from './pages/LogInRegister'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login-reg', component: LogInRegister, name: 'LogInRegister' }
]

export default new VueRouter({
  routes,
  mode: 'history'
})
