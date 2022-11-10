import Vue from 'vue'
import VueRouter from 'vue-router'
import LunchView from '../views/LunchView.vue'
import LottoView from '../views/LottoView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'lunch',
    component: LunchView
  },
  {
    path: '/lotto/:menu',
    name: 'lotto',
    component: LottoView
  },
  
 
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
