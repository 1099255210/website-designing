const test = { template: '<div>Home</div>' }

const routes = [
  { path: '/', component: () => import('../components/Home.vue') },
  { path: '/login', component: () => import('../components/Login.vue') },
  { path: '/register', component: () => import('../components/Register.vue') },
  { path: '/test', component: test},
]

const router = VueRouter.createRouter({
  routes
})

export default router