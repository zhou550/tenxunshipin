<template>
  <div class="videospagw">
    <MultipleSelect></MultipleSelect>
    <InfiniteScrollVideoList></InfiniteScrollVideoList>
  </div>
</template>

<script>
  import MultipleSelect from "../components/MultipleSelect";
  import InfiniteScrollVideoList from "../components/InfiniteScrollVideoList";

  export default {
    name: "VideosPage",
    components: {
      MultipleSelect, InfiniteScrollVideoList,
    },
  }
</script>

<style scoped>

</style>
