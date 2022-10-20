const myInfo = {
    name: 'jack',
    phoneNumber: '123456',
    //띄어쓰기있을땐 콜론써서 키 정의
    'samsung products': {
        buds: 'Galaxy Buds pro',
        galaxy: 'Galaxy s99'
    },
}

console.log(myInfo.name)
console.log(myInfo['name'])
console.log(myInfo['samsung products'].galaxy)


// 1. 속성명 축약
// 객체 정의 시 key와 할당하는 변수 이름 같으면 축약 가능


// 2. 메서드 명 축약
const obj = {
    name: 'jack',
    greeting() {
        console.log('hi!')
    }
}

console.log(obj.name)
console.log(obj.greeting())


// 3. 계산된 속성
// 객체 정의 시 key의 이름을 표현식을 이용해 동적으로 생성 가능
const key = 'ssafy'
const value = ['한국', '미국', '일본', '중국']

const myObj = {
    [key]: value,
}
console.log(myObj)
console.log(myObj.ssafy)



// 4. 구조 분해 할당
// 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당 가능

const { name, phoneNumber } = myInfo


// 5. Spread syntax (...)
// 배열과 마찬가지로 전개구문 사용해 객체 내부에서 객체 전개 가능
// 얕은 복사에 활용

const obj = {b:2, c:3}
const newObj = {a:1, ...obj, d:4}

console.log(newObj) 



//JSON
const jsonData = {
    coffe: 'Americano',
    iceCream: 'Mint Choco',
}

// Object -> json
const objToJson = JSON.stringify(jsonData)

console.log(objToJson)  // {"coffe":"Americano","iceCream":"Mint Choco"}

console.log(typeof objToJson) // string


// json -> Object (중요***- api와 소통할때)
// django가 json을 주면 자바스크립트가 parse해서 object로 바꿔서 적당한 위치에 배분 ...

const jsonToObj = JSON.parse(objToJson)

console.log(jsonToObj)  // { coffe: 'Americano', iceCream: 'Mint Choco' }

console.log(typeof jsonToObj)   // object

console.log(jsonToObj.iceCream) 





