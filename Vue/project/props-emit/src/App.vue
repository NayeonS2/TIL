<template>
  <div id="app">
    <h1>App</h1>
    <!-- 
      입력한 TEXT 를 childData 와 v-model로 양방향 바인딩하여 사용자가 입력한 값을 저장한다.
    -->
    <input type="text" v-model="appData">
    <p>Parent Data : {{ parentData }}</p>
    <p>Child Data : {{ childData }}</p>

    <!-- 
      App.vue 에서 입력한 데이터를 자식 컴포넌트(AppParent.vue)에 전달(prop)하고

      자식 컴포넌트에서 발생하는 이벤트를 처리한다.
      현재 AppParent.vue 에서는 2개의 이벤트가 발생한다. (Parent, Child data 전달)
     -->
    <AppParent 
      :app-data="appData" 
      @parent-data="getParent"
      @send-child="getChild"
      />
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'

export default {
  name: 'App',
  data() {
    return {
      appData: null,
      parentData: null,
      childData: null,
    }
  },
  components: {
    AppParent,
  },
  methods: {
    // AppParent.vue 에서 전달되는 데이터 저장
    getParent: function (data) {
      this.parentData = data
    },

    // AppChild.vue 에서 전달되는 데이터 저장 
    // (AppParent.vue가 다시 App.vue로 전달하는 형태)
    // (AppChild => AppParent.vue => App.vue)
    getChild(data) {
      this.childData = data
    }
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
