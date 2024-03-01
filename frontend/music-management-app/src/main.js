import { createApp } from 'vue'
import './style.css'
import { plugin, defaultConfig } from '@formkit/vue'
import config from './formkit.config'
import App from './App.vue'
import router from './router';


createApp(App).use(router).use(plugin, defaultConfig(config)).mount('#app')
