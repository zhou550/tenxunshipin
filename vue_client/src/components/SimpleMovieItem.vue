<template>
  <div class="itembox">
    <div class="list_item ">
      <a :href="link" target="_blank" class="figure">
        <img @mouseenter="handleEnter(true)" class="figure_pic posterHalf" onerror="picerr(this,'v')"
             :src="movie.poster" style="visibility: visible;">
        <!---->
        <div class="figure_score">{{movie.score}}</div>
        <!---->
        <img class="mark_v mark_v_VIP" src="//puui.qpic.cn/vupload/0/20190716_sub_poster_vip.png/0">
      </a>
      <div class="figure_detail figure_detail_two_row  ">
        <a :href="link" target="_blank" class="figure_title figure_title_two_row bold">{{movie.title}}</a>
        <div class="figure_desc" :title="movie.title">{{movie.sub_title}}</div>
      </div>
    </div>

  </div>
</template>

<script>
    export default {
        name: "SimpleMovieItem",
        props: ['movie'],
    }
</script>

<style scoped>

  .itembox {
    position: relative;
  }

  .list_item {
    width: 183px;

    margin: 0 18px 40px 0;
    padding: 0;
    color: #999;
    font-size: 12px;
    letter-spacing: normal;
    vertical-align: top;
  }

  .figure {
    width: 183px;
    height: 257px;
    display: block;
    position: relative;
    margin-bottom: 14px;
    border-radius: 4px;
  }

  .figure_title {
    font-size: 14px;
  }

  .figure_pic {
    -o-object-fit: cover;
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 4px;
    background: #f8f8f8;
    background-color: #ececec;
    background-color: rgba(236, 236, 236, .1);
  }

  .mark_v {
    position: absolute;
    top: 5px;
    right: 5px;
    pointer-events: none;
  }

  .figure_score {
    position: absolute;
    right: 2px;
    bottom: 0;
    width: 35px;
    height: 28px;
    color: #fff;
    color: #ff5c38;
    font-size: 0;
    font-size: 17px;
    font-weight: 400;
    line-height: 28px;
    text-align: center;
  }

  a {
    text-decoration: none;
    cursor: pointer;
    color: #111;
  }

  a:hover {
    color: #ff5c38;
  }

  .bold {
    font-weight: 700;
    letter-spacing: 0;
  }

  .figure_desc {
    display: block;
    width: 100%;
    margin-top: 3px;
    overflow: hidden;
    font-size: 13px;
    line-height: 20px;
    text-overflow: ellipsis;
    white-space: nowrap;
    cursor: default;
  }

  .figure_detail_two_row {
    height: 44px;
    overflow: hidden;
  }
</style>
