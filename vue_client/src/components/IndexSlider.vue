<template>
  <div class="site_slider site_slider_intrude">
    <div class="slider_inner">
      <!--  background-image写成    backgroundImage   ！！！！！！1-->
      <div class="slider_item in" :style="{backgroundColor: imgInColor, backgroundImage: 'url('+imgIn+')'}"></div>
      <div class="slider_item out" :style="{ backgroundColor: imgOutColor,backgroundImage: 'url('+imgOut+')'}"></div>
    </div>
    <div class="slider_nav slider_nav_watched">
      <div v-for="(item, index) in sliders" :key="index" @mouseenter="handleEnter(index)" class="nav_link"
           :class="{current:cur==index}">
          <span class="text text2" :title="item.title">
            <span class="title_text">{{item.title}}</span>{{item.caption}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "IndexSlider",
    data() {
      return {
        cur: 0,
        imgOut: '',
        imgOutColor: ''
      }
    },
    computed: {
      imgIn: function () {
        if (this.sliders[this.cur]) {
          return this.sliders[this.cur].img;
        }
        return "";
      },
      imgInColor: function () {
        if (this.sliders[this.cur]) {
          return this.sliders[this.cur].description;
        }
        return "";
      },
    },
    props: ['sliders',],
    methods: {
      handleEnter(index) {
        this.imgOutColor = this.imgInColor;
        this.imgOut = this.imgIn;
        this.cur = index;
      },
    }
  }
</script>

<style lang="stylus">
  .site_slider
    z-index: 1;
    position: relative;
    height: 500px;

    margin-bottom: 30px;
    overflow: hidden;

    .slider_inner
      position: absolute;
      width: 100%;
      height: 100%;
      transition: transform 1.8s ease, -webkit-transform 1.8s ease;

      .slider_item
        position: absolute;
        width: 100%;
        height: 100%;
        background-position: center 0;
        background-repeat: no-repeat;

    .slider_nav
      display flex
      flex-direction column
      justify-content space-around
      width: 310px;
      top: 68px;

      background: rgba(15, 15, 30, .4);
      z-index: 2;
      position: absolute;
      right: 0;
      bottom: 0;
      width: 348px;
      padding 20px 0

      overflow: hidden;
      background: #0f0f1e;
      background: rgba(15, 15, 30, .5);
      user-select: none;

      .nav_link
        display: block;
        position: relative;
        height: 35px;
        margin-left: 45px;
        color: #fff;
        color: rgba(255, 255, 255, .7);
        font-size: 15px;
        line-height: 35px;
        cursor: pointer;
        margin-left: 40px;

        &.current
          color: #ff5c38;

          .title_text
            font-size: 22px;
            font-weight: 700;

          .text2
            font-size: 13px;


        .title_text
          padding-right: 5px;
          font-size: 15px;
          transition: font-size .08s ease;

        .text
          display: block;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
          cursor: inherit;

        .text2
          font-size: 0;

        .title_text
          padding-right: 5px;
          font-size: 15px;
          transition: font-size .08s ease;

</style>
