<template>
<div id="app">
    <SearchBar />
    <MenuBar />
</div>
</template>

<script>
import SearchBar from '../components/Board/Search.vue'
import MenuBar from '../components/Board/Menu.vue'
export default {
	data() {
		return {
			mySession: false,
		};
	},
    components:{
        SearchBar,
        MenuBar
    },
};
</script>

<style scoped>
@import '../assets/scss/view/Main.css';
/* #app {
	font-family: 'Avenir', Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #42b983;
	margin-top: 10px;
	margin-right: 10px;
	margin-left: 0px;
	margin-bottom: 150px;
}
#banner {
	margin-top: 10px;
}

#notice {
	font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
	margin-top: 10px;
	padding: 7px;
	height: 250px;
	align-self: auto;
	white-space: nowrap;
	overflow: hidden;
	text-overflow: ellipsis;
}
#first_line {
	margin-bottom: 30px;
}

.footer {
	margin-top: 60px;
	color: black;
}

.loginbutton {
	margin-top: 10px;
	width: 250px;
	height: 70px;
}

.trueLogin {
	width: 50px;
	vertical-align: middle;
	float: right;
}

.hottopic {
	margin-top: 20px;
	margin-bottom: 20px;
}

.ad {
	margin-top: 10px;
	height: 250px;
} */
</style>
