# OOP

> 객체 지향 프로그래밍

- 컴퓨터 프로그래밍의 패러다임 (방법론) 중 하나

- 컴퓨터 프로그램을 명렁어의 목록으로 보는 시각에서 벗어나

- 여러개 독립된 단위, 객체들의 모임으로 파악

- 각각의 객체는 메세지 주고받고 데이터 처리 가능

- 프로그램을 여러개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법 

- ex) 콘서트 - 가수 객체, 감독 객체, 관객 객체

- 정보와 행동을 묶어둔 것 (변수 + 함수)

- data와 method들을 하나의 object로 묶음

- 데이터와 기능(메서드) 분리/ 추상화된 구조 (인터페이스) - 복잡한거 숨기고 필요한거 드러냄

> 절차지향 프로그래밍

- global data -> function 1 / function 2/ ...

- 하나를 고치면 다 바꿔야하는 번거로움 (데이터와 함수로 인한 변화)

- 그래서 객체 지향에서는 데이터와 기능(메서드) 분리/ 추상화된 구조 (인터페이스)

> 객체지향 프로그래밍이 필요한 이유

- 현실 세계를 프로그램 설계에 반영 (추상화)

- 각자의 기능을 다 알지 못해도 꾸러미만 들고와서 사용가능 (가수.노래부르기())

> 객체지향의 장단점

- 장점
  
  - 클래스 단위로 모듈화시켜 개발 가능
  
  - 많은 인원이 참여하는 대규모 소프트웨어 개발에 적합
  
  - 필요한 부분만 수정하기 쉽기에 프로그램 유지보수가 쉬움

- 단점
  
  - 설계 시 많은 노력과 시간이 필요
  
  - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력 필요
  
  - 실행속도가 상대적으로 느림
  
  - 절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도가 빠름

---

> 객체 (컴퓨터 과학)

- 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당된 것
- 변수/ 자료구조/ 함수/ 메서드
- **속성** (변수)과 **행동** (함수-메서드)으로 구성된 모든 것

- ex) 이찬혁.랩하기() = 어!느새 부터! / 이찬혁.직업 = 가수

- 파이썬은 모든 것이 객체(object)

- 리스트.정렬() == 객체.행동()

- 문자열.대문자로() == 객체.행동()

- 정보 예시 - 문자열은 immutable, iterable

> 클래스와 객체

- ex) 클래스 (설계도) : 가수 / 객체 (실제 사례) : 이찬혁

- **클래스 = 타입 (ex. list)**

- 클래스를 만든다 == 타입을 만든다

> 객체와 인스턴스

- **클래스로 만든 객체**를 **인스턴스** 라고도 함 (특정 타입의/*클래스의! 인스턴스*)

- ex) 이찬혁은 객체다 O / 이찬혁은 인스턴스다 X/ **이찬혁은 가수의 인스턴스다 O**

- 타입(클래스)과 실제 사례(값)
  

- [1,2,3],[1],[],['hi'] <- 모두 리스트 타입(클래스)의 객체 (*리스트의 인스턴스*)

- ",'hi','파이썬' <- 모두 문자열 타입(클래스)의 객체 (*스트링의 인스턴스*)

- **객체는 특정 타입의 인스턴스**이다.

- 123, 900, 5 는 모두 *int의 인스턴스*

- 'hello', 'bye' 는 모두 *string의 인스턴스*

- [232, 89, 1], [] 은 모두 *list의 인스턴스*

> 객체의 특징

- 타입(type) : 어떤 연산자(operator)와 조작(method)이 가능한가?

- 속성(attribute) : 어떤 상태(데이터)를 가지는가?

- 조작법(method) : 어떤 행위(함수)를 할 수 있는가?

- 객체(object) = 속성(attribute) + 기능(method)

- "banana".upper() 
  
  - "banana" : 문자열 타입의 인스턴스
  
  - .upper() : 행동 (함수 메서드)

---

> 객체와 클래스 문법

- 기본문법
  
  - 클래스 정의  (설명을 적어 놓은 것)
    
    - 클래스 생성시 대문자 우선 
    
    - Pascal case : 단어의 첫글자는 대문자 (MyClass)
    
    - ```python
      Class MyClass:
      ```
  
  - 인스턴스 생성
    
    - ```python
      my_instance = MyClass()
      ```
  
  - 메서드 호출 (인스턴스.메서드명())
    
    - Snake case (def my_class : 함수형성 시에는 언더바로 단어 묶음)
    
    - ```python
      my_instance.my_method()
      ```
  
  - 속성 (인스턴스.변수명)
    
    - ```python
      my_instance.my_attribute
      ```

> 클래스와 인스턴스

- 객체의 설계도(클래스)를 가지고, 객체(인스턴스)를 생성

- 클래스 : 객체들의 분류/ 설계도

- 인스턴스 : 하나하나의 **실체**/ 예

- ```python
  Class Person:   # 설계도 정의
      pass
  
  print(type(Person)) # <class 'type'>
  
  person1 = Person()
  
  print(isinstance(person1, Person) # True
  print(type(person1)) # <class '__main__.Person'>
  ```

- 파이썬은 모든 것이 객체, 모든 객체는 특정 타입의 인스턴스

> 객체 비교하기

- ==
  
  - 동등한(equal)
  
  - 변수가 참조하는 객체가 동등(*내용이 같은*) 경우 True
  
  - 생긴게 같지만 다른사람 (쌍둥이)
  
  - 두 객체가 같아보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님

- is
  
  - 동일한 (identical)
  
  - 두 변수가 *동일한 객체*를 가리키는 경우 True

- ```python
  a = [1,2,3]  # 실제론 다른 방 사용
  b = [1,2,3]
  
  print(a == b, a is b) # True False
  
  a = [1, 2, 3]
  
  b = a  # 주소가 동일
  
  print(a == b, a is b) # True True
  ```

> 속성 (데이터, 정보, 상태)

- 데이터를 저장하는 변수 (**공용: 클래스 변수/ 개인: 인스턴스 변수**)

- 특정 데이터 타입/ 클래스의 객체들이 가지게 될 상태/데이터를 의미

- 클래스 변수/ 인스턴스 변수가 존재

- ```python
  class Person:
      blood_color = 'red' # 클래스 변수 (같이 사용)
      population = 100
  
      def __init__(self, name):
          self.name = name  # 인스턴스 변수 (각자 사용)
  person1 = Person('지민')
  print(person1.name) #지민
  ```

- 객체는 정보와 행동 ! / 정보는 클래스변수와 인스턴스 변수!!

> 인스턴스 변수

- **self.변수명** 인경우

- 인스턴스가 개인적으로 가지고 있는 속성(attribute) (ex. 뽀삐)

- 각각 인스턴스마다 인스턴스 변수가 다 따로 저장

- 각 인스턴스들의 고유 변수

- 생성자 메서드(__init__)에서 self.<name>으로 정의

- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당

- ```python
  class Person:
  
      def __init__(self, name, #mbti):    # 인스턴스 변수 정의
          self.name = name
         #self.mbti = mbti
  
  john = Person('john')        # 인스턴스 변수 접근 및 할당
  print(john.name) # john
  john.name = 'John Kim' # 변수 접근
  print(john.name) #John Kim
  john.age = 20 # 변수 생성
  print(john.age)
  ```


> 클래스 변수

- 한 클래스의 모든 인스턴스가 공유하는 값

- 같은 클래스의 인스턴스들은 같은 값을 갖게 됨

- 클래스 선언 내부에서 정의

- \<classname>.\<name> 으로 접근 및 할당

- 클래스 변수 변경은 항상 클래스.클래스변수 형식으로 변경

```python
class Circle():
  pi = 3.14   # 클래스 변수 정의 (공용) # 변수명만 있으면 됨!

  def __init__(self, r):
      self.r = r    # 인스턴스 변수 (개인용) # 누구의 것인지 적어줘야함!

c1 = Circle(5)
c2 = Circle(10)

print(Circle.pi) # 3.14  
print(c1.pi) # 3.14  인스턴스 변수 x -> 클래스 변수 찾기 가능
print(c2.pi) # 3.14  인스턴스 변수 x -> 클래스 변수 찾기 가능

Circle.pi = 5  # 클래스 변수 바꾸면 다같이 바뀜 (공통)
print(Circle.pi) #5
print(c1.pi) # 5
print(c2.pi) # 5 

c2.pi = 5 # 인스턴스 변수 변경
print(Circle.pi) # 3.14 (클래스 변수)
print(c1.pi) # 3.14 (클래스 변수)
print(c2.pi) # 5 (새로운 인스턴스 변수 생성)
```

> 클래스 변수 활용 (사용자 수 계산)

- 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록

- 클래스 변수는 앞에 클래스 명을 붙이는게 일반적!

- ```python
  class Person:
      count = 0
      # 인스턴스 변수 설정
      def __init__(self, name):
          self.name = name
          Person.count += 1  # 클래스 변수는 앞에 클래스 명 붙여줌
  
  person1 = Person('아이유')
  person2 = Person('이찬혁')
  
  print(Person.count)
  ```

> 메서드

- 특정 데이터 타입/ 클래스의 객체에 공통적으로 적용 가능한 행위 (함수)

```python
  class Person:
      def talk(self):
          print('안녕')

      def eat(self, food):
          print(f'{food}를 냠냠')
  person1 = Person()
  person1.talk() # 안녕
  person1.eat('피자') # 피자를 냠냠
```

> 메서드의 종류

- 인스턴트 메서드

- 클래스 메서드

- 정적 메서드 (나머지)

> 인스턴트 메서드

- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메서드

- 클래스 내부에 정의되는 메서드의 기본

- *호출시, 첫번째 인자로 자기자신이(self) 전달됨*

- **self**가 있으면 인스턴스 메서드 !!!!!

- ```python
  class MyClass:
  
      def instance_method(self, arg1, ...):
  
  my_instance = MyClass()
  my_instance.instance_method(...)
  ```

> self

- 인스턴스 자기자신

> 생성자(constructor) 메서드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드

- 인스턴스 변수들의 초기값을 설정
  
  - 인스턴스 생성
  
  - ______init_______ 메서드 자동 생성

> 매직메서드

- Double underscore(____) **던더**가 있는 메서드는 특수한 동작을 위해 만들어진 메서드

- 스페셜 메서드 or 매직 메서드

- 특정 상황에 자동으로 불리는 메서드

- 객체의 특수 조작 행위를 지정 (함수, 연산자 등)

- ___str___ : 해당 객체의 출력 형태 지정, 프린트함수 호출 할때 자동호출, 어떤 인스턴스 출력하면 str의 return값이 출력

- __gt__ : 부등호 연산자 (>, greater than)

> 소멸자(destructor) 메서드

- 인스턴스 객체가 소멸되기 직전 호출되는 메서드

- ```python
  class Person:
      def __del__(self):
          print('인스턴스가 사라졌습니다.')
  person1 = Person()
  
  del person1 # 인스턴스가 사라졌습니다.
  ```

> 매직 메서드 예시

- ```python
  class Circle:
      def __init__(self, r):
          self.r = r
      def area(self):
          return 3.14 * self.r * self.r
      def __str__(self):
          return f'[원] radius: {self.r}'
      def __gt__(self, other):
          return self.r > other.r
  
  c1 = Circle(10)
  c2 = Circle(1)
  
  print(c1) # [원] radius: 10
  print(c2) # [원] radius: 1
  print(c1 > c2) # True
  print(c1 < c2) # False
  ```

- 인스턴스메서드 > 매직메서드 포함

> 클래스 메서드

- 클래스가 사용할 메서드

- @classmethod 데코레이터를 사용하여 정의

- 호출 시, 첫번째 인자로 클래스(cls)가 전달됨

- ```python
  class MyClass:
  
      @classmethod
      def class_method(cls, arg1, ...):
  
  MyClass.class_method(...)
  ```
- ```python
  class Person:
      count = 0
      # 인스턴스 변수 설정
      def __init__(self, name):
          self.name = name
          Person.count += 1  # 클래스 변수는 앞에 클래스 명 붙여줌

      @classmethod
      def number_of_population(cls):
          print(f'인구수는 {cls.count}입니다.')

  person1 = Person('아이유')
  person2 = Person('이찬혁')
  
  print(Person.count) #2
  Person.number_of_population() #인구수는 2입니다.
  ```

> 데코레이터
- 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- @데코레이터(함수명) 형태로 함수위에 작성
- 순서대로 적용되기 때문에 작성 순서가 중요
- ```python
  # 데코레이터 없이 함수 꾸미기

  def hello():
    print('hello')

  def add_print(original):  # 파라미터로 함수를 받음
    def wrapper():          # 함수내에서 새로운 함수 선언
      print('함수시작')     # 부가기능 -> original함수를 꾸밈
      original()
      print('함수끝')       # 부가기능 -> original함수를 꾸밈
    return wrapper          # 함수를 return함


  print_hello = add_print(hello)
  print_hello()
  # 함수시작
  # hello
  # 함수끝

  ---------------------------------
  
  @add_print         # add_print를 사용해 print_hello() 함수를 꾸밈
  def print_hello():
    print('hello')
  
  print_hello()
  
  # 함수시작
  # hello
  # 함수끝
  ```

> 클래스 메서드와 인스턴스 메서드
- 클래스 메서드 -> 클래스 변수 사용
- 인스턴스 메서드 -> 인스턴스 변수 사용
- 인스턴스변수, 클래스변수 모두 사용하고싶다면?
  - **클래스는 인스턴스 변수 사용이 불가능!**
  - **인스턴스 메서드는 클래스변수, 인스턴스변수 둘다 사용가능!**

> 스태틱 메서드
- 인스턴스변수, 클래스변수를 전혀 다루지 않는 메서드
- 속성을 다루지않고 단지 기능(행동)만을 하는 메서드를 정의할때
- 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우
- **객체 상태나 클래스 상태를 수정 불가**
- @staticmethod 데코레이터를 사용하여 정의
- 일반함수처럼 동작하지만, **클래스의 이름공간에 귀속**됨
- **주로 해당 클래스로 한정하는 용도**로 사용
- ```python
  class Person:
      count = 0
      # 인스턴스 변수 설정
      def __init__(self, name):
          self.name = name
          Person.count += 1  # 클래스 변수는 앞에 클래스 명 붙여줌

      @staticmethod
      def check_rich(money): # 스태틱은 cls, self 사용 x
          return money > 10000

  person1 = Person('아이유')
  person2 = Person('이찬혁')
  
  print(Person.check_rich(100000)) # True 스태틱은 클래스로 접근 가능
  print(person1.check_rich(100000)) # True 스태틱은 인스턴스로 접근 가능
  ```

> 인스턴스와 클래스 간의 이름 공간 (namespace)
- 클래스를 정의하면, 클래스와 해당하는 이름공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색
- ```python
  class Person:
    name = 'unknown'

    def talk(self):
      print(self.name)
  
  p1 = Person()
  p1.talk()   # unknown

  p2 = Person()
  p2.talk() # unknown
  p2.name = 'Kim'
  p2.talk() # Kim

  print(Person.name)  # unknown
  print(p1.name)  # unknown
  print(p2.name)  # Kim
  
  # Person 클래스 값이 Kim으로 변경된것이아닌, 
  # p2 인스턴스 이름공간의 name이 Kim으로 저장됨 
  ```


> 메서드 정리

- 인스턴스 메서드

- 호출한 인스턴스를 의미하는 self 매개변수를 통해 인스턴스 조작

- 클래스 메서드

- 클래스를 의미하는 cls 매개변수를 통해 클래스 조작

- 스태틱 메서드

- 클래스 변수나 인스턴스 변수를 사용하지 않는 경우에 사용

- 객체 상태나 클래스 상태를 수정할 수 없음

- 
  ```python
  class MyClass:

    def method(self):
        return 'instance method', self

    @classmethod  # 개발자가 만들어놓은 함수
    def classmethod(cls):
        return 'class method', cls

    @staticmethod
    def staticmethod():
        return 'static method'
  ```

- 인스턴스 메서드 호출 결과

- ```python
  obj = MyClass() # 인스턴스 만들기
  
  print(obj.method()) # ('instance method', <__main__self>)
  
  print(MyClass.method(obj)) # 이렇게도 쓸수있음
  ```

- 클래스 자체에서 각 메서드를 호출하는 경우
  
  - 인스턴스 메서드는 호출할 수 없음
  
  - ```python
    print(MyClass.classmethod()) # ('class method', <class '__main__.MyClass;>)
    
    print(MyClass.staticmethod())
    
    MyClass.method() # 앞에가 인스턴스면 자동 self 할당이지만 class라서 안됨
    ```
  - **인스턴스는 클래스 메서드와 스태틱 메서드 모두 접근 가능**
  - ```python
    print(obj.classmethod())  
    print(MyClass.classmethod())
    print(obj.staticmethod())
    ```

> 객체 지향의 핵심개념

- 추상화

- 상속

- 다형성

- 캡슐화

- 객체지향프로그래밍 : 객체 <-> 객체 방법론, 패러다임

- 정보 - 변수 /  행동 - 메서드

> 추상화 (변수, 함수, 클래스)

- 복잡한 것을 숨기고, 필요한 것만 들어내기

- ex) user.login() <- django에서 활용도 높음

> 상속

- 두 클래스 사이 부모 - 자식 관계를 정립

- 클래스는 상속 가능

- 모든 파이썬 클래스는 object를 상속 받음

- ```python
  class ChildClass(ParentClass): # 받고싶은 parentclass 적으면됨
  ```

- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음

- 부모클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐

- ```python
  class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def talk(self):     # 중복 파트 !! (메서드 재사용)
      print(f'반갑습니다. {self.name}입니다.')

  class Professor(Person):
    def __init__(self, name, age, department):
      self.name = name
      self.age = age
      self.department = department

  class Student(Person):
    def __init__(self, name, age, gpa):
      self.name = name
      self.age = age
      self.gpa = gpa

  p1 = Professor('박교수', 49, '컴공')
  s1 = Student('김학생', 20, 3.5)

  p1.talk()   # 중복 파트!! 
              # 부모 클래스의 메서드 활용
  s1.talk()
  ```

- 상속 없이 구현하면 메서드 중복 정의하게 됨

- 상속을 통해 메서드 재사용 

- 자기 클래스에 없으면 parentclass에서 찾음

- 상속 관련 함수와 메서드
  
  - isinstance(object, classinfo) : 
    - classinfo의 instance거나 subclass*인 경우 True
  
    - 
      ```python
      class Person:
      
      #1)
      class Professor:
      
      p1 = Professor()
      
      print(isinstance(p1, Person) #False
      
      #2)
      class Professor(Person):
      
      p1 = Professor()
      
      print(isinstance(p1, Person) #True
      ```
    
   

  - issubclass(class, classinfo)

    - : class가 classinfo의 subclass면 True

    - classinfo는 클래스 객체의 *튜플일 수 있으며, classinfo의 모든 항목 검사*

    - ```python
      print(issubclass(bool, int)) # True
      print(issubclass(float, int)) #False
      print(issubclass(Professor, Person)) # True
      print(issubclass(Professor, (Person,Student)) # True 
      ```

    - super() : 자식클래스에서 부모클래스를 사용하고 싶은 경우

    - ```python
      class Student(Person):
          def __init__(self,name,age,number,email,student_id):
              #Person 클래스        
              super().__init__(name, age, number, email)
              self.student_id = student_id
      ```

> 상속 정리

- 파이썬의 모든 클래스는 object로부터 상속됨

- 부모클래스의 모든요소가 상속됨

- **super()** 통해 부모클래스 요소를 호출 가능 (그대로 가져오고, 한줄 더 자기꺼 추가하고싶을때)

- 매서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함

- 상속관계에서의 이름 공간은 인스턴스, 자식클래스, 부모클래스 순 탐색

> 다중 상속

- 두개 이상의 클래스를 상속 받는 경우

- 상속받은 모든 클래스의 요소를 활용 가능

- 중복된 속성, 메서드가 있으면 상속 순서에 의해 결정됨

- ```python
  class Person:
  
  class Mom(Person):
      gene = 'XX'
  
  class Dad(Person):
      gene = 'XY'
  
  class SecondChild(Mom, Dad):
  
  baby2 = SecondChile('아가')
  print(baby2.gene) # XX  (상속순서!)
  ```
  
 
- mro 메서드 (Method Resolution Order)

- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드

- 기존의 인스턴스 -> 클래스 순으로 이름공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식클래스 -> 부모클래스로 확장

- ```python
  print(SecondChild.mro())
  # [<class '__main__.SecondChild'>, <class '__main__.Mom'>, <class '__main__.Dad'>, <class '__main__.Person'>, <class 'object'>]
  ```
> 다형성

- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미

- 즉, 서로 다른 클래스에 속해있는 객체들이 **동일한 메시지에 대해 다른 방식으로 응답**할 수 있음

- **메서드 오버라이딩** (vs. 오버로딩)

- 상속받은 메서드를 재정의
  - 클래스 상속시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
  - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정기능을 바꾸고싶을때 사용
  
  - 상속받은 클래스에서 같은 이름의 매서드로 덮어씀
  
  - 부모 클래스의 메서드를 실행시키고 싶은 경우 super 활용
  
  - ```python
    class Person():
        def __init__(self, name):        
            self.name = name
        def talk(self):
            print(f'반갑습니다. {self.name}입니다.')
    
    class Professor(Person):
        def talk(self):
            print(f'{self.name}일세.')
    
    class Student(Person):
        def talk(self):    
            super().talk()
            print(f'저는 학생입니다.')
    
    p1 = Professor('김교수')
    p1.talk() # 김교수일세
    
    s1 = Student('이학생')
    s1.talk()
    # 반갑습니다. 이학생입니다.
    # 저는 학생입니다.
    ```
    



> 오버로딩

- print(a), print(a,b), print(a,b,c) 매개변수 개수 다양 (여러개 정의해서 상황에 맞게 사용)

- 오버로딩은 개념적으로만 존재 in python

> 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
  
  - 예시 : 주민등록번호

- 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음

> 접근제어자 종류

- Public Access Modifier

- Protected Access Modifier

- Private Access Modifier

> Public Member

- 언더바 없이 시작하는 메서드나 속성

- 어디서나 호출이 가능, 하위 클래스 override 허용

- 일반적으로 작성되는 메서드와 속성의 대다수를 차지

> Protected Member

- 언더바 1개로 시작하는 메서드나 속성

- 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능

- 하위 클래스 override 허용

- ```python
  class Person:
      def __init__(self,name,age):    
          self.name = name
          self._age = age 

      def get_age(self):
        return self._age

  
  p1 = Person('김싸피',30)
  print(p1.get_age()) 
  #인스턴스 만들고, get_age 메서드 활용하여 호출 가능
  
  
  print(p1._age) # 직접 접근해도 확인 가능하긴함
  ```

> Private Member

- 언더바 2개로 시작하는 메서드나 속성

- 본 클래스 내부에서만 사용가능

- 하위 클래스 상속 및 호출 불가능 (오류)

- 외부 호출 불가능 (오류)
- ```python
  class Person:
      def __init__(self,name,age):    
          self.name = name
          self.__age = age 

      def get_age(self):
        return self.__age

  
  p1 = Person('김싸피',30)
  print(p1.get_age()) 
  #인스턴스 만들고, get_age 메서드 활용하여 호출 가능
  
  
  print(p1.__age) # 직접 접근 불가
  # AttributeError: 'Person' object has no attribute '__age'
  ```  



> getter 메서드 / setter 메서드

- 변수에 접근 할 수 있는 메서드를 별도로 생성

- getter : 변수의 값을 읽는 메서드

- @property 데코레이터 사용

- setter : 변수 값을 설정

- @변수.setter 사용

- 
  ```python
  class Person():

      def __init__(self,age):
          self._age = age

      @property
      def age(self):
          return self._age

      @age.setter
      def age(self, new_age):
          if new_age <= 19:
              raise ValueError('Too Young For SSAFY')
              return
          self._age = new_age
    

  p1 = Person(20)
  print(p1.age) # 20 (getter setter 메서를 이용하므로 언더바안써도됨)

  p1.age = 33
  print(p1.age) # 30

  p1.age = 19
  print(p1.age) # ValueError 
  # 잘못된 정보를 막기위해
  ```



> 에러/예외 처리 (Error/ Exception Handling)

- 디버깅
  
  - 잘못된 프로그램을 수정하는 것
  
  - 에러 메시지가 발생하는경우
    
    - 해당 위치를 찾아 해결
  
  - 로직 에러가 발생하는 경우
    
    - 명시적인 에러 메시지 없이 예상과 다른 결과
    
    - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
    
    - 전체 코드 살펴봄
    
    - 휴식
    
    - 누군가에게 설명
  
  - 제어가 되는 시점
  
  - 조건/반복, 함수
  
  - print함수 활용
  
  - 개발환경에서 제공하는 기능 활용
  
  - Python tutor 활용

> 에러와 예외

- 문법 에러 (Syntax Error)

- SyntaxError 가 발생하면, 파이썬 프로그램은 실행되지않음

- 파일이름, 줄번호, ^ 문자를 통해 파이썬이 코드를 읽어 나갈때 (parser) 문제가 발생한 위치를 표현

- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿 (caret) 기호 (^)를 표시

- Invalid syntax : 문법오류
  
  - ```python
    while
    ```

- assign to literal : 잘못된 할당 
  
  - ```python
    5=3
    ```

- EOL (End of Line)
  
  - ```python
    print('hello)
    ```

- EOF (End of File)
  
  - ```python
    print(
    ```

- 예외 (Exception)
  
  - 실행도중 예상치 못한 상황을 맞이하면, 프로그램 실행 멈춤
    
    - 문장이나 표현식이 올바르더라도 발생하는 에러
  
  - 실행중에 감지되는 에러들을 예외 라고 부름
  
  - 예외는 여러타입으로 나타나고 타입이 메시지 일부로 출력
    
    - NameError, TypeError
  
  - 모든 내장 예외는 Exception Class 상속 받아 이뤄짐
  
  - 사용자 정의 예외를 만들어 관리 가능
  
  - ZeroDivisionError : 0으로 나누고자 할때
    
    - ```python
      10/0
      ```
  
  - NameError : namespace상에 이름이 없을때
    
    - ```python
      print(name_error)
      ```
  
  - TypeError : 타입 불일치
    
    - ```python
      1 + '1'
      round('3.5')
      divmod()
      ```
      
      import random
      random.sample()
      
      ```
      
      ```

- ValueError : 타입은 올바르나 값이 적절하지 않거나 없는 경우
  
  - ```python
    int('3.5')
    range(3).index(6)
    ```

- IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우
  
  - ```python
    empty_list = []
    
    empty_list[2]
    ```

- KeyError : 해당 키가 존재하지 않는 경우
  
  - ```python
    song = {'IU' : '좋은날'}
    song['BTS']
    ```

- ModuleNotFoundError
  
  - ```python
    import ssafy
    ```

- ImportError : Module은 있으나 존재하지않는 클래스/함수를 가져오는 경우
  
  - ```python
    from random import samp
    print(sample(range(3),1)
    ```

- KeyboardInterrupt : 임의로 프로그램을 종료하였을뗴
  
  - ```python
    while True:
        continuw
    ```

- IndentationError : Indentation이 적절하지않은 경우
  
  - ```python
    for i in range(3):
        print(i)
            print(i)
    ```

> 예외 처리

- try 문 (statement) / except 절 (clause)

- try문
  
  - 오류 발생 가능성 있는 코드 실행
  
  - 예외 발생 안하면 except없이 실행 종료
  - 반드시 한개 이상의 except문이 필요!

- except문
  
  - 예외 발생하면 except절이 실행
  
  - 예외 상황을 처리하는 코드를 받아서 적절 조치

- ```python
  try:
      num = input(숫자입력 : ')
  except ValueError: # int로 못바꿔서 에러가 발생하면
      print('숫자가 입력되지 않았습니다.')
  ```

- 에러메시지 처리 (as)
  
  - as 키워드 활용해 원본 에러 메시지 사용
  
  - 예외를 다른 이름에 대입
  
  - ```python
    try:
    
    except IndexError as err:
        print(f'{err})
    ```

- 복수 예외처리 : 발생가능한 에러를 모두 명시
  
  - 순차적으로 수행되므로, 가장 작은 범주부터 예외처리
  
  - ```python
    try:
        num = input('100으로 나눌 값을 입력 : ')
        100/int(num)
    except (ValueError, ZeroDivisionError):
        print('제대로 입력해')
    ```

    

- 예외 처리 종합
  
  - try : 코드 실행
  
  - except : try문에서 예외 발생시 실행
  
  - else : try문에서 예외 발생안하면 실행
  
  - finally : 예외 발생 여부와 관계없이 항상 실행
  
  - ```python
    # 파일이 없는 경우
    try:
        f = open('.txt')
    except FileNotFoundError:
        print()
    else:
        print()
    finally:
        print()
    ```
