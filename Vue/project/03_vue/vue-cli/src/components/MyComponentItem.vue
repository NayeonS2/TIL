<template>
    <div>
        <h3>나는 MyComponent의 하위 컴포넌트</h3>
        <p>{{ staticProps }}</p>
        <p>{{ dynamicProps }}</p>
        <button @click="childToParent">클릭!</button>
        <input type="text" 
        v-model="childInputData"
        @keyup.enter="childInput">
    </div>
</template>

<script>
export default {
    name: 'MyComponentItem',
    // 부모에게서 받을때는 camelCase
    props: {
        staticProps: String,
        // dynamic-props의 camelCase
        dynamicProps: String,
    },
    data: function () {
        return {
            childInputData: null,
        }
    },
    methods: {
        childToParent: function () {
            // 기본속성값 emit
            // 이름, 추가데이터
            this.$emit('child-to-parent', '나는 자식이 보낸 데이터다')

        },
        childInput: function () {
            this.$emit('child-input', this.childInputData)
            this.childInputData = null
        }
    },
}
</script>

<style>

</style>