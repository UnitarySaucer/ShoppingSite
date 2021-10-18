import VueRouter from 'vue-router'
import Home from './pages/Home.vue'
import LogInRegister from './pages/LogInRegister'
import Product from './pages/Product'

const routes = [
  { path: '/', component: Home, name: 'Home' },
  { path: '/login-reg', component: LogInRegister, name: 'LogInRegister' },
  { path: '/product/:id', component: Product, name: 'Product' }
]

export default new VueRouter({
  routes,
  mode: 'history'
})
