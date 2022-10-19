const numbers = [1,2,3,4,5]

//1. forEach + return !!
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