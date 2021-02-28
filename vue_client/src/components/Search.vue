<template>
  <form id="searchForm" action="detail.html" method="get" target="_blank">
    <div class="mod_search">
      <div class="search_keywords">
        <input type="text" name="n" value="庆余年" class="search_input" placeholder="搜索" autocomplete="off"/>
      </div>
      <button class="search_btn" type="submit"><span class="btn_inner">全网搜</span></button>
    </div>
  </form>
</template>

<script>
  export default {
    name: 'Search'
  }
</script>

<style scoped>
  .mod_search {
    display: flex;
    width: 428px;
    height: 38px;
    border: 1px solid #ff5c38;
    border-radius: 20px
  }

  .mod_search .search_keywords {
    flex-grow: 2;
    margin: 0 0px 0 20px
  }

  .mod_search .search_input {
    width: 100%;
    padding: 0;
    border: 0;
    outline: 0;
    background: 0 0;
    color: #999;
    font-size: 15px;
    line-height: 40px
  }

  .mod_search .search_input:focus {
    color: #111
  }

  .mod_search .search_btn {
    display: block;
    width: 90px;
    height: 38px;
    padding-right: 6px;
    border: none;
    border-radius: 0 20px 20px 0;
    outline: 0;
    background: #ff5c38;
    color: #fff;
    font-size: 15px;
    line-height: 40px;
    cursor: pointer
  }

  .mod_search .search_btn .btn_inner {
    padding-right: 2px
  }

  .mod_search .search_btn:hover {
    background: #ff183e
  }

</style>
