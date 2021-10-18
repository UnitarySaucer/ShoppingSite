import axios from 'axios'

export const BASE_URL = 'http://localhost:5000'

axios.defaults.headers.common['Authorization'] =
  'Bearer' + localStorage.getItem('token')
