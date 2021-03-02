<template>
  <div class="muti_select">
    <div class="list_filter">
      <div class="filter_result none">共<span class="resultcount"  >{{resultcount}}</span>个筛选结果
      </div>
      <div class="filter_line ">
        <span class="filter_label">地区</span>
        <div v-for="(value,key) in regions" :key="key"  @click="region=key"  :class="{current:key==region}" class="filter_item ">{{value}}</div>
      </div>
      <div class="filter_line ">
        <span class="filter_label">年份</span>
        <div v-for="(value,key) in years" :key="key" @click="year=key"  :class="{current:key==year}"  class="filter_item ">{{value}}</div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "MultipleSelect",
    data() {
      return {
        regions: {
          "all": "全部",
          "china": "内地",
          "hk": "中国香港",
          "us": "美国",
          "europe": "欧洲",
          "taiwan": "中国台湾",
          "japan": "日本",
          "korea": "韩国",
          "india": "印度",
          "other": "其它"
        },
        years: {
          "all": "全部",
          "y2021": "2021",
          "y2020": "2020",
          "y2019": "2019",
          "y2018": "2018",
          "y2017": "2017",
          "y2016": "2016",
          "y2015": "2015",
          "y2014": "2014",
          "y2011-2013": "2013-2011",
          "y2006-2010": "2010-2006",
          "other": "其它",
        },
        resultcount: 0,
        region: "all",
        year: "all",
      }
    },
  }
</script>

<style lang="stylus">
  .muti_select
    z-index: 2;
    position: relative;
    width: 1710px;
    margin: 0 auto;

    .list_filter
      position: relative;
      margin: 0 0 40px;
      padding: 1px 26px;
      border-radius: 4px;
      background-color: #f8f8f8;
      font-size: 13px;

      .filter_result
        position: absolute;
        top: 26px;
        right: 26px;
        line-height: 32px;
        .resultcount
          color #ff5c38

      .filter_line
        position: relative;
        margin: 26px 0;
        padding-left: 90px;

        .filter_label
          position: absolute;
          top: 0;
          left: 0;
          min-width: 50px;
          margin-right: 20px;
          padding: 0 5px;
          border-radius: 16px 0 16px 16px;
          background-color: #7f7f8c;
          color: #fff;
          line-height: 32px;
          text-align: center;


        .filter_item
          display: inline-block;
          margin: 2px 0;
          padding: 0 10px;
          border-radius: 15px;
          color: #999;
          line-height: 28px;
          vertical-align: top;

          &:hover
            color: #ff5c38;
            /*用css 添加手状样式,鼠标移上去变小手,变小手*/
            cursor: pointer;

          &.current
            position: relative;
            background-color: #f7eae8;
            color: #ff5c38;
            font-weight: 700;


</style>
