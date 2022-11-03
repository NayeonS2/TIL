<template>
  <div>
    <h1>App Parent</h1>
    <!-- 
      1. 입력한 TEXT 를 childData 와 v-model로 양방향 바인딩하여 사용자가 입력한 값을 저장한다.
      2. 입력할 때 마다 emit으로 데이터를 전달하기위해 input 이벤트를 이용하여 sendData 메서드를 실행한다.
        - 엔터칠 때 마다 데이터를 전달하고 싶으면 @keyup.enter 이벤트를 사용하면 됨
     -->
    <input type="text" v-model="parentData" @input="sendData">
    <p>AppData : {{ appData }}</p>
    <p>ChildData : {{ childData }}</p>
    <!-- 
      App.vue 에서 전달한 데이터와
      parent 컴포넌트에서 입력한 데이터를 자식 컴포넌트에 전달(prop)하고

      자식 컴포넌트에서 발생하는 이벤트를 처리한다.
     -->
    <AppChild 
      :app-data="appData"
      :parent-data="parentData" 
      @child-data="getChild"
      />
  </div>
</template>

<script>
import AppChild from '@/components/AppChild'
export default {
  name: 'AppParent',
  data() {
    return {
      parentData: null, // 부모(App.vue)에서 전달되는 데이터 저장
      childData: null,  // 자식(AppChild.vue)에서 전달되는 데이터 저장
    }
  },
  components: {
    AppChild,
  },
  props: {
    // Parent가 전달해주는 데이터를 받기위해 props에 선언한다.
    // 이름은 부모 컴포넌트가 전달해주는 케밥케이스 이름을 카멜 케이스 형태로 작성해준다. (html -> js)
    // 그리고 어떤 타입의 값인지 명시해준다.
    appData: String,
  },
  methods: {
    // 현재 컴포넌트(AppParent.vue)에서 작성한 데이터를 App.vue 로 전달해주기 위한 메서드
    sendData: function () {
      this.$emit('parent-data', this.parentData)
    },

    // 자식 컴포넌트(AppChild.vue)에서 전달되는 데이터를 App.vue 로 전달해주기 위한 메서드
    // 첫 번째 인자로 자식에서 전달되는 값이니 매개변수를 선언하여 해당 값을 받는다.
    getChild(data) {
      this.childData = data
      this.$emit('send-child', data)
    }
  }
}
</script>

<style>

</style>