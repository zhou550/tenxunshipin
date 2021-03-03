<template>
  <div id="app">
    <!--路由链接-->

    <router-view></router-view>
    <FixedAnchor>

      <div class="anchor-list" slot="default">
        <router-link  class="anchor-item"  to="/index">首页</router-link>
        <router-link class="anchor-item" to="/videos">视频列表</router-link> <!--用于渲染当前路由组件-->
      </div>

    </FixedAnchor>
  </div>
</template>

<script>
  import FixedAnchor from "./components/FixedAnchor";

  export default {
    name: 'App',
    components: {
      FixedAnchor,
    },
    mounted() {


      console.log()
      if(this.$route.path=="/"){
        //路径为/时，跳到首页
        this.$router.push("index");
      }

    },
  }
</script>

<style lang="stylus">
  body
    margin 0
    padding 0
</style>
