import { createApp } from 'vue'
import App from './App.vue'
import YMAP_SETTINGS from './js/common.js'
import FirstTask from "./components/FirstTask.vue"
import SecondTask from "./components/SecondTask.vue"
import indexOne from "./components/indexOne.vue"
import {createRouter, createWebHashHistory} from 'vue-router'
import BootstrapVue3 from 'bootstrap-vue-3'

// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'


const app = createApp(App);

const YmapPlugin =  require('vue-yandex-maps');
app.use(YmapPlugin, YMAP_SETTINGS)
// Make BootstrapVue available throughout your project
app.use(BootstrapVue3)

const routes = [
  { path: '/', component: indexOne },
  { path: '/task1', component: FirstTask },
  { path: '/task2', component: SecondTask },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes: routes, // short for `routes: routes`
})


app.use(router)
app.mount('#app')
