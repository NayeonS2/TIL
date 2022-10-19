# 그리드 시스템/ 반응형 웹

> CSS layout techniques

- Display
- Position
- Float
- Flexbox
- Grid
- 기타 (Responsive Web Design, Media Queries)

> Float

- CSS 원칙 1
  
  - **Normal Flow** : 쌓이는 것! 공간차지를 하는 것! (둥둥 뜨는 건 normal flow를 벗어난 것!!!!)
    - relative는 자기 자리 유지하며 움직이지만
    - absolute는 아예 움직임, 다른애들이 자리 차지 가능!
    - Inline Direction : 좌측에서 우측으로 쌓임
    - Block Direction : 위에서 아래로 쌓임
  - 모든 요소는 네모, 위에서 아래로 왼쪽에서 오른쪽으로
  - 좌측상단에 배치
  - 우리가 원하는 배치가 어려움! (어떤요소를 감싸는 배치? 좌/우측에 배치?)

- Float란 : 
  
  - 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping하도록 함
  - 요소가 Normal flow를 벗어나도록 함
  - box 자체는 원래 자리에서 벗어나서, normal flow를 벗어나지만,
  - 주변 텍스트들이 wrappinig을 해서 normal flow가 유지되는 것처럼 보임!
  - Float 속성
    - none : 기본값
    - left : 요소를 왼쪽으로 띄움 (붕 뜬것!)
    - right : 요소를 오른쪽으로 띄움 (붕 뜬것!)

> **Flexbox**

- CSS Flexible Box Layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델

- 축
  
  - **main axis (메인 축)** - 꼬지(--1-2-3-->)를 생각해!
  - **cross axis (교차 축)** - main axis에서 수직

- 구성 요소
  
  - Flex Container (부모 요소) - **부모요소에 flex 적용!!!**
  
  - Flex item (자식 요소)
  
  - flex-direction : default값은 row (--1-2-3-->)
  
  - Flex 속성
    
    - [배치 설정]
      
      - **flex-direction** (메인 축에 따라 cross 축도 바뀜!!!)
        - 1) row
        - 2) row-reverse
        - 3) column
        - 4) column-reverse
      - flex-wrap
        - 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정 (기본적으로 컨테이너 영역을 벗어나지 않도록)
        - wrap : 튀어나올 것 같으면 줄바꿈 
        - nowrap : 벗어나도 그냥 한줄에 끼워넣기
      - flex-flow
        - flex-direction과 flex-wrap의 shorthand
        - flex-flow: row nowrap;
    
    - [공간 나누기]
      
      - **justify-content** (main) : **main axis 기준** 공간 배분 (꼬지 방향!!)
        - 1) flex-start (좌측)
        - 2) flex-end (우측)
        - 3) center (센터)
        - 4) space-between (좌 중앙 우)
        - 5) space-around (요소를 둘러싼 좌우 여백을 똑같이 배분 1:2:2:1)   
        - 6) space-evenly (여백을 똑같이 배분)
      - **align-content** (cross)
        - 1) flex-start (위)
        - 2) flex-end (아래)
        - 3) center (중앙)
        - 4) space-between
        - 5) space-around
        - 6) space-evenly
    
    - [정렬]
      
      - **align-items** (모든 아이템) - **cross axis 기준**
        
        - 1) stretch (컨테이너 가득 채움)
        - 2) flex-start
        - 3) flex-end
        - 4) center
        - 5) baseline (글자 선 맞춰서)
      
      - align-self (개별 아이템!) - cross axis 기준
        
        - 1) stretch
        - 2) flex-start
        - 3) flex-end
        - 4) center
    
    - 기타 속성
      
      - flex-grow : 남은 영역을 아이템에 분배
      - order : 배치순서
    
    - ** 중앙정렬 공식 display: flex / justify-content: center / align-items: center

---

> Bootstrap

- Non bootstrap heading vs. Bootstrap heading
  - 글자가 조금 더 크고, 마진은 bottom만 존재
- CDN 통해 가져오기! (link는 closing head위/ script는 closing body위)

> Spacing (Margin and padding)

- {property}{sides}-{size}
- css는 개발자들이 다만들어놔서 **클래스만 지정**해주면됨!!!!
- \<div class="mt-3 ms-5"\>bootstrap-spacing\</div\>
- property : margin or padding
- sides : 
  - t (top) / b (bottom) / s (start) / e (end) / x (left, right) / y (top, bottom) / blank (4sides)
- size : (1, 0.25 rem, 4px) ... 사이즈 외우기!
- mx-auto : 가운데정렬 / ms-auto : 오른쪽정렬

> Color

- \<div class="bg-primary"\>이건 파랑\</div\>
- \<p class="text-success"\>이건 초록색\</p\>

> Text

- \<p class="text-start"\>이건 왼쪽\</p\>
- \<a href-"#" class="text-decoration-none text-dard"\>Non-underline-Link\</a\>
- \<p class="fw-bold"\>Bold text\</p\>
- \<p class="fw-normal"\>Normal weight text\</p\>

> Position

- \<div class="box fixed-top"\>fixed-top\</div\>
- \<div class="box fixed-bottom"\>fixed-bottom\</div\>

> Display

- .d-{value}

- \<div class="d-inline p-2 text-bg-primary"\>d-inline\</div\>

- \<div class="d-inline p-2 text-bg-dark"\>d-inline\</div\>

- \<div class="d-none p-2 text-bg-primary"\>d-inline\</div\>

- ```html
  <div class="bigbox position-relative">
    <div class="box position-absolute top-0 start-0">top0/start0</div>
  </div>
  ```

- ```html
  <div class="box bg-warning d-sm-none d-md-block">보이나 안보이나</div>
  ```
  
  > 컴포넌트
  
  - Buttons
  - Dropdown
  - Form
  - navbar
  - Carousel (슬라이드가 넘어가는 것)
  - Modal *
  - Flexbox
  - Card (Grid card) - 반응형 (화면 줄어들면 모양 바뀜)

> Responsive web (***)

> *****Bootstrp Grid system ** (중요!!!!!!!!!)

- flexbox로 제작됨
- container, rows, column 으로 컨텐츠 배치, 정렬
- column : 실제 컨텐츠를 포함하는 부분
- gutter : 칼럼과 칼럼 사이의 공간
- container : column들을 담고있는 공간
- 12개의 column
- 6개의 grid breakpoints
  - None / sm / md / lf / xl / xxl

> Grid system breakpoints

- 한줄에 12칸 맞춰서 동작
- ```html
  <div class="row">
    <div class="box col-2 col-sm-8 col-md-4 col-lg-5">1</div> 
    <div class="box col-8 col-sm-2 col-md-4 col-lg-2">2</div> 
    <div class="box col-2 col-sm-2 col-md-4 col-lg-5">3</div>     
  </div>  
  사이즈별로 동작 설정 (2:8:2 / 8:2:2 / 4:4:4 / 5:2:5)
  ```
- nesting
- offset