<template>
  <div>
    <ul class="list-group">
      <li class="list-group-item list-group-item-action list-group-item-light fs-5 mt-2" @click="updateWish"
    :class="[{ 'is-completed' : wish.isCompleted }, {'list-group-item-dark' : wish.isCompleted}]">{{ wish.title }}</li>
    </ul>
    <!-- <p @click="updateWish"
    :class="{ 'is-completed' : wish.isCompleted }"
    >{{ wish.title }}</p> -->
  </div>
</template>

<script>
export default {
    name: 'WatchListItem',
    props: {
      wish: Object,
    },
    methods: {
      updateWish() {
        this.$store.dispatch('updateWish', this.wish)
      }
    }
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
    
  }
</style>