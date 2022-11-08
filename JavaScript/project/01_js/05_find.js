const avengers = [
    { name: 'Tony Stark', age: 45 },
    { name: 'Steve Rogers', age: 32},
    { name: 'Thor', age: 40},
]

// return 값이 참이면 해당 요소 반환 후 실행 종료
// 조건 만족하는 첫번째 요소 반환
// 찾는 값이 배열에 없으면 undefined 반환

// filter는 새로운 배열 생성
// find는 원소 출력


const avenger = avengers.find((avenger) => {
    return avenger.name === 'Tony Stark'
})

console.log(avenger)