/* eslint-disable */
<template>
  <div id="app" class="container">
    <div class="logo">
      <img
        @click="main"
        style="width: 200px; height: 200px"
        alt="Vue logo"
        src="./assets/skcnclogo.jpg"
      />
    </div>
    <router-view :key="$route.fullPath"></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
  methods: {
    main: function() {
      this.$router.push("/");
    },
    board(category) {
      this.$router.push(`/board/${category}`);
    },
    AdminMenu(menu) {
      this.$router.push(`/admin/${menu}`);
    }
  },
  data() {
    return {
      /*로그인 세션 정보를 받아와서 로그인을 할지 닉네임을 표시할지 선택*/
      mySession: false
    };
  },
  watch: {}
};
</script>

<style scoped>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #42b983;
  margin-top: 60px;
  margin-right: 150px;
  margin-left: 150px;
}
.loginbox {
  width: 150px;
  vertical-align: middle;
  float: right;
}
.trueLogin {
  width: 50px;
  vertical-align: middle;
  float: right;
}
.link,
.logo {
  cursor: pointer;
}
</style>
