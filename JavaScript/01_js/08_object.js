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




const obj = {
    name: 'jack',
    greeting() {
        console.log('hi!')
    }
}

console.log(obj.name)
console.log(obj.greeting())



const key = 'ssafy'
const value = ['한국', '미국', '일본', '중국']

const myObj = {
    [key]: value,
}
console.log(myObj)
console.log(myObj.ssafy)



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





