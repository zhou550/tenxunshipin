import Vue from 'vue'
import detail from './detail.vue'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#detail',
  render: h => h(detail)
})
