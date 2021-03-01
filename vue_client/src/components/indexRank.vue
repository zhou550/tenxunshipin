<template>
  <div class="index_rank">
    <div class="rank_head">
      <h2 class="rank_title">{{rankname}}</h2>
      <div class="bg_rank_ball"></div>
    </div>
    <div class="rank_list">
      <div v-for="(indexitem, index) in indexitems" :key="index" class="rank_item ">
        <span class="rank_num" :class="{rank_num_1:index==0,rank_num_2:index==1,rank_num_3:index==2,}">{{indexitem.sort}}</span>
        <span class="rank_title">{{indexitem.title}}</span>
        <span class="rank_desc">{{indexitem.caption}}</span>
        <span class="rank_update">{{indexitem.description}}</span>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "indexRank",
    props: ['rankname', 'indexitems'],
  }
</script>

<style lang="stylus">
  .index_rank
    width: 388px;

    .rank_head
      position: relative;
      margin: 0 auto;

      .rank_title
        display: inline-block;
        position: relative;
        height: 40px;
        margin: 0 10px 20px 0;
        color: #111;
        font-size: 30px;
        font-weight: 400;
        line-height: 40px;
        vertical-align: top;
        white-space: nowrap;

      .bg_rank_ball
        z-index: -1;
        position: absolute;
        top: -30px;
        left: 170px;
        width: 26px;
        height: 57px;
        border-radius: 13px 13px 0 0;
        background-image: linear-gradient(-180deg, #ff5c38, rgba(255, 255, 255, 0) 83%);
        opacity: .4;

        &:before, &:after {
          position: absolute;
          top: 68px;
          left: -30px;
          width: 20px;
          height: 30px;
          border-radius: 10px 10px 0 0;
          background-image: linear-gradient(-180deg, #ffb821, rgba(255, 255, 255, 0) 79%);
          content: "";
        }

        &:after {
          top: 40px;
          right: -35px;
          left: auto;
          width: 14px;
          height: 40px;
          border-radius: 7px 7px 0 0;
          background-image: linear-gradient(-180deg, #ff117a, rgba(255, 255, 255, 0) 77%);
        }

    .rank_list
      padding: 12px 0;
      border-radius: 4px;
      background-color: #f8f8f8;

      .rank_item
        padding: 18px 30px 15px 40px;
        margin: 0 20px;
        position: relative;

        .rank_num_1, .rank_num_2, .rank_num_3 {
          -webkit-text-fill-color: transparent;
          -webkit-background-clip: text;
          background-image: linear-gradient(180deg, #ffb821 0, #ff5c38 45%, #ff1459);
          color: #ff183e;
          font-size: 28px;
        }

        .rank_num {
          left: 4px;
          position: absolute;
          /*left: 30px;*/
          margin-top: -4px;
          color: #666;
          font-size: 26px;
          line-height: 30px;
        }

        .rank_title {
          margin-right: 80px;
          color: #111;
          font-size: 18px;
          font-weight: 700;
          line-height: 24px;
        }

        .rank_desc {
          color: #999;
          font-size: 13px;
        }

        .rank_desc, .rank_title {
          display: block;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
        }

        .rank_update {
          position: absolute;
          top: 20px;
          right: 20px;
          color: #999;
          font-size: 13px;
          white-space: nowrap;
        }


</style>
