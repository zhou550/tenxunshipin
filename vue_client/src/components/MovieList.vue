<template>
  <div class="movieList">
    <div class="listhead">
      <h2 class="mod_title"><a href="#">
        电影
      </a></h2>
      <div class="mod_page_small">
        <button class="btn_prev" :class="{'disabled':curPage==1}" @click="prePage">
          <i class="el-icon-arrow-left"></i>
        </button>
        <span class="page_num">{{curPage}}/{{pages}}</span>
        <button class="btn_next" :class="{'disabled':curPage==pages}" @click="nextPage">
          <i class="el-icon-arrow-right"></i>
        </button>
      </div>
    </div>
    <div class="itemswrap">
      <MovieItem v-for="(movie, index) in getCurPage()" :key="index" :movie="movie"/>
    </div>

  </div>
</template>

<script>
  import MovieItem from './MovieItem.vue'
  import axios from 'axios'

  export default {
    name: 'MovieList',
    data() {
      return {
        movies: [],
        row: 2,
        curPage: 1,
        curitem: 0
      }
    },
    props: ['col'],

    computed: {
      pages: function () {
        var row = 2
        var num = Math.ceil(this.movies.length / (row * this.col));
        return num;
      }
    },
    components: {MovieItem},
    mounted() {
      // 发ajax请求进行搜索
      const url = `/video/list?offset=0&pagesize=30`
      axios.get(url)
        .then(response => {
          // 成功了
          this.movies = response.data.data
        })
        .catch(error => {
          // 失败了
          console.log(error)
        })
    },
    methods: {
      getCurPage: function () {
        var fend = this.curitem + this.row * this.col;
        var end = fend > this.movies.length ? this.movies.length : fend;
        return this.movies.slice(this.curitem, end);
      },
      prePage: function () {
        if (this.curPage > 1) {
          this.curPage--;
          this.curitem=this.curitem-this.row * this.col
          if(this.curitem<0){
            this.curitem=0;
          }
        }

      },
      nextPage: function () {
        if (this.curPage < this.pages) {
          this.curPage++;
          this.curitem=this.curitem+this.row * this.col
          if(this.curitem>this.movies.length-this.row * this.col){
            this.curitem=this.movies.length-this.row * this.col;
          }
        }
      }
    }

  }
</script>

<style lang="stylus">
  .movieList
    display flex
    flex-direction column
    padding: 5px 20px
    width 1314px
    height 770px
    .listhead
      display flex
      justify-content space-between
      padding 0 10px

    .itemswrap
      display: grid;
      grid-template-columns: repeat(6, 198px)
      grid-template-rows: repeat(2, 335px)
      justify-items: center;
      align-items: center;
      justify-content:space-between;
      align-content:space-between;



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

    background-color: #fff;
    font-size: 0;
    user-select: none;
  }


  button {
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
