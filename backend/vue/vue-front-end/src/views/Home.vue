<template>
  <div id="app" class="container">
    <div id="main">
    <!--로그인-->
      <div v-if="this.$store.getters.getToken==null">
        <signInPage />
      </div>
      <div v-else>
      <!--메인 페이지-->
        <mainPage />
      </div>
    </div>
    <!-- Footer -->
    <categoryFooter />
  </div>
</template>

<script>
/* eslint-disable */
import signInPage from "../components/Sign/login.vue";
import categoryFooter from "../components/Board/CategoryFooter.vue";
import mainPage from './Main.vue'

export default {
  data() {
    return {
      mySession: false,
    };
  },
  components: {
    signInPage,
    categoryFooter,
    mainPage,
  },
  methods() {

  },
  mounted() {
    console.log(this.$store.getters.getToken);
    this.$store.dispatch('tokenCheck', this.$store.getters.getToken)
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

.footer {
  margin-top: 100px;
  color: black;
}

</style>
