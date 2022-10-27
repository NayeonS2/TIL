# JavaScript

## 동기와 비동기

### 동기 (Synchronous)
- 모든일 `순서대로 하나씩` 처리
- 이전작업이 끝나면 다음작업 시작 (순서대로 처리)
- 그동안 작성했던 Python 코드들
- 요청을 보내고 응답이 올때까지 기다렸다가 다음 로직을 처리

### 비동기 (Asynchronous)
- 작업 시작 후 `결과를 기다리지 않고` 다음 작업 처리 (병렬적 수행)
- 시간이 필요한 작업들은 요청 보낸뒤 응답이 빨리오는 작업부터 처리
- ex) Gmail에서 메일 전송을 누르면 목록 화면으로 전환되지만 실제로 메일을 보내는 작업은 병렬적으로 뒤에서 처리됨

```javascript
function slowRequest(callBack) {
  console.log('1. 오래 걸리는 작업 시작 ...')
  setTimeout(function () {  
    callBack()
  }, 3000)
}

function myCallBack() {
  console.log('2. 콜백함수 실행됨')
}

slowRequest(myCallBack)
console.log('3. 다른 작업 실행')


// 1. 오래 걸리는 작업 시작 ...
// 3. 다른 작업 실행
// 2. 콜백함수 실행됨
```

### 비동기 사용 이유
- `사용자 경험`
  - 아주 큰 데이터를 불러온 뒤 실행되는 앱
  - 동기로 처리하면,
  - 데이터 모두 불러온 뒤에야 앱 실행 로직 수행
  - 사용자들은 앱이 멈춘 것과 같은 경험
  - 즉, 동기식은 특정 로직 실행 동안 다른 로직 실행 차단
  - `비동기 처리`하면,
  - `먼저 처리되는 부분부터 보여줄 수 있음`
  - 사용자 경험에 긍정적 효과
  - 많은 웹 기능은 비동기 로직을 사용해서 구현되어 있음

---

## JavaScript의 비동기 처리

### Single Thread 언어, JavaScript
- 그럼 응답이 먼저 오는 순서대로 처리하지 말고, 아예 여러 작업을 동시에 처리하면 되지 않을까?
- `JavaScript는 한번에 하나의 일만 수행할 수 있는 Single Thread 언어`
- 동시 여러 작업 처리 불가
  - > [참고] Thread란?
    - 작업을 처리할 때 실제로 작업 수행하는 주체 
    - multi-thread는 업무 수행 가능 주체가 여러개  
- 즉, `JavaScript는 하나의 작업을 요청한 순서대로 처리`할 수 밖에 없음
  - 그러면 Single Thread인 JavaScript가 어떻게 비동기 처리?

### JavaScript Runtime
- JavaScript가 비동기 처리할 수 있도록 도와주는 환경 필요
- 특정 언어가 동작할 수 있는 환경 : `런타임`
- JavaScript에서 `비동기 관련 작업은 브라우저 or Node 환경에서 처리`
- 브라우저 환경에서의 비동기 동작은 아래 요소들로 구성
  - JavaScript Engine의 **`Call Stack`**
  - **`Web API`**
  - **`Task Queue`**
  - **`Event Loop`**

### 비동기 처리 동작 방식
- 브라우저 환경에서의 JavaScript 비동기는 아래와 같이 처리
  - 모든 작업은 `Call Stack`(LIFO)으로 들어간 후 처리
  - 오래 걸리는 작업이 Call Stack으로 들어오면 `Web API`로 보내서 별도로 처리하도록 함
  - Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 `Task Queue`(FIFO)에 순서대로 들어감
  - `Event Loop`가 Call Stack이 비어있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된(가장 앞에 있는) 작업을 Call Stack으로 보냄

### Call Stack
- 요청이 들어올 때 마다 순차적으로 처리하는 Stack(LIFO)
- 기본적인 JavaScript의 Single Thread 작업 처리

### Web API
- JavaScript 엔진이 아닌 브라우저에서 제공하는 runtime 환경으로
- 시간이 소요되는 작업을 처리 (setTimeout, DOM Event, AJAX 요청 등)

---

## Axios
- JavaScript의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능한 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공


### LIKES
- **내가 누른 버튼의 DOM 조작하기 (DOM)**
  - form을 전부 선택 후 (`querySelectorAll`) -> `eventListener` 추가 (`forEach`)
  - 몇번째 버튼인지를 몰라서 
  - 몇번째 정보를 속성으로 (article.pk) 정보 전달
    - `dataset` 사용 (각 버튼들의 구분을 위해!)
      - HTML : data-변수명="값" (변수명 : article-id)
      - JS : dataset.변수명 (변수명 자동 변환 : articleId)
- **axios 요청으로 좋아요 보내기 (Ajax)**
  - axios 이용해서 `url`, `method` 설정 요청했는데
  - 동작 x (403 ForBidden Error) -> `CSRF TOKEN` 필요
  - {% csrf token %}로 생성된 값을 추출
    - 속성 선택자(querySelector) `[name=csrfmiddlewaretoken]` 요소 선택해서 value값 추출
  - headers 라는 곳에 `headers: {'X-CSRFToken': csrftoken}` 전달 (정상적 요청)
- **응답받은 data로 DOM 변경 (DOM)**
  - views.py (백) 에서 버튼이 눌렸는지 여부를 전달해주는 `is_like` 변수 만들고, json으로 응답 (`JsonResponse`)
  - 좋아요 누른 사람 수를 보여주기 위해 '`like_cnt`': article.like_users.count()도 같이 JsonResponse로 전달해줌
- JS에서 isLike와 likeCnt로 data 가져와주고,
- likeCntText 변수로 좋아요 수 span 태그 선택하고 innerText를 likeCnt로 변경!

