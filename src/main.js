import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'


Vue.use(ElementUI)

Vue.config.productionTip = false

new Vue({
  router,    //ES6中router:router的简写
  render: h => h(App)
}).$mount('#app')
