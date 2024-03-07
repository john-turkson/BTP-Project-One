import { createApp } from 'vue'
import './style.css'
import { plugin, defaultConfig } from '@formkit/vue'
import config from './formkit.config'
import App from './App.vue'
import router from './router';
import { Field, Form, defineRule, configure } from 'vee-validate';
import { required, min, confirmed } from '@vee-validate/rules';
import { localize } from '@vee-validate/i18n';

defineRule('required', required);
defineRule('min', min);
defineRule('confirmed', confirmed);

configure({
  generateMessage: localize({
    en: {
      messages: {
        required: 'This field is required',
        min: 'This field must have at least {length} characters',
        confirmed: 'The confirmation does not match',
      }
    }
  })
});


createApp(App).use(router).use(plugin, defaultConfig(config)).component('Form', Form).component('Field', Field).mount('#app')
