# Django 01
### 클라이언트와 서버
- 오늘날 대부분 웹서비스는 클라이언트-서버 구조 기반으로 동작
- 클라이언트와 서버는 하나의 컴퓨터
- <img src="./django01_img/cli-ser.png">

- **요청과 응답 !!!**


> 클라이언트
- 웹 사용자의 인터넷에 연결된 장치 (ex. wifi에 연결된 컴퓨터 또는 모바일)
- chrome 또는 firefox와 같은 웹 브라우저
- 서비스를 요청하는 주체

> 서버
- 웹페이지, 사이트 또는 앱을 저장하는 컴퓨터
- 클라이언트가 웹페이지에 접근하려할때 서버에서 클라이언트 컴퓨터로 웹 페이지 데이터를 응답해 사용자의 웹 브라우저에 표시됨
- 요청에 대해 서비스를 응답하는 주체

### Web browser와 Web page
> Web browser
- 웹 브라우저란 웹에서 페이지를 찾아 보여주고, 사용자가 하이퍼링크를 통해 다른 페이지로 이동할 수 있도록 하는 프로그램
- 웹 페이지 파일을 우리가 보는 화면으로 바꿔주는(rendering) 프로그램

> Web page
- 웹에 있는 문서
- 우리가 보는 화면 각각 한장 한장
  - 1. 정적 웹페이지
  - 2. 동적 웹페이지

> 정적 웹페이지
- static web page
- 있는 그대로를 제공하는 것 (served as-is)
- 한번 작성된 html파일 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달
- 서버에 미리 저장된 html 파일 그대로 전달된 웹페이지
- 같은 상황에서 사용자에게 동일 정보 표시

> 동적 웹페이지
- dynamic web page
- 사용자 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹페이지
- 웹 페이지의 내용을 바꿔주는 주체 == 서버
  - 서버에서 동작하고있는 프로그램이 웹 페이지를 변경해줌
  - 이렇게 사용자 요청을 받아 적절한 응답을 만들어주는 프로그램을 쉽게 만들 수 있게 도와주는 프레임워크가 django
  - 다양한 서버 사이드 프로그래밍 언어 사용가능
  - 파일 처리하고 데베와의 상호작용이 이루어짐
  

  ### MTV Design Pattern
- 디자인 패턴이란 각기 다른 기능을 가진 다양한 응용 소프트웨어를 개발할때 공통적인 설계문제 존재, 이를 처리하는 해결책사이에도 공통점 존재
- 이런 유사점이 패턴
- 클라이언트-서버 구조
- 재사용 가능한 해결책
- 시스템 디자인 중 발생하는 공통 문제들을 해결하는데 형식화된 좋은 관행
- 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할수있도록 한 규칙

### Django's Design Pattern

- django에서도 디자인 패턴이 적용되어있음 -> MTV 패턴
- MTV 패턴은 MVC 디자인 패턴을 기반으로 조금 변형된 패턴

> MVC 소프트웨어 디자인 패턴
- Model - View - Controller
- 데이터 및 논리제어를 구현하는데 널리 사용되는 소프트웨어 디자인 패턴
- 하나의 큰 프로그램을 세가지 역할로 구분한 개발 방법론
  - Model : 데이터와 관련된 로직을 관리
  - View : 레이아웃과 화면을 처리
  - Controller : 명령을 model과 view 부분으로 연결
- 목적 - "관심사 분리"
- 더나은 업무 분리와 향상된 관리 제공
- 각 부분 독립적 개발 가능, 하나 수정하고싶을때 모두 건들지 않아도 됨
- == 개발 효율성 및 유지보수 용이
- == 다수 멤버로 개발하기 용이

> Django 에서의 디자인 패턴 ***
- MVC 패턴 기반 MTV 패턴 사용
- MVC :
  - Model (DB)
  - View  (HTML)
  - Controller  (DB, HTML)
- MTV :
  - Model
  - Template
  - View

> MTV 디자인 패턴
- Model
  - MVC 패턴에서 Model의 역할에 해당
  - 데이터와 관련된 로직을 관리
  - 응용프로그램의 데이터 구조를 정의하고 데베의 기록을 관리
- Template
  - 레이아웃과 화면을 처리
  - 화면상의 사용자 인터페이스 구조와 레이아웃을 정의
  - MVC 패턴에서 View
- View
  - Model & Template 관련 로직을 처리해서 응답을 반환
  - 클라이언트 요청에 대해 처리를 분기하는 역할
  - 데이터가 필요하다면 model에 접근해서 데이터를 가져오고
  - 가져온 데이터를 template로 보내 화면을 구성하고
  - 구성된 화면을 응답으로 만들어 클라이언트에게 반환
  - MVC 패턴에서 Controller 역할에 해당
  
### MTV 구조 기억 !!!!!  *****
- <img src="./MTV.png">


### 기본설정
> 프로젝트 구조
- __init__.py : python에게 이 디렉토리를 하나의 python패키지로 다루도록 지시
  - 별도로 추가 코드를 작성하지 않음

- asgi.py : Asynchronous Server Gateway Interface
  - Django 애플리케이션이 비동기식 웹서버와 연결 및 소통하는 것을 도움
  - 추후 배포시 사용

- **settings.py** : Django 프로젝트 설정을 관리

- **urls.py** : 사이트의 url과 적절한 views연결 지정

- wsgi.py : Web Server Gateway Interface
  - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움
  - 추후 배포시 사용

- **manage.py** : Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티


> 애플리케이션 구조


> Project & Application
- Project
  - collection of apps
  - 프로젝트는 앱의 집합
  - 프로젝트에는 여러 앱이 포함될 수 있음
  - 앱은 여러 프로젝트에 있을 수 있음

- Application
  - 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할 담당
  - 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장함
  - 반드시 생성후 등록!!!!!!!!!!!


### 요청과 응답
- **URL -> VIEW -> TEMPLATE** 순의 작성 순서로 코드를 작성해보고 데이터 흐름 이해하기



---

### Django Template
> Variable
- {{ variable }}
- 변수명은 영어, 숫자와 밑줄_ 의 조합으로 구성가능하나 밑줄로는 시작할 수 없음
- 공백이나 구두점 문자또한 사용 불가
- dot(.)을 사용해 변수 속성에 접근 가능
- render()의 세번째 인자로 {'key':value}와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 key에 해당하는 문자열이 template에서 사용가능한 변수명이 됨

> Filters
- {{ variable|filter }}
- 표시할 변수를 수정할 때 사용
- built-in template filters


> Tags
- {{}} : 값을 표현
- tag 사용할 때 {% %} : 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어흐름을 만드는 등 변수보다 복잡한 일 수행
- 일부 태그는 시작과 종료태그 필요 {% if %}{% endif %} / {% for %}{% endfor %}  -> 들여쓰기로 구분해야하는 코드들

> Comments (주석)
- {# #} : 라인 주석
- {% comment %} 여러줄 주석 {% endcomment %}


### Template inheritance
> 템플릿 상속
- 코드의 재사용성에 초점
- 사이트의 모든 공통 요소를 포함하고 하위템플릿이 재정의 할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿을 만들 수 있음

---
### Sending and Retrieving form data
> Client&Server architecture
- 브라우저는 클라이언트!

### Sending form data (Client)
> action
- 목적지 주소
> method
- GET 방식
  - 쿼리 스트링 파라미터 -> '?h1=qwert&a1=2222' == '?key=value&key=value/'

> HTML input's attribute
- **name 필수 !!!**


