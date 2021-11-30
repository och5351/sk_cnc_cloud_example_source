<template>
<div class="login-wrap">
	<div class="login-html">
		<input id="tab-1" type="radio" name="tab" class="sign-in" checked><label for="tab-1" class="tab">Sign In</label>
		<input id="tab-2" type="radio" name="tab" class="sign-up"><label for="tab-2" class="tab">Sign Up</label>
		<div class="login-form">
			<div class="sign-in-htm">
				<div class="group">
          <br>
					<label for="signin_user" class="label">아이디</label>
					<input 
          id="signin_user" 
          type="text" 
          class="input" 
          v-model="user.userid" 
          placeholder="아이디를 입력해주세요.">
				</div>
				<div class="group">
          <br>
					<label for="signin_pass" class="label">비밀번호</label>
					<input id="signin_pass" type="password" class="input" v-model="user.password" placeholder="비밀번호를 입력해주세요." v-on:keydown.enter="login">
				</div>
				<div class="group">
          <br><br>
					<button class="button" v-on:click="login"> 로그인 </button>
				</div>
			</div>
			<div class="sign-up-htm">
				<div class="group">
					<label for="signup_user" class="label">아이디</label>
					<input 
          id="signup_user" 
          type="text" 
          class="input"
           v-model="signup_user.userid" 
          placeholder="아이디를 입력해주세요."><br>
          <button
            class="button"
            v-on:click="idCheck"
            id="idCheckClear"
          >
          중복 확인
        </button>
        <img
          src="../../assets/loginComponentIMG/check.png"
          id="idClear"
          style="width: 5%; visibility: hidden; position: relative;"
        />
				</div>
				<div class="group">
					<label for="signup_pass" class="label">비밀번호(영문,숫자,특수 문자 조합 4~15이내로 입력해주세요.)</label>
					<input 
          id="signup_pass" 
          name="upw"
          type="password" 
          class="input" 
          @keyup="pwCheck"
          data-type="password"
          v-model="signup_user.password" 
          placeholder="비밀번호를 입력해주세요.">
          
        <img
          src="../../assets/loginComponentIMG/check.png"
          id="pwClear"
          style="width: 5%; visibility: hidden; position: relative;"
        />
				</div>
				<div class="group">
					<label for="re_signup_pass" class="label">비밀번호 확인</label>
					<input id="re_signup_pass" 
           v-on:keydown.enter="signUp"
           type="password" 
           class="input"
           data-type="password"
           @keyup="repwCheck"
           placeholder="비밀번호를 다시 입력해주세요.">
        <span
          id="alert-success"
          style="display: none; font-weight: bold; color: blue"
          >비밀번호가 일치합니다.</span
        >
        <span id="alert-danger" style="display: none; font-weight: bold; color: red"
          >비밀번호가 일치하지 않습니다.</span
        >
				</div>
				<div class="group">
					<label for="signup_name_pass" class="label">이름</label>
					<input 
          id="signup_name_pass" 
          type="text" 
          class="input"
          v-model="signup_user.name"
          @keyup="nameCheck"
          placeholder="이름을 입력해주세요.">
          <img
          src="../../assets/loginComponentIMG/check.png"
          id="nameClear"
          style="width: 5%; visibility: hidden; position: relative;"
          />
          <input
            type="text"
            value="* 한글만 입력해 주세요."
            id="nameFalse"
            style="
              width: 100%;
              position: relative;
              visibility: visible;
              font-weight: bold;
            "
            disabled
          />
				</div>
				<div class="group">
					<button  class="button" v-on:click="signUp">회원가입</button>
				</div>
				<div class="hr"></div>
			</div>
		</div>
	</div>
</div>
</template>

<script>
import $ from "jquery";
export default {
  data() {
    return {
      redirect: this.$route.query.redirect,
      user: {
        userid: "",
        password: ""
      },
      signup_user: {
        userid: "",
        password: "",
        name: "",
      }
    };
  },
  mounted(){
    this.$store.dispatch('tokenCheck', this.$store.getters.getToken)
  },
  methods: {
    login() {
      this.$http
        .post("/api/member/signin", {
          id: this.user.userid,
          password: this.user.password
        })
        .then(res => {
          if(res.status === 200){
            if(res.data.accessToken == '자격 증명에 실패하였습니다.'){
              location.reload();
              alert("자격 증명에 실패하였습니다.");
            }else{
              this.$store.commit('login', {
              userId:this.user.userid,
              token:res.data.accessToken
              })
              console.log(this.$store.getters.getToken)
              this.$http.defaults.headers.common['x-access-token'] = res.data.accessToken;
              location.reload()
            }
            
          }else{
            alert("로그인에 실패하였습니다.\n 정보를 한번 더 확인 해 주세요.")
          }
        })
        .catch(error => {
          console.log(`Error : ${error}`);
        });
    },
    signUp() {
      var id = $("#idClear").css("visibility");
      var name = $("#nameClear").css("visibility");
      var pw = $("#pwClear").css("visibility");
      var aler = $("#alert-success").css("display");
      if (
        id === "visible" &&
        name === "visible" &&
        pw === "visible" &&
        aler === "inline-block"
      ) {
        this.$http
          .post("/api/member/signup", {
            id: this.signup_user.userid,
            name: this.signup_user.name,
            password: this.signup_user.password
          })
          .then(res => {
            if (res.data === true) {
              alert('회원가입을 성공하였습니다.');
              location.reload()
              // this.$router.push("/");
            }
            if (res.data === false) {
              alert('회원가입을 실패하였습니다.');
              this.$router.push("/signup");
            }
          });
      } else {
        alert("회원 정보를 다시 확인해주세요!");
      }
    },
    //아이디 확인 버튼
    idCheck() {
      var idReg = /^[A-Za-z]+[A-Za-z0-9]{3,15}$/g;
      // var idReg = /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
      if (!idReg.test($("input[name=uid]").val())) {
        alert(
          "이메일을 다시 한번 확인 해 주세요."
        );
      } else {
        this.$http
          .post("/api/member/idCheck", {
            id: this.signup_user.userid
          })
          .then(res => {
            if (res.data.success == false) {
              alert(res.data.message);
              $("#idClear").css("visibility", "visible");
              $("#idCheckClear").css("visibility", "hidden");
              $("#id")
                .attr("disabled", true)
                .attr("readonly", false);
            }
            if (res.data.success == true) {
              alert(res.data.message);
            }
          })
          .catch(error => console.log(error.response.data.message));
      }
    },
    //이름 확인
    nameCheck() {
      var regexp = /[a-z0-9]|[ [\]{}()<>?|`~!@#$%^&*-_+=,.;:'"\\]/g;
      var v = $("#signup_name_pass").val();
      if (regexp.test(v)) {
        alert("한글만 입력가능 합니다.");
        $("#nameClear").css("visibility", "hidden");
        $("#nameFalse").css("visibility", "visible");
        $("#name").val(v.replace(regexp, ""));
      } else {
        $("#nameClear").css("visibility", "visible");
        $("#nameFalse").css("visibility", "hidden");
      }
      if (v == "") {
        $("#nameClear").css("visibility", "hidden");
        $("#nameFalse").css("visibility", "visible");
      }
    },
    //비밀 번호 확인
    pwCheck() {
      var pwd1 = $("#signup_pass").val();
      var pwd2 = $("#re_signup_pass").val();
      var pwReg = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{4,15}$/;

      if (!pwReg.test($("input[name=upw]").val())) {
        $("#pwClear").css("visibility", "hidden");
        $("#pwFalse").css("visibility", "visible");
        return;
      } else {
        $("#pwClear").css("visibility", "visible");
        $("#pwFalse").css("visibility", "hidden");
      }
      if (pwd1 != "" && pwd2 == "") {
        null;
      } else if (pwd1 != "" || pwd2 != "") {
        if (pwd1 == pwd2) {
          $("#alert-success").css("display", "inline-block");
          $("#alert-danger").css("display", "none");
        } else {
          $("#alert-success").css("display", "none");
          $("#alert-danger").css("display", "inline-block");
        }
      }
    },
    //비밀 번호 재확인
    repwCheck() {
      var pwd1 = $("#signup_pass").val();
      var pwd2 = $("#re_signup_pass").val();

      if (pwd1 != "" && pwd2 == "") {
        null;
      } else if (pwd1 != "" || pwd2 != "") {
        if (pwd1 == pwd2) {
          $("#alert-success").css("display", "inline-block");
          $("#alert-danger").css("display", "none");
        } else {
          $("#alert-success").css("display", "none");
          $("#alert-danger").css("display", "inline-block");
        }
      }
    }
  }
};
</script>

<style scoped>

@import '../../assets/scss/components/login.css';
/* .login {
  margin-top: 40px;
  text-align: center;
}

.tag {
  position: relative;
  margin-left: -210px;
  margin-bottom: 5px;
  font-size: 15px;
  color: black;
}

input {
  margin: 0px 0;
  width: 22%;
  padding: 15px;
}

button {
  margin-top: 10px;
  width: 10%;
  cursor: pointer;
  background-color: white;
  border: 0px;
  height: 0px;
}

p {
  margin-top: 40px;
  font-size: 15px;
  color: #248657;
}

p a {
  text-decoration: underline;
  cursor: pointer;
  color: #df0174;
} */
</style>
