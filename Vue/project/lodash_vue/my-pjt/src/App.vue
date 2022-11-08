<template>
  <div id="app">
  
    <TheLunch/>
    <TheLotto/>
  </div>
</template>

<script>
import TheLunch from '@/components/TheLunch'
import TheLotto from '@/components/TheLotto'

export default {
  name: 'App',
  data() {
    return {
      lottoNum: null,
    }
  },
  components: {
    TheLunch,
    TheLotto,
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
