import Vue from 'vue'
import VueRouter from 'vue-router'
import IndexView from '../views/IndexView.vue'
import CreateView from '../views/CreateView.vue'
import DetailView from '../views/DetailView.vue'
import NotFound404 from '../views/NotFound404.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
  {// 숫자가 앞에 나오는 path라서 앞 숫자까지 만족하면 detail이 실행돼버리니까 위로 올려줌
    path: '404-not-found',
    name: 'NotFound404',
    component: NotFound404,
  },
  {// 동적 라우팅 변수  
    path: '/:id',
    name: 'detail',
    component: DetailView
  },
  {// 위에서 존재하지 않는 주소일때!
    path: '*',
    redirect: { name: 'NotFound404'},
  }
  
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
