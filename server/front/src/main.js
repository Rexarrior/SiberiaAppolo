import { createApp } from 'vue'
import App from './App.vue'
import YMAP_SETTINGS from './js/common.js'
const app = createApp(App);
app.mount('#app')

const YmapPlugin =  require('vue-yandex-maps');
app.use(YmapPlugin, YMAP_SETTINGS)
