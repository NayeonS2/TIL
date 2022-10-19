const arr = [1,2,3,4,5]

//1. 하나만 통과해도 true !! , 빈배열은 false
const result = arr.some((elem) => elem % 2 === 0)
console.log(result)