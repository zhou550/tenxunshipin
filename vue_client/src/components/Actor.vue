<template>
  <div class="actress open">
    <div  @mouseenter="overSmall=true"  @mouseleave="overSmall=false" >
      <a href="http://v.qq.com/x/star/75098" target="blank" class="img"  >
        <img  class="video_actor_pic" :src="actress.headUrl" itemprop="image">
      </a>
      <span class="name" itemprop="name" _stat="info:actor_name">{{actress.japaneseName}}</span>
    </div>
    <div class="actor_pop" v-show="overBig||overSmall" @mouseenter="overBig=true"  @mouseleave="overBig=false">
      <div class="quick_pop_inner">
        <i class="triangle_up triangle_up_wrap"><i class="triangle_up"></i></i>
        <div class="pop_info_content">
          <div class="actor_info">
            <a href="http://v.qq.com/x/star/75098" target="_blank" class="actor_img" _stat="info:card_avatar"><img class="actor_pic" :src="actress.headUrl"></a>
            <div class="actor_detail">
              <h2 class="actor_name"><a href="http://v.qq.com/x/star/75098" target="_blank" _stat="info:card_name">{{actress.japaneseName}}</a></h2>
              <div class="info"><span class="info_tit">职业：</span><span class="info_txt">演员 歌手</span></div>
              <div class="info"><span class="info_tit">地区：</span><span class="info_txt">中国香港</span></div>
            </div>
            <div class="actor_desc">
									<span class="txt" itemprop="description">朱茵，1971年10月25日出生于香港，中国香港影视女演员、歌手，毕业于香港演艺学院戏剧系。
1991年，参演个人首部电影《逃学威龙2》，从而正式出道。1993年获得壹电视十大最受欢迎电视艺人奖。1994年凭借武侠剧《射雕英雄传》进入观众...</span>
              <a href="http://v.qq.com/x/star/75098" target="_blank" class="desc_more" _stat="info:card_detail">查看详情<i class="icon_sm icon_right_sm"><svg class="svg_icon svg_icon_right_sm" viewBox="0 0 16 16" width="16" height="16"><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg_icon_right_sm"></use></svg></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Actress',
    data () {
      return {
        overSmall: false,
        overBig: false,
      }
    },
    props:['actress'],
  }
</script>

<style scoped>
  .actress {
    position: relative;
    width: 80px;
    margin: 0 10px 7px;
    float: left;
    text-align: center;
  }
  .actress .img {
    display: block;
    position: relative;
    width: 50px;
    height: 50px;
    margin: 0 auto 2px;
    border-radius: 50px;
    background-color: #eee;
    color: #666;
    font-size: 12px;
    line-height: 50px;
    cursor: pointer;
  }
  .video_actor_pic{
    display: block;
    width: 100%;
    height: 100%;
    border-radius: 50%;
  }
  .name {
    display: block;
    overflow: hidden;
    color: #666;
    font-size: 12px;
    line-height: 20px;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .open .actor_pop {
    display: block;
  }
  .actor_pop {
    -webkit-animation-duration: .3s;
    -webkit-animation-delay: 0s;
    -webkit-animation-timing-function: ease-in;
    -webkit-animation-fill-mode: both;
    display: none;
    position: absolute;
    top: 57px;
    right: 0;
    width: 414px;
    margin-right: -167px;
    animation-duration: .3s;
    animation-fill-mode: both;
    animation-timing-function: ease-in;
    animation-delay: 0s;
  }
  .actor_pop .quick_pop_inner {
    border-top: 2px solid #ff5c38;
  }


  .actor_pop .quick_pop_inner {
    border-top: 2px solid #ff5c38;
  }
  .actor_pop .triangle_up_wrap {
    position: absolute;
    top: -13px;
    right: 50%;
    margin-right: -7px;
    overflow: visible;
    border-bottom-color: #ff5c38;
  }

  .actor_pop .triangle_up {
    border-width: 7px;
  }
  .triangle_up {
    border-bottom: 5px solid #111;
  }
  .triangle_down, .triangle_left, .triangle_right, .triangle_up {
    display: inline-block;
    width: 0;
    height: 0;
    overflow: hidden;
    border: 5px dashed transparent;
    font-size: 0;
  }
  .actor_pop .triangle_up_wrap .triangle_up {
    position: absolute;
    top: -4px;
    left: -7px;
    border-bottom-color: #fff;
  }

  .actor_pop .triangle_up {
    border-width: 7px;
  }
  .triangle_up {
    border-bottom: 5px solid #111;
  }
  .triangle_down, .triangle_left, .triangle_right, .triangle_up {
    display: inline-block;
    width: 0;
    height: 0;
    overflow: hidden;
    border: 5px dashed transparent;
    font-size: 0;
  }

  .actor_pop .quick_pop_inner {
    border-top: 2px solid #ff5c38;
  }
  .actor_pop .pop_info_content {
     z-index: 2;
     position: relative;
     padding: 18px 19px;
     border: 1px solid #ccc;
     border-top: none;
     border-radius: 4px;
     background: #fff;
     box-shadow: 0 28px 50px rgba(25,24,40,.35);
     color: #666;
     font-size: 12px;
     line-height: 20px;
     text-align: left;
   }
  .actor_pop .pop_info_content {
    z-index: 2;
    position: relative;
    padding: 18px 19px;
    border: 1px solid #ccc;
    border-top: none;
    border-radius: 4px;
    background: #fff;
    box-shadow: 0 28px 50px rgba(25,24,40,.35);
    color: #666;
    font-size: 12px;
    line-height: 20px;
    text-align: left;
  }.actor_pop .actor_detail {
     display: inline-block;
     margin-left: 14px;
     vertical-align: top;
   }.actor_pop .actor_detail .actor_name {
      margin-top: 6px;
      color: #111;
      font-size: 18px;
      font-weight: 400;
      line-height: 30px;
    }.actor_pop .actor_detail .info {
       margin-bottom: 1px;
     }
  .actor_pop .actor_img {
    display: inline-block;
    width: 80px;
    height: 80px;
    margin-bottom: 10px;
    border-radius: 50%;
  }
  .actor_pop .actor_img .actor_pic, .actor_pop .actor_img img {
    width: 100%;
    height: 100%;
    border-radius: 50%;
  }.actor_pop .actor_detail .actor_name {
     margin-top: 6px;
     color: #111;
     font-size: 18px;
     font-weight: 400;
     line-height: 30px;
   }
  .actor_pop .actor_detail .info_tit {
    color: #999;
  }.actor_pop .actor_detail .actor_name {
     margin-top: 6px;
     color: #111;
     font-size: 18px;
     font-weight: 400;
     line-height: 30px;
   }.desc_more {
      position: absolute;
      right: 0;
      bottom: 0;
      padding-left: 30px;
      background: #fff;
      background: linear-gradient(90deg,rgba(255,255,255,.2) 0,#fff 20px);
      line-height: 20px;
      cursor: pointer;
    }.actor_pop .actor_desc {
       position: relative;
     }.desc_more .icon_right_sm {
        position: relative;
        top: 3px;
      }
  .icon, .icon_gg, .icon_l, .icon_lg, .icon_sm, .icon_xl, .icon_xs, .icon_xxl, .icon_xxxl {
    display: inline-block;
    color: inherit;
  }
  .icon_sm {
    display: inline-block;
    width: 16px;
    height: 16px;
  }a {
     color: #111;
   }a {
      text-decoration: none;
      cursor: pointer;
    }user agent stylesheet
     h2 {
       display: block;
       font-size: 1.5em;
       margin-block-start: 0.83em;
       margin-block-end: 0.83em;
       margin-inline-start: 0px;
       margin-inline-end: 0px;
       font-weight: bold;
     }* {
        margin: 0;
        padding: 0;
      }.actor_pop .quick_pop_inner {
         border-top: 2px solid #ff5c38;
       }
</style>
