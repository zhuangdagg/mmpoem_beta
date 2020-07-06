import Vue from 'vue'
import VueRouter from 'vue-router'
import home from '../views/home.vue'
import bxcp from '../views/bxcp.vue'
import search from '../views/search.vue'


Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'home',
    component: home
  },{
    path:'/bxcp',
    name:'bxcp',
    component:bxcp,
    children:[
      {
        path:'/search/:cm',
        name:'search',
        component:search,
        props:true,
      }]
    //     // 对于包含命名视图的路由，你必须分别为每个命名视图添加 `props` 选项：
    // {
    //   path: '/user/:id',
    //   components: { default: User, sidebar: Sidebar },
    //   props: { default: true, sidebar: false }
    // }

  }
 
]

const router = new VueRouter({
  routes
})

export default router
