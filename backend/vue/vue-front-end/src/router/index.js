/* eslint-disable */
import Vue from 'vue';
import VueRouter from 'vue-router';

/* Components */

Vue.use(VueRouter);

const routes = [
	{
		path: '/',
		name: 'Home',
		component: function () {
			return import('../views/Home.vue');
		},
	},
	{
		path: '/article/:contentId',
		name: 'Article',
		component: function () {
			return import('../views/Article.vue');
		},
	},
	{
		path: '/Mypage',
		name: 'Mypage',
		component: function () {
			return import('../views/Mypage.vue');
		},
	},

];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
