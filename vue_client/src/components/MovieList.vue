<template>
  <div class="movieList">

    <el-row>
      <el-row type="flex"  justify="space-between">
        <el-col :span="4">
          <h2 class="mod_title"><a href="#">
            电影
          </a></h2>
        </el-col>
        <el-col :span="4" >
          <div class="mod_page_small">
            <button class="btn_prev" :class="{'disabled':curPage==1}" @click="prePage">
              <i class="el-icon-arrow-left"></i>
            </button>
            <span class="page_num" >{{curPage}}/{{pages}}</span>
            <button class="btn_next" :class="{'disabled':curPage==pages}"  @click="nextPage">
              <i class="el-icon-arrow-right"></i>
            </button>
          </div>
        </el-col>

      </el-row>
    </el-row>

    <el-row :gutter="10" v-show="curPage==n" v-for="n in pages" >
      <el-col :span="Math.floor(24/col)" v-for="(movie, index) in getCurPage(n)" :key="index">
        <MovieItem :movie="movie"/>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import MovieItem from './MovieItem.vue'
  import axios from 'axios'

  export default {
    name: 'MovieList',
    data () {
      return {
        movies: [],
        row:2,
        curPage:1
      }
    },
    props: ['col'],

    computed :{
      pages:function () {
        var row = 2
        var num = Math.ceil(this.movies.length / (row * this.col));
        return num;
      }
    },
    components: {MovieItem},
    mounted () {
      // 发ajax请求进行搜索

      const url = `/api/lastmovies/31`
      axios.get(url)
        .then(response => {
          console.log(1)
          console.log(response)
          // 成功了
          this.movies = response.data

        })
        .catch(error => {
          // 失败了
          console.log(2)
          console.log(response)
          console.log(error)
        })
    },
    methods:{
      getCurPage:function (n) {
        var start=(n-1)*(this.row*this.col);
        var fend=start+this.row*this.col;
        var end=fend>this.movies.length?this.movies.length:fend;
        console.log(start+" "+end)
        return this.movies.slice(start,end);
      },
      prePage:function () {
        if(this.curPage>1){
          this.curPage--;
        }

      },
      nextPage:function () {
        if(this.curPage<this.pages){
          this.curPage++;
        }
      }
    }

  }
</script>

<style scoped>
.movieList{
  padding: 5px 20px;
}

  a {
    text-decoration: none;
    cursor: pointer;
    color: #111;
  }

  a:active, a:hover {
    color: #ff5c38;
  }

  .mod_title {
    height: 40px;
    margin: 0 10px 20px 0;
    color: #111;
    font-size: 30px;
    font-weight: 400;
    line-height: 40px;
    vertical-align: top;
    white-space: nowrap;
  }


  .mod_page_small {
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    position: absolute;
    top: 0;
    right: 0;
    background-color: #fff;
    font-size: 0;
    user-select: none;
  }




  button{
    border: 0;
    background-color: transparent;
   cursor: pointer;
    box-sizing: content-box;
    outline: 0 none;
    padding: 0;
  }
  .mod_page_small .disabled {
     color: #ccc;
   }
  .mod_page_small .btn_next:hover, .mod_page_small .btn_prev:hover {
    background-color: #f8f8f8;
    color: #ff5c38;
  }
  .mod_page_small .page_num {
     display: inline-block;
     min-width: 20px;
     margin: 0 15px;
     color: #666;
     font-size: 14px;
     letter-spacing: 2px;
     line-height: 30px;
     text-align: center;
     vertical-align: top;
   }
  .mod_page_small .btn_next, .mod_page_small .btn_prev {
      display: inline-block;
      width: 30px;
      height: 30px;
      border-radius: 100%;
      color: #666;
      text-align: center;
      vertical-align: top;
    }
  .mod_page_small .disabled {
    color: #ccc;
  }
</style>
