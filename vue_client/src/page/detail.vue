<template>
  <div id="detail">
    <div class="detailContainer" style="padding: 10px">
      <div class="poster_wrap">
        <img class="poster_pic" :src="poster">
      </div>
      <div class="video_title">
        <span class="gray1 title"> {{fanhao.title}}</span>
      </div>
      <div class="actressWrap">
        <div class="actressList">
          <div class="actressItem" v-for="(actress, index) in actresses" :key="index">
            <Actress :actress="actress"></Actress>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import Actress from '@/components/Actress'

  export default {
    name: 'detail',
    components: {Actress},
    data () {
      return {
        poster:"",
        detailImages:[],
        fanhao: {},
        actresses: [],
        tags:[]
      }
    },
    methods: {

      // 用JS获取地址栏参数的方法（超级简单）
      getQueryString: function (name) {
        var reg = new RegExp('(^|&)' + name + '=([^&]*)(&|$)')
        var r = window.location.search.substr(1).match(reg)
        //search,查询？后面的参数，并匹配正则
        if (r != null) {
          return decodeURIComponent(r[2])
        }
        return null
      },
    },
      mounted () {
        // 发ajax请求进行搜索
        let url = `/api/fanhao/`
        url+=this.getQueryString("n")
        axios.get(url)
          .then(response => {
            console.log(response)
            if(response.data.success==1){
              let data=response.data.data;
              // 成功了
              this.fanhao =data.fanhao;
              this.actresses=data.actresses;
              this.tags=data.tags;
              this.poster=data.poster;
              this.detailImages=data.detailImages;
            }


          })
          .catch(error => {
            // 失败了
            console.log(2)
            console.log(response)
            console.log(error)
          })
      },
    }
</script>
<style>
  .detailContainer {
    display: grid;
    grid-template-columns: [left] 400px [info] repeat(3, 1fr) [right];
    grid-template-rows: [top] 40px repeat(3, 20px) [actress] 120px [bottom];
    border-top: 1px solid #eee;
    border-bottom: 1px solid #eee;
    background: #f8f8f8;
  }
  .poster_wrap {
    grid-row-start: top;
    grid-row-end: bottom;
  }
  .actressWrap {
    grid-row: actress;
    grid-column: 2/right;
  }

  .video_title {
    grid-row: 1;
    grid-column: info/right;
  }

  .poster_pic {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  .gray1 {
    color: #111;
  }
  .title {
    font-size: 28px;
    font-weight: 400;
    line-height: 34px;
  }
</style>
