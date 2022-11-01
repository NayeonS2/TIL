# Vue
## Vue intro

### Front-end(FE) 개발이란?
- 사용자에게 보여주는 화면 만들기
- `Web App`(SPA)을 만들 때 사용하는 도구
  - SPA - Single Page Application

### Web App이란?
- 웹 브라우저에서 실행되는 어플리케이션 소프트웨어
- 개발자 도구 > 디바이스 모드
- 웹페이지가 그대로 보이는 것이 아닌 `디바이스에 설치된 App`처럼 보이는 것
- 웹페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태

### SPA (Single Page Application)
- **서버에서 최초 1장의 HTML만 전달**받아 모든 요청에 대응하는 방식
- `CSR (Client Side Rendering)` 방식으로 요청을 처리
  - 기존 요청처리방식은 `SSR (Server Side Rendering)`

> [참고] SSR 이란?

<img src="./Vue_img/ssr.png">

- Server가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
- 전달받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행

### CSR (Client Side Rendering) 이란?
- 최초 한 장의 HTML을 받아오는 것은 동일
- 단, **server로부터 최초로 받아오는 문서는 빈 html문서**
- 각 요청에 대한 대응을 JavaScript를 사용하여 **필요한 부분만 다시 렌더링**
  - 새로운 페이지를 서버에 AJAX로 요청
  - 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
  - JSON 데이터를 JavaScript로 처리, DOM 트리에 반영 (렌더링)
  - <img src="./Vue_img/csr.png">

<img src="./Vue_img/csr2.png">

### CSR 방식 사용 이유
- 모든 HTML 페이지를 서버로부터 받는 것이 아니기 때문
  - 클라이언트 - 서버 간 통신 즉, 트래픽이 감소
  - 트래픽이 감소 == 응답 속도가 빨라짐
- 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행 (UX 향상)
- BE와 FE의 작업 영역을 명확히 분리 가능 (협업 용이)

### CSR은 만능?
- 첫 구동 시 필요한 데이터가 많으면 최초 작동 시작까지 오랜 시간 소요
- 검색 엔진 최적화가 어려움


### **CSR vs SSR**
---

## Vue로 코드 작성하기
- CND
- **Vue instance 생성**
- `el, data` 설정
- 선언적 렌더링 `{{}}`


### input tag에 v-model 작성
- input에 값 입력 -> Vue data 반영
-  Vue data -> DOM 반영
-  Vanilla JS만으로 모든 데이터 조작 -> 불필요한 코드 반복
-  Vue -> 변경 사항도 한 번에 반영 (하나의 data로 관리)

---

## Vue2 vs Vue3
- 여전히 vue2

---

## Vue instance

### MVVM Pattern
- DOM : `View`
  - 우리눈에 보이는 부분
- Vue : `ViewModel`
  - View와 binding되어 action 주고받음
  - Model이 변경되면 View Model도 변경되고 바인딩된 View도 변경
  - View에서 사용자가 데이터를 변경하면 View Model 데이터가 변경되고 바인딩된 다른 View도 변경
- Plain JavaScript Objects : `Model`
  - 실제 데이터 (JSON)


### Vue instance
- `new` 연산자 사용한 생성자 함수 호출
  - vue instance 생성
    - 아주 많은 속성과 메서드를 가지고있어서, 이러한 기능들을 사용하는 것!

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="app">

  </div>
  <!-- Vue CDN -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    // CODE HERE
    // 1. Vue instance constructor
    // const vm = new Vue()
    // console.log(vm)

    // 2. el
    const app = new Vue({
      el: '#app',
    //   // 3. data
      data: {
        message: 'Hello, Vue!'
      },

    //   // 4. methods
      methods: {
        print: function () {
          console.log(this.message)
        },
      

        bye: function () {
          this.message = 'Bye, Vue!'
        },

    //   //   // 4-1. arrow function
        arrowBye: () => {
          // arrowfunction은 메서드 정의시 쓰면 안됨! this가 window 객체를 가르킴
          // 콜백함수 내에선 써도됨!
          this.message = 'Arrow Function?'
          console.log(this)
        }
      }
    })
    console.log(app)
  </script>
</body>
</html>
```

> [참고] 생성자 함수


### el (element)
- Vue instance와 DOM을 mount(연결)하는 옵션
  - View와 Model을 연결
  - HTML id 혹은 class와 마운트 가능
- Vue instance와 **연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음**
  - Vue 속성 및 메서드 사용 불가


### data
- Vue instance의 `데이터 객체` 혹은 `인스턴스 속성`
- 데이터 객체는 반드시 기본 객체 `{} (object)`여야함
- 객체 내부 아이템들은 value로 모든 타입의 객체를 가질 수 있음
- 정의된 속성은 `interpolation {{}}` 을 통해 view에 렌더링 가능
- 추가된 객체의 각 값들은 `this.message` 형태로 접근 가능!


### methods
- 마지막 s 주의!
- Vue instance의 `method`들을 정의하는 곳
- `methods` 객체 정의
  - methods도 object임!
  

> [주의] methods with Arrow Function
- methods에서 메서드 정의할때는 arrow function 사용 x!!!!!!

---

## Basic of Syntax

### Template Syntax

### RAW HTML
- `v-html` directive
- HTML 기본 속성이 아닌 Vue가 제공하는 특수 속성의 값으로 data 작성



---
## Directives

- `v-접두사`
- **표현식의 값이 변경될 때 반응적으로 DOM에 적용**

### v-text
- `{{ }}` 와 유사한 역할


### **v-html** **
- RAW HTML을 표현할 수 있는 방법
- 단, 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지!

### **v-show** **
- 표현식에 작성된 값에 element를 보여줄 것인지 결정
  - boolean 값이 변경 될 때 마다 반응
- **toggle 비용은 저렴**하나, **렌더링 비용은 비쌈**!!!
  - **표현식 결과와 관계없이 렌더링**
  - **CSS의 display 속성**을 이용해 block or none 값만 바꾸면 되기때문
- 화면에서만 사라졌을 뿐, **DOM에는 존재**!


```html
<!-- 3. v-show && v-if -->
  <div id="app3">
    <p v-show="isActive">보이니? 안보이니?</p>
    <p v-if="isActive">안보이니? 보이니?</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app3 = new Vue({
      el: '#app3',
      data: {
        isActive: false
      }
    })
  </script>
```

### v-if
- v-show와 사용 방법은 동일
- isActive의 값이 변경될 때 반응
- 단, 값이 false면 **DOM에서 사라짐!**
- **toggle 비용이 비싸지만, 초기 렌더링 비용은 낮음**
  - 표현식 결과가 false인 경우 렌더링조차 되지 않기 때문!
  - 단, 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가할 수 있음


### v-for

- for .. in ..
- (char, index)
- 각 요소가 객체면 `dot notation` 접근 가능
- `"v-for 사용 시 반드시 key 속성을 각 요소에 작성!!!!!!"`

```html
<div v-for="(item, index) in myArr2" :key="`arry-${index}`">
      <p>{{ index }}번째 아이템</p>
		  <p>{{ item.name }}</p>
    </div>
    ...
```

### v-on
- addEventListener와 유사
- `'@'` shortcut


### v-bind
- HTML 기본 속성에 Vue data를 연결
- class의 경우 다양한 형태로 연결 가능
  - `조건부 바인딩`
    - {'class Name': '조건 표현식'}
    - 삼항 연산자도 가능
  - `다중 바인딩`
    - ['JS 표현식','JS 표현식',...]
- `':'` shortcut


### v-model
- 사용자 입력 받는 곳에서 사용!
- Vue instance와 DOM의 `양방향 바인딩`

---

## Vue advanced
### computed
- Vue instance의 options중 하나

### **method vs computed** **
- `method` (**동작**)
  - 호출 될 때마다 함수를 실행
  - 같은 결과여도 매번 새롭게 계산
- `computed` (**값**)
  - 함수 종속대상의 변화에 따라 계산 여부가 결정됨
  - **사용하는 변수가 변하면 계산을 새로함**
    - 메모리에 저장 (cache)
  - 종속대상이 **변하지 않으면 항상 저장(캐싱)된 값을 반환**

### watch (**동작**)
- 특정 데이터의 변화를 감지
  - **특정 데이터가 변경되면 실행하여라!**
  - 따로 호출 필요 x!
- **실행 함수를 Vue method로 대체 가능**
  - 감시 대상 data의 이름드로 객체 생성
  - 실행하고자 하는 method를 handler에 문자열 형태로 할당


### filters
- Vue의 옵션
- interpolations 혹은 v-bind 이용할 때 사용 가능
- 자바스크립트 표현식 마지막에 `'|'`와 함께 추가되어야함
- chaining 가능
- return 필수!



---
# Vue 스타일 가이드

## Always use key with v-for

## Never use v-if on the same element as v-for
- v-if 가 v-for보다 높은 우선순위
