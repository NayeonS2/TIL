<template>
  <div id="app">
    <h1>GET CAT</h1>
    <button @click="getCatImg">GET CAT</button>
    <img :src="catImage" alt="cat image">

  </div>
</template>

<script>


export default {
  name: 'App',
  methods: {
    getCatImg () {
      this.$store.dispatch('getCatImg')
    }
  },
  computed: {
    catImage () {
      return this.$store.getters.catImage
    }
  },
  created () {
    this.getCatImg()
  },
  updated () {
    console.log('이미지 리소스가 업데이트 되었습니다.')
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
