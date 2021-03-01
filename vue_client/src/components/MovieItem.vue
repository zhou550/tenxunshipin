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

    <div class="x_layer_card" v-show="isShow" @mouseleave="handleEnter(false)">
      <div class="x_layer_card_bd" style="width: 232px; left: -28px; top: 0px;">
        <div class="x_layer_card_video">
          <div class="figure_video_pic" style="height: 168px; width: 232px;">
            <img :src="movie.poster" style="object-fit: cover">
          </div>
          <div class="video_content no_honor">
            <div class="video_title"><a class="tit" :href="link" target="_blank">{{movie.fanhao}}</a></div>
            <div class="video_tags" title=" 动作 武侠 张子文 马牧萱 刘承俊 刘权友"><span class="tag">动作</span><span
              class="tag">武侠</span><span class="tag">张子文</span><span class="tag">马牧萱</span><span
              class="tag">刘承俊</span><span
              class="tag">刘权友</span></div>
            <div class="video_sum"><span class="tit">简介: </span><span class="txt">东京都内发生了三起杀人事件。警方从所有案发现场都遗留有的无法解释的数列推断出这是一系列带有预告信息的连环杀人案，并就此展开了侦查然</span>
            </div>
            <div class="video_play"><a href="https://v.qq.com/x/cover/mzc002009r3bfun.html" target="_blank"
                                       class="btn_play"
                                       _float_click="play">立即观看</a><span class="video_btn"><a href="javascript:;"
                                                                                              class="z_figure_collect _follow"><i
              class="icon_sm icon_collect_sm" title="收藏"></i><i class="icon_sm icon_collected_sm"
                                                                title="取消收藏"></i></a><a
              href="javascript:;" class="z_figure_dl _down" data-clipboard-text="qqlivechannel=channel1.vfloat"><i
              class="icon_sm icon_dl_sm" title="用客户端下载视频"></i></a></span></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'MovieItem',
    data() {
      return {
        isShow: false
      }
    },
    computed: {
      link: function () {
        return "detail.html?n=" + this.movie.fanhao;
      }
    },
    props: ['movie'],
    methods: {
      handleEnter(isEnter) {
        if (isEnter) { // 进入
          this.isShow = true
        } else { // 离开
          this.isShow = false
        }
      },
    }
  }
</script>

<style scoped>

  .posterHalf {
    object-position: 104% 50%;
  }

  .x_layer_card_bd {
    -webkit-user-select: none;
    -ms-user-select: none;
    -moz-user-select: none;
    display: block;
    visibility: visible;
    z-index: 14;
    position: absolute;
    width: 238px;
    overflow: hidden;
    border-radius: 4px;
    background: #fff;
    box-shadow: 0 28px 50px rgba(25, 24, 40, .35);
    opacity: 1;
    transition: opacity .1s ease, -webkit-transform .1s ease;
    transition: opacity .1s ease, transform .1s ease;
    transition: opacity .1s ease, transform .1s ease, -webkit-transform .1s ease;
    user-select: none;
  }

  .x_layer_card_bd.ani_x_layer_card_hover {
    -webkit-animation: ani_x_layer_card_hover .2s ease backwards;
    display: block;
    visibility: visible;
    animation: ani_x_layer_card_hover .2s ease backwards;
    opacity: 1;
    will-change: transform;
    will-change: opacity
  }

  .x_layer_card * {
    margin: 0;
    padding: 0
  }

  .x_layer_card .none, .x_layer_card.none {
    display: none
  }

  .x_layer_card .x_layer_card_video {
    zoom: 1
  }

  .x_layer_card .figure_video.none, .x_layer_card .figure_video_outlink.none, .x_layer_card .figure_video_pic.none {
    display: none
  }

  .x_layer_card .figure_video_outlink, .x_layer_card .figure_video_pic {
    *zoom: 1;
    display: block;
    position: relative;
    width: 100%;
    height: 179px;
    overflow: hidden;
    background: #fff
  }

  .x_layer_card .figure_video, .x_layer_card .figure_video img {
    width: 100%;
    height: 100%
  }

  .x_layer_card .figure_video_pic .figure {
    position: absolute;
    top: 0;
    left: 50%;
    width: 600px;
    height: 100%;
    margin-left: -300px;
    text-align: center
  }

  .x_layer_card .figure_video_pic .figure img {
    display: inline-block;
    width: auto;
    max-width: 600px;
    height: 100%
  }

  .x_layer_card {
    font-family: numFont, PingFangSC-Regular, Tahoma, Microsoft Yahei, sans-serif
  }

  .x_layer_card .video_content {
    position: relative;
    min-height: 98px;
    padding: 8px 12px 44px
  }

  .x_layer_card .video_title {
    display: block;
    position: relative;
    height: 24px;
    margin-bottom: 6px;
    overflow: hidden
  }

  .x_layer_card .video_title .tit {
    display: inline-block;
    max-width: 150px;
    overflow: hidden;
    color: #111;
    font-size: 15px;
    font-weight: 700;
    line-height: 24px;
    text-overflow: ellipsis;
    vertical-align: top;
    white-space: nowrap
  }

  .x_layer_card .video_title .tit:hover {
    color: #ff6428
  }

  .x_layer_card .video_title.no_honor .tit {
    max-width: 100%
  }

  .x_layer_card .honor_cup, .x_layer_card .honor_douban, .x_layer_card .honor_weibo {
    display: inline-block;
    margin-top: 4px;
    margin-left: 5px;
    overflow: hidden;
    font-size: 0;
    vertical-align: top
  }

  .x_layer_card .video_tags {
    position: relative;
    height: 20px;
    margin-right: -10px;
    margin-bottom: 8px;
    overflow: hidden;
    letter-spacing: -3px
  }

  .x_layer_card .video_tags .tag {
    display: inline-block;
    _width: 38px;
    max-width: 90px;
    margin-right: 8px;
    padding: 0 8px;
    overflow: hidden;
    border-radius: 20px;
    background: #eee;
    color: #333;
    font-size: 12px;
    letter-spacing: normal;
    line-height: 20px;
    text-align: center;
    text-overflow: ellipsis;
    vertical-align: top;
    white-space: nowrap
  }

  .x_layer_card .video_sum {
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
    word-wrap: break-word;
    display: -webkit-box;
    *position: relative;
    *width: 100%;
    _height: 36px;
    max-height: 36px;
    margin-bottom: 8px;
    overflow: hidden;
    color: #666;
    font-size: 12px;
    line-height: 18px;
    text-overflow: ellipsis;
    white-space: normal;
    word-break: break-all
  }

  .x_layer_card .video_sum .tit {
    color: #111
  }

  .x_layer_card .video_play {
    position: absolute;
    bottom: 9px;
    left: 0;
    width: 100%;
    height: 32px
  }

  .x_layer_card .btn_play {
    display: inline-block;
    *display: inline;
    width: 82px;
    height: 35px;
    margin-left: 12px;
    color: #fff;
    font-size: 12px;
    line-height: 28px;
    text-align: center;
    cursor: pointer
  }

  .x_layer_card .video_btn {
    box-sizing: border-box;
    position: absolute;
    top: 1px;
    right: 12px;
    width: 80px;
    height: 30px;
    font-size: 0;
    letter-spacing: -3px;
    text-align: right
  }

  .x_layer_card .z_figure_collect, .x_layer_card .z_figure_dl {
    display: inline-block;
    *display: inline;
    margin-left: 8px;
    padding: 5px;
    vertical-align: top
  }

  .x_layer_card .z_figure_collect .icon_sm, .x_layer_card .z_figure_dl .icon_sm {
    display: inline-block;
    *display: inline
  }

  .x_layer_card .poster_card_dl {
    position: absolute;
    bottom: -60px;
    left: 0;
    height: 24px;
    padding: 10px 40px 10px 32px;
    border-radius: 48px;
    background-color: #111;
    background-color: rgba(17, 17, 17, .8);
    color: #fff;
    font-size: 12px;
    line-height: 24px;
    white-space: nowrap
  }

  .x_layer_card .poster_card_dl .btn_close {
    position: absolute;
    top: 10px;
    right: 10px;
    width: 24px;
    height: 24px;
    color: #fff
  }

  .x_layer_card .poster_card_dl .btn_close .icon_close_xs {
    display: block;
    margin: 7px auto 0
  }

  .x_layer_card .poster_card_dl .btn_close:hover {
    color: #ff5945
  }

  .x_layer_card .z_figure_collect .icon_collected_sm, .x_layer_card .z_figure_collected .icon_collect_sm {
    display: none
  }

  .x_layer_card .z_figure_collected .icon_collected_sm {
    display: inline-block
  }

  .x_layer_card .z_figure_dl_disabled {
    display: none
  }

  .x_layer_card .figure_video {
    overflow: hidden
  }

  .x_layer_card .figure_video .figure_video_tools {
    z-index: 2;
    background: 0 0
  }

  .x_layer_card .figure_video .figure_mute, .x_layer_card .figure_video .figure_video_tools .figure_info {
    display: none
  }

  .x_layer_card .figure_video:hover .figure_mute {
    display: block
  }

  .x_layer_card .figure_video_source, .x_layer_card video {
    -o-object-fit: cover;
    -webkit-transform: scale(1.4);
    object-fit: cover;
    transform: scale(1.4)
  }

  .x_layer_card_bd_h .video_content {
    min-height: 0 !important
  }

  .x_layer_card .honor_weibo {
    width: 48px;
    height: 16px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: -85px 0;
    background-size: 133px auto
  }

  .x_layer_card .honor_douban {
    width: 48px;
    height: 16px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: -85px -21px;
    background-size: 133px auto
  }

  .x_layer_card .honor_cup {
    width: 37px;
    height: 16px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: -85px -42px;
    background-size: 133px auto
  }

  .x_layer_card .btn_play {
    width: 80px;
    height: 33px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: 0 0;
    background-size: 133px auto
  }

  .x_layer_card .btn_play:hover {
    width: 80px;
    height: 33px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: 0 -38px;
    background-size: 133px auto
  }

  .x_layer_card .z_figure_collect .icon_collect_sm {
    width: 16px;
    height: 16px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: 0 -76px;
    background-size: 133px auto
  }

  .x_layer_card .z_figure_collect:hover .icon_collect_sm {
    width: 16px;
    height: 16px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: -21px -76px;
    background-size: 133px auto
  }

  .x_layer_card .z_figure_collect .icon_collected_sm {
    width: 16px;
    height: 16px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: -42px -76px;
    background-size: 133px auto
  }

  .x_layer_card .z_figure_dl .icon_dl_sm {
    width: 16px;
    height: 15px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: -63px -76px;
    background-size: 133px auto
  }

  .x_layer_card .z_figure_dl:hover .icon_dl_sm {
    width: 16px;
    height: 15px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: -84px -76px;
    background-size: 133px auto
  }

  .x_layer_card .btn_close .icon_close_xs {
    width: 10px;
    height: 10px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: -105px -76px;
    background-size: 133px auto
  }

  .x_layer_card .btn_close:hover .icon_close_xs {
    width: 10px;
    height: 10px;
    background-image: url(/tencentvideo/vstyle/wr-web-layer/style/img/sprite/icon.png?v=8e892f5d76);
    background-position: -120px -76px;
    background-size: 133px auto
  }

  #jacobgong {
    content: "20190327113528"
  }

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
