<template>
  <div class="py-5 bg-primary p-2 text-dark bg-opacity-10 rounded-2">
    <h1>보고싶은 영화</h1>
    
    <input 
    type="text"
    v-model.trim="searchInput"
    @keyup.enter="createWish"
    class="me-2 ms-5 border"
    >
    <button @click="createWish" class="btn btn-outline-primary">🔍</button>
  </div>
</template>

<script>
export default {
    name: 'WatchListForm',
    data() {
      return {
        searchInput: null,
      }
    },
    methods: {
      createWish() {
        if (this.searchInput) {
          this.$store.dispatch('createWish', this.searchInput)
        }
        this.searchInput = null
      }
    }
}
</script>

<style>
 .border {
  
  border-radius:5px;
  width: 250px;
  height: 35px;
 }


</style>