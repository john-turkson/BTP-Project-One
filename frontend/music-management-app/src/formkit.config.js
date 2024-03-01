import { en } from '@formkit/i18n'
import { defaultConfig } from '@formkit/vue'
import { rootClasses } from '../formkit.theme.mjs'

export default defaultConfig({
  locales: { en },
  locale: 'en',
  config: {
    rootClasses,
  },
})