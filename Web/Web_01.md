# Web
> 웹 사이트의 구성요소
- 웹 사이트 : 브라우저를 통해서 접속하는 웹 페이지(문서)들의 모음
- 웹 페이지는 글, 그림, 동영상 등 여러가지 정보를 담고 있으며 '링크' 들이 있음. '링크'를 통해 여러 웹 페이지를 연결한 것을 웹 사이트라고함.
- HTML (구조) / CSS (표현) / Javascript (동작)

> 웹 사이트와 브라우저
- 웹 사이트는 브라우저를 통해 동작함
- 브라우저마다 동작이 달라서 문제가 생기는 경우가 많음 (파편화)
- 해결책으로 웹 표준이 등장

> 웹 표준
- 웹에서 표준적으로 사용되는 기술이나 규칙
- 어떤 브라우저든 웹 페이지가 동일하게 보이도록 함 (크로스 브라우징)

---

## **HTML**
> Hyper Text
- 참조 (하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
> Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- ex) HTML, Markdown
- HTML : 웹 페이지를 구성하기 위한 언어
- HTML 스타일 가이드 : 마크업 스타일 가이드 (**2 space**)


> HTML 기본구조
- html : 문서 최상위(root) 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소, 실제 화면 구성과 관련된 내용

> head
- \<title\>
- \<meta\>
  - ex) Open Graph Protocol
  - : 메타 데이터를 표현하는 새로운 규약
  -   HTML 문서의 메타 데이터를 통해 문서 정보를 전달
  -   메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의
- \<link\>
- \<script\>
- \<style\>

> HTML 요소 (elements)
- ```python
  <h1>contents</h1>
  ```
- 시작 태그와 종료 태그, 그리고 사이에 위치한 내용으로 구성
- 요소는 태그로 컨텐츠를 감싸는 것, 그 정보로 성격과 의미를 정의
- 내용이 없는 태그들도 존재 (닫는 태그 x)
  - br, hr, img, input, link, meta
- 요소는 중첩될 수 있음
- 여는 태그와 닫는 태그 쌍을 잘 확인
  - 오류 반환이 아니라 그냥 레이아웃이 깨져서 출력되므로 디버깅 어려움
- 개발자 도구

> 속성 (attribute)
- ```python
  <a href="https://google.com"</a>
  ```
- 태그마다 사용가능한 속성이 다름  
- 공백 NO! , ""(쌍따옴표) 사용!
- 태그의 부가적인 정보 설정
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적 정보 제공
- 요소 시작 태그에 작성, 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성 (HTML Global Attiribute)들도 있음

> HTML Global Attribute
-  모든 HTML요소가 공통으로 사용할 수 있는 대표적 속성
-  id : 문서 전체에서 유일한 고유 식별자 지정
-  class : 공백으로 구분된 해당 요소의 클래스 목록 (CSS, JS에서 요소를 선택하거나 접근)
-  data-* : 페이지에 개인 사용자 정의 데이터를 저장
-  style : inline 스타일
-  title : 요소에 대한 추가 정보 지정
-  tabindex : 요소의 탭 순서 

> HTML 코드예시
- ```python
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Document</title>
  </head>
  <body>
    <!-- 이것은 주석입니다. -->
    <h1>나의 첫번째 HTML</h1>
    <p>이것은 본문입니다.</p>
    <span>이것은 인라인요소</span>
    <a href="https://www.naver.com">네이버로 이동!!</a>
  </body>
  </html>
  ```

> 시맨틱 태그
- HTML 태그가 특정 목적, 역할 및 의미적 가치를 가지는 것
- h1 태그 : 최상위 제목인 텍스트를 감싸는 역할
- Non semantic 요소 : div, span
- a, form, table 태그들도 시맨틱 태그
- 대표적 시맨틱 태그 :
  - header : 문서 전체나 섹션의 헤더
  - nav : 내비게이션
  - aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - section : 문서의 일반적 구분, 컨텐츠 그룹을 표현
  - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - footer : 문서 전체나 섹션의 푸터 (마지막 부분)
- 사용해야하는 이유 :
    - 의미론적 마크업 :
    - 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
    - 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가진 태그들을 활용하기 위한 노력
    - 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게함
    - 검색 엔진 최적화 (SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야함

> 텍스트 코드 to 웹사이트
- 렌더링 (Rendering) : 웹사이트 코드를 사용자가 보게되는 웹사이트로 바꾸는 과정
- DOM (Document Object Model) 트리 :
  - 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML 문서에 대한 모델을 구성
  - HTML 문서 내의 각 요소에 접근/수정에 필요한 프로퍼티와 메서드 제공
  - 같은 들여쓰기에 있으면 형제


## HTML 문서 구조화

> 인라인 / 블록 요소
- HTML 요소는 크게 인라인 / 블록 요소로 나눔
- 인라인 요소는 **글자처럼** 취급 (둘이 동일하단 것은 아님)
- 블록 요소는 **한 줄 모두** 사용

> 텍스트 요소 (인라인 요소)
- \<a\>\</a\> : href속성 활용하여 다른 URL로 연결하는 하이퍼링크 생성
- \<b\>\</b\> : 굵은 글씨 요소
- \<strong\>\</strong\> : 중요한 강조하고자 하는 요소 (굵은) - **시맨틱**
- \<i\>\</i\> : 기울임 글씨 요소
- \<em\>\</em\> : 중요한 강조하고자 하는 요소 (기울임) - **시맨틱**
- \<br\> : 텍스트 내에 줄 바꿈 생성
- \<img\> : src속성을 활용하여 이밎 표현
- **\<span\>\</span\> : 의미없는 인라인 컨테이너**


> 그룹 컨텐츠 (블록 요소)
- \<p\>\</p\> : 하나의 문단
- \<hr\> : 문단 레벨 요소에서의 주제의 분리, 수평선으로 표현
- \<ol\>\</ol\> : 순서가 있는 리스트
- \<ul\>\</ul\> : 순서가 없는 리스트
- \<pre\>\</pre\> : HTML에 작성한 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백문자를 유지
- \<blockquote\>\</blockquote\> :  택스트가 긴 인용문, 주로 들여쓰기를 한 것으로 표현됨
- **\<div\>\</div\> : 의미없는 블록 레벨 컨테이너**


> form (중요!!! - django)
- \<form\>은 정보를 서버에 제출하기위해 사용하는 태그
- ex) 로그인창
- action : form을 처리할 서버의 URL (데이터를 보낼 곳)
  - ex) 네이버, 구글
- method : form을 제출할 때 사용할 HTTP메서드 (GET, POST)
- enctype : method가 post인 경우 데이터의 유형
  - application/x-www-form-urlencoded : 기본값
  - multipart/form-data: 파일 전송시 (input type이 file인 경우)
- ```python
  <form>action="/search" method="GET">
  </form>
  ```

> Input (중요!!! - django)
- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨
- name : form control에 적용되는 이름 (이름/값 페어)
- value : form control에 적용되는 값 (이름/값 페어)
- required, readonly, autofocus, autocomplete, disabled 등
- ```python
  <form action="/search" method="GET">
    <input type="text" name="q">
  </form>
  ```

> Input label
- label을 클릭하여 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
- 사용자는 선택할 수 있는 영역이 늘어나 웹/모바일 환경에서 편하게 사용 가능
- label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인 할 수 있도록 함
- \<input\>에 id속성을, \<label\>에는 for속성을 활용, 상호연관
- ```python
  <label for="agreement">개인정보 수집에 동의합니다.</label>
  <input type="checkbox" name="agreement" id="agreement">
  ```
> input 유형 - 일반
  - 일반적으로 입력을 받기 위해 제공되며 타입별로 HTML기본 검증 혹은 추가 속성 활용가능
  - text : 일반 텍스트 입력
  - password : 입력 시 값이 보이지않고 문자를 특수기호(*)로 표현
  - email : 이메일 형식이 아니면 form 제출 불가
  - number : min, max, step속성을 활용하여 숫자 범위 설정 가능
  - file : accept 속성을 활용하여 파일 타입 지정 가능

> input 유형 - 항목 중 선택
- 일반적으로 label 태그와 함께 사용하여 선택항목 작성
- 동일 항목에 대해선 name을 지정하고 선택 항목에 대한 value지정해야함
  - checkbox : 다중선택
  - radio : 단일 선택
  - ```python
    <div>
      <p>checkbox</p>
      <input id="html" type="checkbox" name="language" value="html">
      <label for="html">HTML</label>
      ...
    </div>  
    ```

> input 유형 - 기타
- 다양한 종류의 input을 위한 picker제공
  - color : color picker
  - date : date picker
- hidden input을 활용하여 사용자 입력을 받지않고 서버에 전송되어야하는 값을 설정
  - hidden : 사용자에게 보이지 않는 input

## **CSS**

> CSS
- 스타일을 지정하기 위한 언어
- 선택하고, 스타일을 지정한다
  - ```python
    h1{
      color: blue;
      font-size: 15px;
    }
    ```
- 선택자를 통해 스타일 지정할 HTML요소 선택
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍을 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 : 어떤 스타일 기능을 변경할지
  - 값 : 어떻게 스타일 기능을 변경할지


> CSS 정의 방법
- 인라인 (inline)
  - ```python
    <h1 style="color:blueviolet; font-size:100px;">오옹오오오옹</h1>
    ```

- 내부참조 (embedding) - \<style\>
  - ```python
    <style>
        h1 {
            color:red;
            font-size: 40px;

        }

    </style>
    ```
- 외부참조 (link file) *** - 분리된 CSS 파일
  - ```python
    <link rel="stylesheet" href="mystyle.css">
    ```

> **CSS Selectors** (중요 !!!!! *****)
- 기본 선택자
  - 전체 선택자, 요소 선택자 (HTML 태그를 직접 선택)
  - 클래스 선택자 (마침표. 문자로 시작, 해당 클래스가 적용된 항목을 선택), 아이디 선택자 (#문자로 시작, 해당 아이디가 적용된 항목 선택, **일반적으로 하나의 문서에 1번만 사용** (중복 x), 여러번 사용해도 동작하지만 단일 id사용을 권장), 속성 선택자
  - ```python
    * {
      color: red;     # 전체 선택자 
    }

    h2 {
      color: orange;    # 요소 선택자
    }

    h3,
    h4 {
      font-size: 10px;
    }

    .green {
      color: green;     # 클래스 선택자
    }

    #purple {
      color: purple;    # id 선택자
    }
    ```
- 결합자 (combinators)
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자
  - ```python
    .box > p {
      font-size: 30px;
    }

    .box p {
      color: blue;
    }
- 의사 클래스/요소
  - 링크,동적 의사 클래스
  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자



> **CSS 적용 우선순위 (cascading order)** (중요!!!!!!*******)
- !important -> inline -> id -> class -> 요소 -> 소스
- 범위가 좁을수록 강하다!!!
```python
<p>1</p>  # h2
<p class="blue">2</p>   #.blue
<p class="blue green">3</p>   # .green 
<p class="green blue">4</p>   # .green
<p id="red" class="blue">5</p>    # #red
<h2 id="red" class="blue">6</h2>    # h2 (!important)
<p id="red" class="blue" style="color: yellow;">7</p>   # inline
<h2 id="red" class="blue" style="color: yellow;">8</h2>   # !important

-----------------------------------------------------------------

h2 {
  color: darkviolet !important;
}

p {
  color: orange;
}

.blue {
  color: blue;
}

.green {
  color: green;
}

#red {
  color: red;
}
```

> CSS 상속
- 상속을 통해 부모요소 속성을 자식에게 상속
- 상속되는 것 :
  - **Text 관련요소** (font, color, text-align), opacity, visibility
- 상속 안되는 것:
  - Box model 관련요소 (width, height, margin, padding, border, box-sizing, display), position 관련요소 (position, top/right/bottom/left, z-index)
- ```python
  <body>
    <p>안녕하세요! <span>테스트</span> 입니다.</p>
  </body>


  <style>
  p {
    color: red;   # 상속됨

    border: 3px solid black;    # 상속 안됨
  }

  span {

  }
  </style>
  ```  

> CSS 기본 스타일
- 크기단위
  - px (픽셀)
    - 모니터 해상도의 한 화소인 픽셀 기준
    - 픽셀의 크기는 변하지 않기 때문에 고정적 단위
  - %
    - 백분율 단위
    - 가변적인 레이아웃에서 자주 사용
    - 부모 요소의 %
  - em
    - (바로 위, 부모 요소에 대한) 상속의 영향을 받음
    - 배수단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
  - rem
    - 상속의 영향을 받지 않음
    - 최상위 요소 (html)의 사이즈를 기준으로 배수 단위를 가짐
  ```python
  <style>
    .font-big {
      font-size: 36px
    }
    .em {
      font-size: 2em;
    }
    .rem {
      font-size: 2rem;
    }
  </style>


  <body>
    <ul class="font-big"> # 36px  
      <li class="em">2em</li>   # 36 *2 px 
      <li class="rem">2rem</li>   # 16px * 2 px
      <li>no class</li>   # 36px
    </ul>
  </body>
  ```

> 크기단위 (viewport)
- 웹 페이지를 방문한 유저에게 바로 보이게되는 웹 컨텐츠의 영역 (디바이스 화면)
- **디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨**
- **vw** (브라우저 크기에 따라 크기가 변함), vh, vmin, vmax

> 색상단위
- 색상키워드
  - 대소문자 구분 x
  - red, blue, black 같은 특정 색을 직접 글자로 나타냄
- RGB 색상
  - 16진수 표기법 혹은 함수형 표기법 사용하여 특정 색 표현
- HSL 색상
  - 색상, 채도, 명도를 통해 특정색 표현


---

> 결합자 심화
- 자손 결합자
  - selectorA 하위의 모든 selectorB 요소
  - ```python
    <style>
      div span {
        color: red;
      }
    </style>
    ```
- 자식 결합자
  - selectorA 바로 아래의 selectorB 요소
  - ```python
    <style>
      div > span {
        color: red;
      }
    </style>
    ```
- 일반 형제 결합자
  - selectorA의 형제 요소 중 뒤에 위치하는 selectorB요소를 모두 선택
  - ```python
    p ~ span {
      color: red;
    }
    ```

- 인접 형제 결합자
  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택
  - ```python
    p + span {
      color: red;
    }
    ```

> CSS Box model
- 모든 HTML 요소는 네모(박스모델)
- **위에서부터 아래로, 왼쪽에서 오른쪽으로** 쌓인다 (Normal flow)
  - content : 실제 내용
  - border : 테두리
  - padding : 내용과 테두리 사이
  - margin : 테두리 바깥
- margin shorthand
  - .margin {margin: 10px;}
  - .margin {margin: 10px 20px;} # 상하 / 좌우
  - .margin {margin: 10px 20px 30px;} # 상 / 좌우 / 하
  - .margin {margin: 10px 20px 30px 40px;}  # 상 / 우 / 하 / 좌
- border shorthand (순서 상관 x)
  - .border {border: 2px dashed black;}  # width / style / color


> **box-sizing** (중요 !!!***)
- 기본적으로 모든 요소의 box-sizing은 content-box
- padding을 제외한 **순수 contents 영역만을 box로 지정**
- 다만, 일반적으로 영역을 볼때는 border까지의 너비를 100px 보는 것을 원함
- 그경우 box-sizing을 border-box로 설정


> CSS Display
- display : block
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- display : inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - content 너비만큼 가로 폭을 차지
  - width, height, margin-top, margin-bottom 을 지정할 수 없다
  - 상하 여백은 line-height로 지정
- display : inline-block
  - inline처럼 한줄에 표시 가능, block처럼 width,height,margin 속성 모두 지정 가능
- **display : None**
  - 화면에 표시하지않고, 공간조차 부여 x
  - **visibility: hidden**과 비교! (공간은 차지하나 화면에 표시만 하지 않음)

> 블록 레벨 요소와 인라인 레벨 요소
- 블록 레벨 요소
  - div / ul, ol, li / p / hr / form
- 인라인 레벨 요소
  - span / a / img / input, label / b, em, i, strong


> 속성에 따른 수평 정렬
- margin-right: auto; / margin-left: auto; / margin-right: auto; margin-left: auto;
- text-align: left; / text-align: right; / text-align: center; (블럭요소 적용)




> CSS Position
- 레이아웃 설정할 때
- 문서 상에서 요소의 위치 결정
- static : 모든 태그의 기본값
- **relative (상대위치)** - normal flow 유지, 실제위치는 그대로 (**원래자리 남겨두고 이동**)
- **absolute (절대위치)** - normal flow에서 벗어남(요소를 일반 문서 흐름에서 제거 후 레이아웃에 공간을 차지 하지 않음), 다음 블록 요소가 좌측 상단으로 붙음 **(원래 자리 남겨두지 않고, static이 아닌 부모요소(relative로 만든다!)를 기준으로 이동 /  전부 다 아니라면 body를 기준으로 이동)**
- fixed (고정위치) - 우리가 보고있는 화면을 기준으로! (스크롤해도 이동 x)
- sticky (스크롤에따라 static->fixed)


> CSS 원칙
- 원칙 1,2 : Normal flow
  - 모든 요소는 박스모델, 좌측 상단에 배치
  - display에 따라 크기와 배치가 달라짐
- 원칙 3 : position으로 위치 기준 변경
  - relative : 본인 원래 위치
  - absolute : 특정 부모 위치
  - fixed : 화면 위치
  - sticky : 기본적으로 static, 스크롤 이동에 따라 fixed