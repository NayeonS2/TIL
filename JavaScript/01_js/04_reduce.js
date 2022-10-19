const numbers = [90, 80, 70, 100]

// 총합 반환!
// 첫번째 인자 result가 누적값!

//1. 초기값 안넣으면 첫번째 값이 초기값으로 자동설정
const sumNum = numbers.reduce(function (result, number) {
    console.log(result)
    return result + number
})

console.log(sumNum)


// 초기값 설정
const sumNum = numbers.reduce(function (result, number) {return result + number}, 0)

console.log(sumNum)

//2.
const sumNum = numbers.reduce((result, number) => {return result + number}, 0)


//3. 평균값 구하기
const avgNum = numbers.reduce((result,number) => result + number, 0) / numbers.length
