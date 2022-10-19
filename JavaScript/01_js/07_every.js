// 배열 모든 요소가 판별 함수 통과해야 true
// 하나라도 통과못하면 false
// 빈 배열은 항상 true

const arr = [1,2,3,4,5]


const result = arr.every((elem) => elem % 2 === 0)
console.log(result)