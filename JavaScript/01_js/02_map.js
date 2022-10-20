const numbers = [1,2,3,4,5]

//1. forEach + return !!
// return 값을 원소로 사용
// return 값을 결과로 새로운 배열 생성
const doubleEle = function (number) {
    return number * 2
}

const newArray = numbers.map(doubleEle) // 반환값이 존재

console.log(newArray)

//2.
const newArray = numbers.map(function (number) {
    return number * 2
})

//3. 가장 흔하게 쓰는 단계
const newArray = numbers.map((number) => {
    return number * 2
})

//4.
const newArray = numbers.map((number) => number * 2)