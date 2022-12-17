import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DocView from '../views/DocView.vue'
import CommunityView from '../views/CommunityView.vue'
import GifgenView from '../views/GifgenView.vue'
import LoginView from '../views/LoginView.vue'
import MyassetsView from '../views/MyassetsView.vue'
import MydesignView from '../views/MydesignView.vue'
import MyfavouriteView from '../views/MyfavouriteView.vue'
import PostergenView from '../views/PostergenView.vue'
import RegistView from '../views/RegistView.vue'
import TestView from '../views/TestView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/doc',
      name: 'doc',
      component: DocView
    },
    {
      path: '/community',
      name: 'community',
      component: CommunityView
    },
    {
      path: '/gifgen',
      name: 'gifgen',
      component: GifgenView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/myassets',
      name: 'myassets',
      component: MyassetsView
    },
    {
      path: '/mydesign',
      name: 'mydesign',
      component: MydesignView
    },
    {
      path: '/myfavourite',
      name: 'myfavourite',
      component: MyfavouriteView
    },
    {
      path: '/postergen',
      name: 'postergen',
      component: PostergenView 
    },
    {
      path: '/regist',
      name: 'regist',
      component: RegistView 
    },
    {
      path: '/test',
      name: 'test',
      component: TestView
    }
  ]
})

export default router
