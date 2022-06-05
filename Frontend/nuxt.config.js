import axios from 'axios'

export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
      // Main title of web
      title: 'Truckers:',


      // Inject meta tags
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      ]
  },

  // Router link config
  router: {
    prefetchLinks: false,
  },


  // Axios module configuration: https://go.nuxtjs.dev/config-axios
  axios: {
    // URL to backend APIs
    baseURL: ''
  },

  // Static config
  static: {
    prefix: false
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    '~/assets/main.sass',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [

  ],

  // Auto import components by folder: https://go.nuxtjs.dev/config-components
  components: true,

    // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // Modules to fetch https://go.nuxtjs.dev/axios
    '@nuxtjs/axios',
  ],

  server: {
    host: process.env.NUXT_HOST || 'localhost',
    port: process.env.NODE_ENV === 'production' ? process.env.PORT : 80,
  },
}
