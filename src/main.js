import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { plugin, defaultConfig } from '@formkit/vue'
import '@formkit/themes/genesis'
import { createPinia } from 'pinia'
import { fabric } from 'fabric'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
// import VueColor from ''

loadFonts()

const app = createApp(App)
const pinia = createPinia()

app.use(router)
app.use(pinia)
app.use(fabric)
app.use(vuetify)
app.use(plugin, defaultConfig)

app.mount('#app')

