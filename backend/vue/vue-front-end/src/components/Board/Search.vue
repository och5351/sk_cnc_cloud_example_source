<template>
    <div class="wrap">
   <div class="search">
      <input 
      id="search_bar"
      type="text" 
      class="searchTerm" 
      @keyup="typing"
      placeholder="  검색어를 적어주세요.">
      <button type="submit" class="searchButton">
        <i class="fa fa-search"></i>
     </button>
   </div>
</div>
</template>

<script>
export default {
    data(){
        return{
            search_value: ""
        }
    },
    methods:{
        typing(){
            this.search_value = document.getElementById('search_bar').value;
            console.log(this.search_value)
        }
    },
}
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Open+Sans);

body {
  background: #f2f2f2;
  font-family: "Open Sans", sans-serif;
}

.search {
  width: 500px;
  height: 0px;
  position: relative;
  display: flex;
}

.searchTerm {
  width: 100%;
  border: 3px solid #212121;
  border-right: none;
  padding: 5px;
  height: 40px;
  border-radius: 5px 0 0 5px;
  outline: none;
  color: #9dbfaf;
}

.searchTerm:focus {
  color: #212121;
}

.searchButton {
  width: 40px;
  height: 40px;
  border: 1px solid #212121;
  background: #212121;
  text-align: center;
  color: #fff;
  border-radius: 0 5px 5px 0;
  cursor: pointer;
  font-size: 20px;
}

/*Resize the wrap to see the search bar change!*/
.wrap {
  width: 30%;
  height: 200px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

</style>