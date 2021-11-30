import Vue from 'vue';
import Vuex from 'vuex';
import App from './App.vue';
import router from './router';
import http from 'axios';
import BootstrapVue from 'bootstrap-vue';
import moment from 'moment';
import VueMomentJS from 'vue-momentjs';
import VueSession from 'vue-session';
import store from './store/store';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

Vue.use(VueSession, [{ persist: true }]);
Vue.use(BootstrapVue);
Vue.use(VueMomentJS, moment);
Vue.use(Vuex);
http.defaults.xsrfCookieName = 'csrftoken'
http.defaults.xsrfHeaderName = 'X-CSRFToken'
Vue.config.productionTip = false;
Vue.prototype.$http = http;

new Vue({
	router,
	store,
	render: v => v(App),
}).$mount('#app');
