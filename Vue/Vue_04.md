## UX & UI
### UX (User Experience)
- 유저와 가장 가까이 있는 분야, 데이터 기반으로 유저 조사, 분석해서 개발자, 디자이너가 이해할 수 있게 소통
- 유저가 느끼는 느낌, 태도 그리고 행동을 디자인

### UI (User Interface)
- 유저에게 보여지는 화면을 디자인
- UX를 고려한 디자인을 반영, 이 과정에서 기능 개선 혹은 추가가 필요한 경우 프론트엔드 개발자와 가장 많이 소통

> [참고] Interface
- 서로 다른 두개의 시스템, 장치 사이에서 정보나 신호를 주고받는 경우의 접점
  - 사용자가 기기를 쉽게 동작 시키는데 도움을 주는 시스템
- CLI(command-line interface)나 GUI(Graphic User Interface)를 사용해서 컴퓨터를 조작

### UX/UI 그리고 HCI
- GUI : 유저가 보는 일반적 시각적인 디자인
- UI : 비시각적인 부분까지 포함한 디자인
- UX : 유저가 겪는 모든 경험 (컴퓨터와 관련 없는 부분까지 포함)
- HCI : 인간과 컴퓨터 사이의 상호작용에 대한 학문

## Prototyping
### Software prototyping
- 애플리케이션의 프로토타입을 만드는 것
- 개발중인 소프트웨어 프로그램의 완성되기 전 버전
- 한번에 완성 버전이 나올수 없기에 중간마다 현재 상태 체크하는 과정

### Figma
- 인터페이스 디자인을 위한 협업 웹 애플리케이션
- `협업`에 중점을 두면서 UI/UX 설계에 초점
- 웹 기반 시스템
  - 매우 가벼운 환경에서 실행 가능
  - 모든 작업 내역이 웹에 저장됨
- `실시간으로 팀원들이 협업`할 수 있는 기능 제공
- 직관적이고 다양한 디자인 툴
- Figma 사용자들이 만든 다양한 플러그인 존재 (VSCode 확장 프로그램 등)
- `대부분의 기능을 무료로 사용` 가능

### 프로젝트 시작 전
- 개발부터 시작하지 말고 반드시 충분한 기획 필요
- 프로토타입
- 이런 과정을 통해 기획에서 빠진 화면이나 API등을 확인 가능
- 설계 기획이 끝난 후 개발 시작해야 체계적인 진행 가능

### 프로젝트와 협업
- 효과적 협업 위해 다양한 방법과 도구 찾기

---


# Vue Router

## Routing
- 네트워크에서 경로를 선택하는 프로세스
- 웹 서비스에서의 라우팅
  - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
  - /articles/index/에 접근하면 articles의 index에 대한 결과를 보내줌

### Routing in SSR
- Server가 모든 라우팅을 통제 (view)
- URL로 요청이 들어오면 응답으로 완성된 HTML 제공
  - Django로 보낸 요청의 응답 HTML은 완성본인 상태였음
- 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐

### Routing in SPA / CSR
- 서버는 하나의 HTML(index.html)만을 제공
- 이후에 모든 동작은 하나의 HTML 문서 위에서 Javascript 코드를 활용
  - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리
- 즉, `하나의 URL만 가질 수 있음`

### Why routing?
- 동작에 따라 URL이 바뀌어야하나?
  - 유저의 사용성 관점에선 필요함
- Routing이 없다면,
  - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음
  - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
    - 새로고침 시 처음 페이지로 돌아감
    - 링크 공유 시 처음 페이지만 공유가능
  - 브라우저의 뒤로가기 기능 사용 불가

## Vue Router
- Vue의 공식 라우터
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
- 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
  - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능
  - SPA의 단점 중 하나인 `"URL이 변경되지 않는다."를 해결`
- 페이지는 여전히 하나!

> [참고] MPA (Multiple Page Application)
- 여러개의 페이지로 구성된 애플리케이션
- SSR 방식으로 렌더링

### Vue Router 시작하기
```
$ vue create vue-router-app
$ cd vue-router-app
$ vue add router
```
- history mode 사용여부 -> Yes

### History mode
- 브라우저의 History API를 활용한 방식
  - 새로고침 없이 URL 이동 기록을 남길 수 있음
- 우리에게 익숙한 URL 구조로 사용 가능
  - http://localhost:8080/index
- History mode를 사용하지 않으면 
  - Default값인 hash mode로 설정됨 ('#'을 통해 URL을 구분하는 방식)
  - http://localhost:8080#index


### `router-link`
- a태그와 비슷한 기능
  - URL을 이동시킴
  - routes에 등록된 컴포넌트와 매핑됨
  - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
- 목표 경로는 `'to'`속성으로 지정됨
- 기능에 맞게 HTML에서 a태그로 rendering되지만, 필요에 따라 다른 태그로 바꿀 수 있음


### `router-view`
- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미
- router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
- Django의 **block tag**와 비슷
  - **App.vue**는 **base.html**의 역할
  - **router-view**는 **block태그**로 감싼 부분

### src/router/index.js
- 라우터에 관련된 정보 및 설정이 작성되는 곳
- Django에서의 urls.py에 해당
- routes에 URL과 컴포넌트 매핑

### src/Views
- router-view에 들어갈 component 작성
- 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나눠짐
- 각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
- 이제 폴더별 컴포넌트 배치는 다음과 같이 진행 (규약은 아님)
- `views/`
  - **routes에 매핑되는 컴포넌트**,
  - 즉 `<router-view>`의 위치에 렌더링 되는 컴포넌트를 모아두는 폴더
  - 다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것을 권장
  - ex) App 컴포넌트 내부의 AboutView & HomeView 컴포넌트
- `components/`
  - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
  - ex) HomeView 컴포넌트 내부의 HelloWorld 컴포넌트

---

## Vue Router 실습

### 주소를 이동하는 2가지 방법
- 1. 선언적 방식 네비게이션
- 2. 프로그래밍 방식 네비게이션

### 선언적 방식 네비게이션
- router-link `'to'`속성으로 주소 전달
  - routes에 등록된 주소와 매핑된 컴포넌트로 이동

<img src="./Vue_img/vue_router01.png">

- Named Routes
  - 이름을 가지는 routes
    - Django에서 path 함수의 name 인자의 활용과 같은 방식

<img src="./Vue_img/vue_router02.png">

- 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적 작동

<img src="./Vue_img/vue_router03.png">

### 프로그래밍 방식 네비게이션
- Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근 할 수 있음
- 다른 URL로 이동하려면 `this.$router.push`를 사용
  - history **stack**에 이동할 URL을 넣는 (push) 방식
  - history stack에 기록이 남기 때문에 사용자가 브라우저의 **뒤로 가기** 버튼을 클릭하면 이전 URL로 이동 가능
- 결국 `<router-link :to="...">`를 클릭하는 것과 `$router.push(...)`를 호출하는 것은 같은 동작
- 동작원리는 선언적 방식과 같음

<img src="./Vue_img/vue_router04.png">


### Dynamic Route Matching
- 동적 인자 전달
  - URL의 특정 값을 변수처럼 사용 가능
- ex) Django에서의 variable routing

- HelloView.vue 작성 및 route 추가
- route 추가 시, 동적 인자를 명시


<img src="./Vue_img/vue_router05.png">

<img src="./Vue_img/vue_router06.png">

- `$route.params`로 변수에 접근 가능

<img src="./Vue_img/vue_router07.png">

- 다만 HTML에서 직접 사용하기 보다는 data에 넣어서 사용할 것을 권장

<img src="./Vue_img/vue_router08.png">

### Dynamic Route Matching - 선언적 방식 네비게이션
- App.vue에서 harry에게 인사하는 페이지로 이동해보기
- params를 이용하여 동적 인자 전달 가능

<img src="./Vue_img/vue_router09.png">

### Dynamic Route Matching - 프로그래밍 방식 네비게이션
- AboutView에서 데이터를 입력 받아 HelloView로 이동하여 입력받은 데이터에게 인사하기

<img src="./Vue_img/vue_router10.png">

### route에 컴포넌트를 등록하는 또다른 방법
- router/index.js에 컴포넌트를 등록하는 또다른 방식이 주어지고 있음 (about)

<img src="./Vue_img/vue_router11.png">

### lazy-loading
- 모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림
- 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
  - 모든 파일을 한 번에 로드하지 않아도 되기 때문에 최초에 로드하는 시간이 빨라짐
  - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심

---

## Navigation Guard

### 네비게이션 가드
- Vue router를 통해 특정 URL에 접근할 때 **다른 url로 redirect**하거나 **해당 URL로의 접근을 막는** 방법
  - Ex) 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함

- 전역가드
  - 애플리케이션 전역에서 동작
- 라우터 가드
  - 특정 URL에서만 동작
- 컴포넌트 가드
  - 라우터 컴포넌트 안에 정의

## 전역가드
### Global Before Guard
- 다른 url 주소로 이동할때 항상 실행
- router/index.js에 `router.beforeEach()` 를 사용하여 설정
- 콜백 함수의 값으로 3개의 인자를 받음
  - **to** : 이동할 URL 정보가 담긴 Route 객체
  - **from** : 현재 URL 정보가 담긴 Route 객체
  - **next** : 지정한 URL로 이동하기 위해 호출하는 함수
    - 콜백 함수 내부에서 반드시 한 번만 호출되어야 함
    - 기본적으로 to에 해당하는 URL로 이동
- URL이 변경되어 화면이 전환되기 전 router.beforeEach()가 호출됨
  - 화면이 전환되지 않고 대기상태가 됨
- 변경된 URL로 라우팅하기 위해서는 next()를 호출해줘야 함
  - `next()가 호출되기 전까지 화면이 전환되지 않음`



## 라우터 가드
