/* eslint-disable */
import Vue from 'vue';
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex);

import memberStore from './modules/memberStore'

export default new Vuex.Store({
	modules: {
		memberStore: memberStore,
	},
	plugins: [createPersistedState({ 
		paths: ["memberStore"] 
	})]
})

