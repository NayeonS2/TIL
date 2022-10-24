# JavaScript

## DOM

### 개요
- "브라우저에서의 JavaScript"
  - 웹 페이지에서 복잡한 기능을 구현하는 스크립트 언어
  - 정적인 정보만 보여주는 것이 아닌 주기적으로 갱신되거나, 사용자와 상호작용이 가능하거나, 애니메이션이 적용된 그래픽 등에 관여
> [참고] 스크립트 언어 (Script Language)
- 응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어

### Browser APIs
- 웹 브라우저에 내장된 API로, 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러가지 유용하고 복잡한 일을 수행
- 종류
  - `DOM`
  - Geolocation API
  - WebGL

### DOM
- 문서 객체 모델 (Document Object Model)
- 문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
  - 문서 구조, 스타일, 내용 등을 변경할 수 있게 도움
  - HTML 콘텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있음
- 문서가 구조화되어 있으며 각 요소는 `객체(object)`로 취급
- 단순한 속성 접근, 메서드 활용 뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- DOM은 문서를 논리 트리로 표현
- DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 문서의 구조, 스타일, 컨텐츠를 변경 가능


- 웹 페이지는 일종의 문서
- 이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함
- DOM은 동일한 문서를 표현하고, 저장하고, 조작하는 방법을 제공
- DOM은 웹 페이지의 객체 지향 표현이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정 가능

### DOM에 접근하기
- 모든 웹 브라우저는 스크립트 언어가 손쉽게 웹 페이지의 요소에 접근할 수 있도록 만들기 위해 DOM 구조를 항상 사용
- `DOM의 주요 객체들`을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음

### DOM의 주요 객체
- `window`
- `document`
- navigator, location, history, screen 등

### `window` object
- DOM을 표현하는 창
- 가장 최상위 객체 (작성 시 생략 가능)
- 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄



### `document` object
- 브라우저가 불러온 웹 페이지
- 페이지 컨텐츠의 진입점 역할을 하며, <body>등과 같은 수 많은 다른 요소들을 포함
- document는 window의 속성임

> [참고] 파싱 (Parsing)
- 구문 분석, 해석
- 브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정
- PARSE - STYLE - LAYOUT


## DOM 조작

### 개요
- Document가 제공하는 기능을 사용해 웹 페이지 문서 조작하기
- DOM 조작 순서
  - 1)`선택 (Select)`
  - 2)`조작 (Manipulation)`
      - 생성, 추가, 삭제 등

### 선택 관련 메서드
- document.querySelector(selector)
  - 제공한 선택자와 일치하는 element 한 개 선택
  - 제공한 CSS selector를 만족하는 첫번째 element를 반환 (없다면 null 반환)
- document.querySelectorAll(selector)
  - 제공한 선택자와 일치하는 여러 element 선택
  - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
  - 제공한 CSS selector를 만족하는 NodeList를 반환




---


## Event
- 프로그래밍하고 있는 시스템에서 일어나는 사건(action) 