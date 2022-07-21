# 조건문_반복문_함수_모듈

> ### 제어문 (순서도)

- 조건문 : 참/거짓 판단가능한 조건식과 함께 사용
  
  - ```python
    # 조건문
    num = int(input())
    if num % 2 == 0:
        print('짝수')
    
    elif num % 2 == 1:
        print('홀수')  
    ```

```python
# 복수 조건문

dust = int(input())
if dust > 150:

    print('매우나쁨')

elif dust > 80:

    print('나쁨')

elif dust > 30:

    print('보통')

else:

    print('좋음')

print('미세먼지 확인 완료')

#조건식을 동시에 검사하는 것이 아니라 순차적으로 비교!
```

```python
# 중첩 조건문
dust = int(input())
if dust > 150:
    print('매우나쁨')
    if dust > 300:
        print('실외 활동을 자제하세요')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
elif dust >=0:
    print('좋음')
else:
    print('값이 잘못되었습니다')
```

- 조건 표현식 (삼항연산자):

```
true인 경우 값 if 조건 else false인 경우 값
```

```python
# 절댓값을 저장하기위한 코드
value = num if num >= 0 else -num

# 홀수 짝수 구분
num = 2

result = '홀수' if num % 2 else '짝수'
print(result)
```

- 반복문 : 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
  
  - while문 : 종료 조건에 해당하는 코드를 통해 반복문 종료
    
    - 조건식이 참인 경우 코드 블록 실행
    
    - 코드블록 실행 후, 다시 조건식 검사하며 반복 실행
    
    - 무한 루프를 막기위해 종료 조건이 반드시 필요
    
    - ```python
      a = 0
      while a < 5:  # 종료조건
          print(a)
          a += 1    # 반복시 a가 계속 증가 (복합 연산자)
      print('끝')
      ```
  
  - for문 : 반복가능한 객체를 모두 순회하면 종료
    
    - 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체(iterable)의 요소를 모두 순회
    
    - 처음부터 끝까지 모두 순회, 별도 종료 조건 필요없음
    
    - Iterable
      
      - 순회 가능 자료형 (string, list, dict, tuple, range, set)
      
      - 순회형 함수 (range, enumerate)
    
    - ```python
      for fruit in ['apple','mango','banana']
          print(fruit)
      print('끝')
      ```
    
    - ```python
      # String 순회
      chars = input()
      for char in chars:
          print(char)
      
      for i in range(len(chars):
          print(chars[i])
      ```
    
    - ```python
      # Dictionary 순회 (key를 순회)
      grades = {'john':80, 'eric':90}
      
      for student in grades:
          print(student, grades[student])
      ```
    
    - ```python
      for student, grade in grades.items():
            print(student,grade)
      ```
    
    - ```python
      # enumerate 순회 (indes, value)
        members = ['민수','영희','철수']
      
        for idx, member in enumerate(members):
            print(idx, member)
      
        print(list(enumerate(members)) #[(0,'민수'),(1,'영희'),(2,'철수')]
        print(list(enumerate(members, start=1))
        ##[(1,'민수'),(2,'영희'),(3,'철수')]
      ```
  
  - List Comprehension
    
    - ```python
      cubic_list = [number**3 for number in range(1,4)]
          print(cubic_list)
      
          #[1,8,27]
      ```
  
  - Dictionary Comprehension
    
    - ```python
      cubic_dict = {number: number**3 for number in range(1,4)}
          print(cubic_dict)
      
          #{1:1,2:8,3:27}
      ```

- 반복문 제어
  
  - break : 반복문을 종료
    
    - ```python
      n = 0
      while True:
          if n == 3:
              break
          print(n)
          n += 1
      # 0,1,2
      
      for i in range(10):
          if i > 1:
              print('0과 1만 필요해!')
              break
          print(i)
      # 0,1,'0과 1만 필요해!'
      ```
  
  - continue : continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
    
    - ```python
      for i in range(6):
              if i % 2 == 0:
                  continue
              print(i)
          # 1, 3, 5
      ```
  
  - for-else : 끝까지 반복문 실행한 후, else문 실행
    
    - ```python
      for char in 'apple':
          if char == 'b':
              print('b!')
              break
      else:
          print('b가 없습니다.')
      
          # b가 없습니다.
      
          for char in 'banana':
              if char == 'b':
                  print('b!')
                  break           # break로 중단됨 / else 구문 실행 x
          else:
              print('b가 없습니다.')
      
          # b!
      ```
  
  - pass : 아무것도 하지 않음 (문법적으로 필요하나, 할 일이 없을 때)
    
    - ```python
       for i in range(4):
              if i == 2:
                  pass
              print(i)
          # 0,1,2,3
      ```

> ### 함수

- Decomposition (분해) :  기능을 분해하고, 재사용 가능하게 만들고
  
  - ```python
    numbers = [1,2,3]
    
    def average(numbers):
        return sum(numbers) / len(numbers)
    
    print(average(numbers)  #2.0
    ```

- Abstraction (추상화) : 복잡한 내용을 몰라도 사용할 수 있도록, 재사용성과 가독성,생산성

- 함수의 종류
  
  - 함수란? 
    
    :특정한 기능을 하는 코드의 조각
    
     특정 코드를 매번 다시 작성하지않고, 필요시에만 호출
  
  - 내장 함수 : 파이썬에 기본적으로 포함
  
  - 외장 함수 : import문 사용, 외부 라이브러리에서 제공
  
  - 사용자 정의 함수 : 직접 사용자가 만드는 함수

- 함수 기본 구조 <재료(파라미터) - 레시피 - 결과>
  
  - 선언과 호출 (define & call)
  
  - 입력 (input)
  
  - 문서화 (Docstring)
  
  - 범위 (Scope)
  
  - 결과값 (output)
  
  - ```python
    num1 = 0  #재료
    num2 = 1
    
    def func1(a,b):  #선언    
        return a+b   
    def func2(a,b):  #선언
        return a-b
    def func3(a,b):  #선언
        return func1(a,5) + func2(5,b)
    
    result = func3(num1,num2)  #호출
    print(result) # 9
    ```

> 함수의 Output

- 값에 따른 함수의 종류
  
  - Void function 
    
    : 명시적인 return값이 없는 경우, None 반환하고 종료
  
  - Value returning function 
    
    : 함수 실행 후, return문을 통해 값 반환
    
      return을 하게 되면, 값 반환 후 함수가 바로 종료
  
  - print vs. return
    
    - print를 사용하면 호출될 때마다 값이 출력
    
    - 데이터 처리를 위해서는 return 사용
    
    - ```python
      # Void function
      def void(x,y):
          print(f'{x}x{y}={x*y}')
      void(4,5)
      ans = void(4,5)
      print(ans) #None
      
      # Value returning function
      def value(x,y):
          return x*y
      value(4,5)
      ans = value(4,5)
      print(ans) #20
      ```

- 두 개 이상의 값 반환
  
  - ```python
    #튜플
    def minus_and_product(x,y):
        return x-y , x*y
    y = minus_and_product(4,5)
    print(y) # (-1,20)
    print(type(y)) # <class 'tuple'>
    ```
  
  - ```python
    #리스트
    words = ['우영우','기러기','파이썬']
    def palindrome(words):
        palindrome_list = []
        for word in words:
            if word == word[::-1]:
                palindrome_list.append(word)
        return palindrome_list
    
    print(palindrome(words) # ['우영우','기러기']
    ```

> 함수의 Input

- Parameter : 함수를 정의할 때, 함수 내부에서 사용되는 변수

- Argument : 함수를 호출할 때, 넣어주는 값

- ```python
  def func(ham):  #parameter : ham
      return ham
  func('spam')   #argument : 'spam'
  ```
  
  - Positional Arguments 
    
    : 기본적으로 함수 호출 시 argument는 위치에 따라 함수 내에 전달됨
  
  - Keyword Arguments
    
    : 직접 변수의 이름으로 특정 argument 전달 가능
    
      keyword argument 다음에 positional argument를 활용 불가
    
    ```python
    def add(x,y):
        return x+y
    add(x=2,y=5)
    add(2,y=5)
    add(x=2,5) #error발생!
    ```
  
  - Default Arguments Values
    
    : 기본값을 지정, 함수 호출 시 argument 값을 설정하지 않도록 함
    
    ```python
    def add(x, y=0):
        return x+y
    add(2)
    ```
  
  - 가변 인자 (*args):
    
    : 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
    
      몇 개의 positional argument를 받을지 모르는 함수를 정의할 때
    
    ```python
    def add(*args):
        for arg in args:
            print(arg)
    add(2,3,4,5)
    
    ------------------------
    
    def func(*args):
        print(args)
        print(type(args))
    func(1,2,3,'a','b')
    # (1,2,3,'a','b')
    
    #<class 'tuple'>
    ```
    
    - 패킹 : 여러 개의 데이터를 묶어서 변수에 할당
      
      ```python
      nums = (1,2,3,4)
      
      print(numbers) #(1,2,3,4)
      ```
    
    - 언패킹 : 시퀀스 속 요소들을 여러 변수에 나누어 할당
      
      ```python
      nums = (1,2,3,4)
      a,b,c,d = nums
      
      print(a,b,c,d) #1 2 3 4
      
      ------------------------ # asterisk(*)활용
      nums = (1,2,3,4,5)
      a,b, *rest = nums
      print(a,b,rest) # 1 2 [3,4,5]
      
      a,*rest,e = nums
      print(rest) #[2,3,4]
      ```
    
    - 가변인자 예시
      
      ```python
      def sum_all(*nums):  # (1,2,3)
          result = 0
          for num in nums:
              result += num
          return result
      
      print(sum_all(1,2,3)) # 6
      --------------------------------
      def fam_name(fat,mot,*pets):
          print(f'아버지:{fat}')
          print(f'어머니:{mot}')
          print(f'반려동물들..')
          for name in pets:
              print(f'반려동물:{name})
      fam_name('아부지','어무니','멍멍이','냥냥이')
      ```
  
  - 가변 키워드 인자 (**kwargs)
    
    : 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때
    
      **kwargs는 딕셔너리로 묶여 처리
    
      *args와 동시 사용 가능!
    
    ```python
    def fam(**kwargs):
        for key, value in kwargs.items():
            print(key, ":", value)
    
    fam(father='아부지',mother='어무니',baby='아기')
    '''
    father : 아부지
    mother : 어무니
    baby : 아기
    '''
    -------------------------------
    def fam_name(fat,mot,**pets):
        print('아버지:',fat)
        print('어머니:',mot)
        if pets:  # pets안에 내용이 있으면
            print('반려동물들..')
            for species, name in pets.items():
                print(f'{species}:{name}')
    fam_name('아부지','어무니',dog = '멍멍이',cat ='냥냥이')
    ```

> Python의 Scope

- Scope
  
  - global scope : 코드 어디에서든 참조할 수 있는 공간
  
  - local scope : 함수가 만든 scope, 함수 내부에서만 참조 가능

- Variable
  
  - global variable : global scope에 정의된 변수
  
  - local variable : local scope에 정의된 변수

- 변수 수명주기 (lifecycle)
  
  - built-in scope : 파이썬이 실행된 이후부터 영원히 유지
  
  - global scope : 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
  
  - local scope : 함수가 호출될 때 생성, 함수가 종료될 때까지 유지

- ```python
  def func():
      a = 20
      print('local',a)
  
  func()  #local 20
  print('global',a) #NameError: 'a' is not defined
  
  #a는 함수 종료(return)후 수명주기 종료!
  ```

- 이름 검색 규칙 (Name Resolution) -> LEGB Rule
  
  - Local scope : 지역범위
  
  - Enclosed : 지역 범위 한단계 위
  
  - Global : 최상단
  
  - Built-in : 모든 것을 담고 있는 범위  (ex. print())
  
  - 함수 내에서는 바깥 scope의 변수에 접근 가능하나 수정은 불가
  
  - ```python
    print(sum) <built-in function sum>
    print(sum(range(2))) #1
    sum = 5
    print(sum) #5
    print(sum(range(2))) #TypeError: 'int' object is not callable
    
    # Global scope 이름공간의 sum변수에 값 5가 할당, 
    # 이후 global scope에서 sum은 LEGB에 의해 Built-in scope의 내장함수보다 5가 먼저 탐색
    ```

- ```python
  a = 0
  b = 1
  def enclosed():
      a = 10
      c = 3
      def local(c):
          print(a,b,c) # 10 1 300
      local(300)
      print(a,b,c) # 10 1 3
  enclosed()
  print(a,b) # 0 1
  
  # 내방부터 찾기
  ```

- global 문
  
  : 현재 코드 블록 전체에 적용, 나열된 식별자가 global variable임을 나타냄
  
    global에 나열된 이름은 같은 코드 블록에서 global앞에 등장 불가
  
    global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지       않아야함
  
  - ```python
    a = 10
    def func():
        global a
        a = 3
    print(a) # 10
    func()
    print(a) # 3    -> Local scope에서 global 변수 값의 변경,
             #         global키워드를 사용하지 않으면, 
             #         Local scope에 a변수가  생성됨  
    
    #parameter에 global 사용 불가
    #global a 선언 전에는 a변수 사용 불가 (ex. global a 선언전, print(a))
    ```

- nonlocal
  
  : global 제외하고 가장 가까운 (둘러싸고 있는) scope의 변수를 연결하도록 함
  
    nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal 앞에 등장 불가
  
    nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야함
  
    global과는 달리 이미 존재하는 이름과의 연결만 가능함
  
  - ```python
    x = 0 
    def func():
        x = 1
        def func2():
            nonlocal x
            x = 2
        func2()
        print(x) # 2
    
    func()
    print(x) #0
    
     # nonlocal은 이름공간상에 존재하는 변수만 가능!
    ```

> 함수 응용

- 내장 함수
  
  - map(function, iterable)
  
  - filter(function, iterable)
    
    - ```python
      def odd(n):
          return n%2
      nums = [1,2,3]
      result = filter(odd,nums)
      print(list(result)) # [1,3]
      
      # 결과가 True (= 1)인 것들만 반환
      ```
  
  - zip(*iterables)
    
    - ```python
      girs = ['jane','ashley']
      boys = ['justin','eric']
      pair = zip(girls,boys)
      print(list(pair)) # [('jane','justin'),('ashley','eric')]
      
      #복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
      ```

- lambda
  
  - ```python
    def triangle(b,h):
        return 0.5*b*h
    print(triangle(5,6)
    -------------------------------------
    triangle = lambda b, h : 0.5 * b  *h
    print(triangle(5,6)
    ```

- 재귀함수 (Recursive function)
  
  - 1개 이상의 base case (종료되는 상황)가 존재하고, 수렴하도록 작성
  
  - ```python
    def factorial(n):
        if n==0 or n==1:
            return 1
        else:
            return n * factorial(n-1)
    print(factorial(4)) # 24
    -------------------------------------
    #반복문으로 작성
    def fact(n):
        result = 1
        while n>1:
            result *= n
            n -= 1
        return result
    print(fact(4)) #24
    ```

- base case에 도달할 때까지 함수 호출

- 메모리 스택이 넘치게 되면 (stack overflow) 프로그램 동작 불가

- 파이썬 maximum recursion depth가 1000번, 호출 횟수가 이를 초과하면 Recursion Error

- 반복문과 재귀함수 비교:
  
  - 알고리즘 자체가 재귀적 표현이 자연스러우면 재귀함수 사용
  - 재귀 호출은 변수 사용을 줄여줌
  - 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림   

> 모듈

- 모듈 : 다양한 기능을 하나의 파일로 묶은 것
- 패키지 : 다양한 파일을 하나의 폴더로 묶은 것 
- 라이브러리 : 다양한 패키지를 하나의 묶음으로
- pip : 관리하는 관리자
  - $ pip install SomePackage
  - $ pip list
  - $ pip show SomePackage
  - $ pip freeze > requirements.txt
  - $ pip install -r requirements.txt

> 모듈과 패키지

- 모듈 : 특정 기능을 하는 코드를 .py 단위로 작성한 것

- 패키지 : 특정 기능 관련 모듈의 집합, 서브 패키지 포함
  
  ```python
  import module 
  from module import var,fuction,Class
  from module import *
  from package import module
  from package.module import var,function,Class
  ```
  
  > 사용자 모듈과 패키지

```
 - my_package
   - calculator
     - __init__.py
     - tools.py
   - __init__.py
   - check.py
```

```python
# tools.py
def add(num1,num2):
  return num1 + num2
def minus(num1,num2):
  return num1 - num2
# check.py
from calculator import tools
print(dir(tools))
print(tools.add(1,2))
```

> 가상환경

```python
$ python -m venv venv
$ source venv/Scripts/activate #나만의 가상환경
```
