import axios from 'axios';

const memberStore = {
    state: {
        userId: null,
        token: null
    },
    getters:{
        getToken(state){
            return state.token;
        },
        getUserId(state){
            return state.userId;
        },
    },
    mutations: {
        login(state, data){
            state.userId = data.userId;
            state.token = data.token;
        },
        init(state){
            state.userId = null;
            state.token = null;
        },
        tokenCheckMutate(state){
            state.userId = null;
            state.token = null;
        },
    },
    actions: {
        tokenCheck({commit},token){
            axios.post('/api/member/tokenCheck',{
                accessToken: token
            }).then(res => {
                if(!res.data){
                    console.log(res.data)
                    commit('tokenCheckMutate')
                }else{
                    console.log(res.data)
                }
            }).catch(error => {
          console.log(`Error : ${error}`);
        });
        }
    }
}

export default memberStore;