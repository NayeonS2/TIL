<template>
  <!-- 반드시 컴포넌트를 구성하는 최상위 태그가 하나 있어야 에러가 나지 않음! -->
  <!-- template 태그는 렌더링과는 의미 없음 -->
  <div class="border">
    <h1>싸피 이거는 내가 만든 새로운 컴포넌트다!</h1>
    <!-- 3. 보여주기 -->
    <!-- 재사용성 -->
    <!-- 자식으로 보낼때는 kebab-case! -->

    <MyComponentItem 
    static-props="MyComponent에서 보낸 데이터"
    :dynamic-props="dynamicProps"
    @child-to-parent="parentGetEvent"
    @child-input="getDynamicData"
    />
   
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from '@/components/MyComponentItem'


export default {
    // name을 지정해줘야 상위 컴포넌트가 인식할수있음!
    name: 'MyComponent',
    // 2. 등록하기
    components: {
        MyComponentItem,
    },
    data() {
        return {
            dynamicProps: '이건 동적인 데이터!',
        }
    },
    methods: {
        parentGetEvent: function (childData) {
            console.log('자식 컴포넌트에서 발생한 emit 이벤트를 들었다!!')
            console.log(childData)
        },
        // 인자 명은 아무렇게나 가능
        getDynamicData: function (childInputData) {
            console.log(`사용자가 입력한 값은 ${childInputData}입니다.`)
        }
    }
}
</script>

<style>
    .border {
        border: solid 1px black;
    }
</style>