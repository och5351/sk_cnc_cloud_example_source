<template>
  <div id="app" class="container">
    <!--로그인-->
    <signInPage />
    <!-- 배너 부분 링크 문제 해결해야함 -->
    <div class="row">
      <!-- TODO: 리스트 CSS 수정 -->
      <!-- 공지사항 박스 -->
    </div>

    <!-- Footer -->
    <categoryFooter />
  </div>
</template>

<script>
/* eslint-disable */
import signInPage from "../components/Sign/login.vue";
import categoryFooter from "../components/Board/CategoryFooter.vue";

export default {
  data() {
    return {
      notice: Object,
      recent: Object,
      hot: Object,
      mySession: false
    };
  },
  components: {
    signInPage,
    categoryFooter
  },
  methods: {
    login: function() {
      this.$router.push({
        path: "/login",
        query: { redirect: this.$route.fullPath }
      });
    },
    // 로그아웃 시 세션 삭제 후 새로 고침
    logout: function() {
      this.$session.destroy();
      location.reload();
    },
    Mypage: function() {
      this.$router.push("/Mypage");
    }
  },
  mounted() {
    // Load notice / 공지사항 불러오기
    this.$http.get("/api/article/notice").then(res => {
      this.notice = res.data;
    });
    this.$http.get("/api/article/new").then(res => {
      this.recent = res.data;
    });
    this.$http.get("/api/article/hot").then(res => {
      this.hot = res.data;
    });
  }
};
</script>

<style scoped>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
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
  font-family: "Gill Sans", "Gill Sans MT", Calibri, "Trebuchet MS", sans-serif;
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
