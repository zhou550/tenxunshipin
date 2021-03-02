<template>
  <div class="infiniteScrollVideoList">
    <div class="scrolllist" >
      <SimpleMovieItem v-for="movie in movies" :movie="movie"  class="item" ></SimpleMovieItem>
    </div>
    <div v-show="nonewdata" class="nomore">
      <div class="mod_status_box_inner">没有更多数据了</div>
    </div>
    <div v-show="!nonewdata" class="loadmore">
    <el-button @click="load" type="success" >加载更多……</el-button>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import SimpleMovieItem from "./SimpleMovieItem";

  export default {
    name: "InfiniteScrollVideoList",
    data() {
      return {
        movies: [],
        count: 0,
        offset: 0,
        nonewdata: false,
      }
    },
    components: {SimpleMovieItem},
    methods: {
      getVideos() {
        // 发ajax请求进行搜索
        console.log(this.offset)
        let url = "/video/list?offset=" + this.offset + "&pagesize=30"
        axios.get(url)
          .then(response => {
            // 成功了
            let newVideos = response.data.data;
            if (newVideos.length == 0) {
              this.nonewdata = true;
              return;
            }
            for (var i = 0; i < newVideos.length; i++) {
              this.movies.push(newVideos[i])
            }
            this.offset += newVideos.length;

          })
          .catch(error => {
            // 失败了
            console.log(error)
          })
      },

      load() {
        console.log("load")
        this.getVideos();
      },
    }
  }
</script>

<style lang="stylus">
  .scrolllist
    width 100%
    display flex
    flex-wrap wrap
    .item
      width 200px
  .nomore
    margin: 50px 0;
    color: #666;
    text-align: center;
    padding: 0;
  .loadmore
    display flex
    justify-content center


</style>
