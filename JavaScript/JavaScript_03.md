# JavaScript

## 동기와 비동기

### 동기 (Synchronous)
- 모든일 `순서대로 하나씩` 처리
- 이전작업이 끝나면 다음작업 시작 (순서대로 처리)
- 요청을 보내고 응답이 올때까지 기다렸다가 다음 로직을 처리

### 비동기 (Asynchronous)
- 작업 시작 후 결과를 기다리지 않고 다음 작업 처리 (병렬적 수행)
- 시간이 필요한 작업들은 요청 보낸뒤 응답이 빨리오는 작업부터 처리

### 비동기 사용 이유
- 사용자 경헙
  - 아주 큰 데이터를 불러온 뒤 실행되는 앱
  - 동기로 처리하면,
  - 데이터 모두 불러온 뒤에야 앱 실행 로직 수행
  - 사용자들은 앱이 멈춘 것과 같은 경험
  - 즉, 동기식은 특정 로직 실행 동안 다른 로직 실행 차단
  - `비동기 처리`하면,
  - `먼저 처리되는 부분부터 보여줄 수 있음`

---

## JavaScript의 비동기 처리

### Single Thread 언어
- JavaScript는 한번에 하나의 일만 수행할 수 있는 Single Thread 언어
- 동시 여러 작업 처리 불가
  - Thread : 작업 처리할 때 실제로 작업 수행하는 주체  
    - multi-thread는 업무 수행 가능 주체가 여러개
- 즉, JavaScript는 하나의 작업을 요청한 순서대로 처리할 수 밖에 없음
  - 그러면 어떻게 비동기 처리?

### JavaScript Runtime
- JavaScript가 비동기 처리할 수 있도록 도와주는 환경 필요
- 특정 언어가 동작할 수 있는 환경 : 런타임
- JavaScript에서 비동기 관련 작업은 브라우저 or Node 환경에서 처리
- 브라우저 환경에서의 비동기 동작은 아래 요소들로 구성
  - JavaScript Engine의 `Call Stack`
  - `Web API`
  - `Task Queue`
  - `Event Loop`

### 비동기 처리 동작 방식
- 브라우저 환경에서의 JavaScript 비동기
  - 모든 작업은 `Call Stack`(LIFO)으로 들어간 후 처리
  - 오래 걸리는 작업이 Call Stack으로 들어오면 `Web API`로 보내서 별도로 처리하도록 함
  - Web API에서 처리가 끝난 작업들은 곧바로 Call Stack으로 들어가지 못하고 `Task Queue`(FIFO)에 순서대로 들어감
  - `Event Loop`가 Call Stack이 비어있는 것을 계속 체크하고 Call Stack이 빈다면 Task Queue에서 가장 오래된(가장 앞에 있는) 작업을 Call Stack으로 보냄

---

## Axios
- JavaScript의 HTTP 웹 통신을 위한 라이브러리
- 확장 가능한 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공


