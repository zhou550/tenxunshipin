<template>
  <div class="site_head site_head_absolute" id="new_vs_header">

    <div class="head_inner">
      <div class="site_logo"></div>

      <Search></Search>
      <!-- 快捷入口 开始 -->
      <div class="mod_quick cf">
      </div>
      <!-- 快捷入口 结束 -->
    </div>
  </div>
</template>

<script>
  import Search from "./Search";

  export default {
    name: "IndexNav",
    components: {
      Search,
    },
  }
</script>

<style lang="stylus">


  .site_head
    z-index: 10;
    position: relative;
    top: 0;
    left: 0;
    width: 100%;
    min-width: 1000px;
    height: 68px;
    background: #fff;
    color: #666;
    font-size: 12px;

    .head_inner
      display flex
      justify-content space-between
      align-items center
      width: 1710px;
      height: 68px;
      margin: 0 auto;

      .site_logo
        width: 157px;
        height: 40px;
        background: url('~@/assets/sprite_head_logo.svg') 0 -36px no-repeat;


  .site_head_absolute {
    -webkit-backdrop-filter: blur(1px);
    backdrop-filter: blur(1px);
    background: #fff;
    background: rgba(255, 255, 255, .14);
  }

  .site_head_absolute {
    position: absolute;
  }

</style>
