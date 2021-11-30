/* eslint-disable */
import Vue from 'vue';
import VueRouter from 'vue-router';

// Components 분리
import login from '../components/Sign/login';
import SignUp from '../components/Sign/SignUp';

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
	// {
	// 	path: '/login',
	// 	name: 'login',
	// 	component: login,
	// },
	// {
	// 	path: '/signup',
	// 	name: 'SignUp',
	// 	component: SignUp,
	// },
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
