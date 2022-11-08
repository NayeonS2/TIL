const products = [
    { name: 'cucumber', type: 'vegetable'},
    { name: 'banana', type: 'fruit'},
    { name: 'carrot', type: 'vegetable'},
    { name: 'apple', type: 'fruit'},
]

// return 값이 참인지 거짓인지 확인 -> true라면 원소로 사용!!! (false는 사용x)


//1. True / False로 반환
const fruitFilter = function (product) {
    return product.type === 'fruit'
}

const newArray = products.filter(fruitFilter)

console.log(newArray)

//2.
const newArray = products.filter(function (product) {
    return product.type === 'fruit'
})

//3.
const newArray = products.filter((product) => {
    return product.type === 'fruit'
})

//4.
const newArray = products.filter((product) => product.type === 'fruit')