<template>
  <div>
    <h1>App Child</h1>
    <!-- 
      1. 입력한 TEXT 를 childData 와 v-model로 양방향 바인딩하여 사용자가 입력한 값을 저장한다.
      2. 입력할 때 마다 emit으로 데이터를 전달하기위해 input 이벤트를 이용하여 sendData 메서드를 실행한다.
        - 엔터칠 때 마다 데이터를 전달하고 싶으면 @keyup.enter 이벤트를 사용하면 됨
     -->
    <input type="text" v-model="childData" @input="sendData">
    <p>App Data : {{ appData }}</p>
    <p>Parent Data : {{ parentData }} </p>
    <p>Child Data : {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  // Parent가 전달해주는 데이터를 받기위해 props에 선언한다.
  // 이름은 부모 컴포넌트가 전달해주는 케밥케이스 이름을 카멜 케이스 형태로 작성해준다. (html -> js)
  // 그리고 어떤 타입의 값인지 명시해준다.
  props: {
    appData: String,
    parentData: String,
  },
  data() {
    return {
      // 입력 데이터를 저장하기 위해 선언
      childData: null,
    }
  },
  methods: {
    // 입력 데이터를 부모 컴포넌트에 전달하기 위해 emit 이벤트 사용
    // 첫 번째 인자는 '발생하는 이벤트 이름', 두 번째 인자는 '전달하고 싶은 데이터'
    sendData: function () {
      this.$emit('child-data', this.childData)
      // emit 이벤트를 발생시켰다면 이제 부모 컴포넌트에서 이벤트 처리를 해줘야 함
    }
  }
}
</script>

<style>

</style>