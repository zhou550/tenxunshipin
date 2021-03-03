<template>
  <div class="indexpage">
    <IndexNav></IndexNav>
    <IndexSlider :sliders="index_slider"></IndexSlider>
    <div style="display: flex;justify-content: center">
      <MovieList :col="6"/>
      <IndexRank rankname="电视剧排行榜" :indexitems="tv_rank"></IndexRank>
    </div>
  </div>
</template>

<script>
  import axios from "axios";
  import MovieList from "../components/MovieList";
  import Search from "../components/Search";
  import IndexRank from "../components/indexRank";
  import IndexSlider from "../components/IndexSlider";
  import IndexNav from "../components/IndexNav";

  export default {
    name: "IndexPage",
    data() {
      return {
        index_slider: [],
        tv_rank: [],
      }
    },
    components: {
      MovieList, Search, IndexRank, IndexSlider, IndexNav,
    },
    mounted() {
      // 发ajax请求进行搜索
      const url = `/index/items?type=index_slider`
      axios.get(url)
        .then(response => {
          // 成功了
          this.index_slider = response.data.data

        })
        .catch(error => {
          // 失败了
          console.log(error)
        })
      const url2 = `/index/items?type=tv_rank`
      axios.get(url2)
        .then(response => {
          // 成功了
          let list = response.data.data
          if (list.length > 8) {
            list = list.slice(0, 8)
          }
          this.tv_rank = list

        })
        .catch(error => {
          // 失败了
          console.log(error)
        })
    },
  }
</script>

<style lang="stylus">
  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
</style>
