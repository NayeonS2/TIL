//1. 반환값이 없음 (바로 출력!)
// 안에서 반복만 돌고 말기 때문에 return 값 유무는 상관없음
const colors = ['red', 'blue', 'green']

const printClr = function (color) {
    console.log(color)
}

colors.forEach(printClr)

//2. 함수를 배열 각 요소에다 한번씩 실행 ! python의 map 과 유사!

colors.forEach(function (color) {
    console.log(color)
})


//3. 최종형

colors.forEach((color) => {
    console.log(color)
})

colors.forEach((color) => console.log(color))