<template>
	<div id="app" class="container">
		<!-- 배너 부분 링크 문제 해결해야함 -->
		<div class="row">
			<div class="col-md-9">
				<div class="hottopic">
					<div class="tabs" variant="secondary">
						<b-card no-body>
							<b-tabs pills card>
								<b-tab title="인기글" active
									><b-card-text>
										<div :key="item.post_id" v-for="item in hot">
											<b-link v-bind:href="'/article/' + item.post_id">{{ item.title }}</b-link> <br />
										</div> </b-card-text
								></b-tab>
								<b-tab title="최신글"
									><b-card-text>
										<div :key="item.post_id" v-for="item in recent">
											<b-link v-bind:href="'/article/' + item.post_id">{{ item.title }}</b-link> <br />
										</div> </b-card-text
								></b-tab>
							</b-tabs>
						</b-card>
					</div>
				</div>
            </div>
			<!-- 로그인 박스 -->
			<div class="col-md-3">
					{{ this.$store.getters.getUserId }}님 환영 합니다!
					<button v-on:click="Mypage">마이페이지</button>
					<button v-on:click="logout">로그아웃</button>
				<!-- TODO: 리스트 CSS 수정 -->
				<!-- 공지사항 박스 -->
				<div class="border" id="notice">
					<label>공지사항</label><br />
					<div :key="item.post_id" v-for="item in notice">
						<b-link v-bind:href="'/article/' + item.post_id">{{ item.title }}</b-link> <br />
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	data() {
		return {
			notice: Object,
			recent: Object,
			hot: Object,
			mySession: false,
		};
	},
	methods: {
		logout() {
            console.log(this.$store.getters.getUserId);
			if(confirm("로그아웃 하시겠습니까?")){
                this.$store.commit('init')
            }
		},
		Mypage: function () {
			this.$router.push('/Mypage');
		},
	},
	mounted() {
		this.$store.dispatch('tokenCheck', this.$store.getters.getToken)
	},
};
</script>

<style scoped>
#app {
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
}
</style>
