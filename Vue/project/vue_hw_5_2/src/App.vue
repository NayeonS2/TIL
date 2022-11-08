// App.vue

<template>
  <div id="app">
    <p>Counter: {{ getCounter }}</p>
    <p>Counter x2: {{ counterDouble }}</p>
    <p></p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>
  </div>
</template>

<script>
export default {
  name: 'App', 
  data: function() {
    return {
      
    }
  },
  methods: {
    increase: function () {
      const data = this.getCounter + 1  // 값 증가
      // 증가된 값을 vuex의 state에 저장필요
      this.$store.dispatch('saveCnt', data)

    },
    decrease: function () {
      const data = this.getCounter - 1  // 값 감소
      this.$store.dispatch('saveCnt', data)
    },
  },
  computed: {
    counterDouble: function () {
      return this.$store.getters.getCounter * 2
    },

    // vuex 에 저장된 데이터 불러오기
    getCounter () {
      return this.$store.getters.getCounter
    }
  },
}
</script>

<style>
</style>