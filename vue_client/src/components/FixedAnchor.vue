<template>
  <div class="fixed-anchor" style="">
      <slot  name="default"></slot>
  </div>
</template>

<script>
  export default {
    name: "FixedAnchor"
  }
</script>

<style lang="stylus">

  .fixed-anchor
    position: fixed;
    bottom: 50%;
    right: 1%;
    margin-bottom: -199px;
    z-index: 1000;
    text-align: center;
    background-color: rgb(25, 26, 32);
    box-shadow: 0 1px 6px 0 rgba(0,0,0,.1);
    border-radius: 4px;
    .anchor-list
      padding: 5px 0;
      font-size: 0;
      background: hsla(0,0%,100%,.05)
      display flex
      flex-direction column
      .anchor-item
        padding: 5px 7px;
        line-height: 18px;
        font-size: 14px;
        color: hsla(0,0%,100%,.6);



</style>
