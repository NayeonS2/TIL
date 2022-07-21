# Python 기초

> 프로그래밍이란?

- 프로그램을 만드는 행위

- 컴퓨터에게 일을 시키기 위해서 프로그램을 만드는 행위

- 코딩과 유사한 의미

> 프로그램이란?

- 특정 작업을 수행하는 일련의 명령어들의 모음

- 컴퓨터가 해야 할 일들의 모음

- 소프트웨어와 유사한 의미

> 프로그래밍 언어란?

- 컴퓨터는 기계어로 소통함 (0과 1로 모든 것을 표현)

- 기계어의 대안으로 사람이 이해할 수 있는 새로운 언어를 개발 -> 프로그래밍 언어

- 사람이 이해할 수 있는 문자로 구성

- 기본적인 규칙, 문법 존재

- 소스 코드 : 프로그래밍 언어로 작성된 프로그램

- 번역기 (*interpreter / compiler) : 소스 코드를 컴퓨터가 이해할 수 있는 기계어로 번역

> 파이썬의 특징

- 인터프리터 언어 (Interpreter) : 소스 코드를 기계어로 변환할 때 통역하듯이 1줄씩 변환

- 객체 지향 프로그래밍 : 모든 것이 객체로 구현

> 파이썬 개발 환경

- IDE (Integrated development environment)
  
  - 통합 개발 환경의 약자, 개발에 필요한 다양하고 강력한 기능들을 모아둔 프로그램 보통 개발은 IDE로 진행함 (ex. vs code, Pycharm)
  
  - IDE 기능
    
    - 세로 커서 (Alt + Ctrl + 화살표)
    
    - 특정 단어 replace (Ctrl + D)
    
    - 줄 바꿈 (Alt + 화살표)
    
    - 줄 복사 (Alt + Shift + 화살표)
    
    - 화면 Split

- Jupyter Notebook
  
  - 문법 학습을 위한 최적의 도구, 소스코드와 함께 실행 결과와 마크다운 저장 가능
  
  - Open Source 기반의 웹 플랫폼 및 어플리케이션, 파이썬을 비롯한 다양한 프로그래밍 언어를 지원하며 셀 단위의 실행이 가능

> 코드 작성법

- 파이썬에서 제안하는 스타일 가이드 - PEP8

- 들여쓰기 (Indentation)
  
  - Space sensitive
  
  - 4칸 or 1탭
  
  - 한 코드 안에서는 반드시 한 종류의 들여쓰기만 사용!
  
  - 원칙적으로는 공백(빈칸, space) 사용을 권장

- 주석 (Comment)
  
  - 코드에 대한 설명
  
  - 코드 이해 쉬워지고, 분석 및 수정 용이
  
  - 실행에 영향을 미치지 않고, 프로그램 속도를 느리게 하지않으며, 용량을 늘리지 않음
  
  - 한 줄 주석 ('#')
  
  - 여러 줄 주석 (한 줄씩 '#' or ''', """ 묶어서)
  
  - 가독성 저해할 정도로 무분별 사용 자제

> 변수 (Variable)

- 데이터를 저장하기 위해서 사용

- 변수를 사용하면 복잡한 값들을 쉽게 사용할 수 있음 (추상화)

- 동일 변수에 다른 데이터를 언제든 할당(저장)할 수 있기 때문에, '변수'라고 함

- 추상화 (변수를 사용해야 하는 이유)
  
  - 코드 가독성 증가
  
  - 숫자를 직접 적지 않고, 의미 단위로 작성 가능
  
  - 코드 수정이 용이해짐

> 변수의 할당

- 변수는 할당 연산자 (=)를 통해 값을 할당 (assignment)

- 같은 값을 동시에 할당할 수 있음
  
  ```python
  a = b = 2000
  ```

- 다른 값을 동시에 할당할 수 있음
  
  ```python
  a, b = 2000, 3000
  ```

- 각 변수의 값을 바꿔서 저장하기
  
  - 방법 1) 임시 변수 활용
    
    ```python
    x, y = 10, 20
    temp = x
    x = y
    y = temp
    ```
  
  - 방법 2) Pythonic!
    
    ```python
    x, y = 10, 20
    
    x, y = y, x
    ```

> 식별자

- 식별자의 이름은 영문 알파벳, 언더스코어(_), 숫자로 구성

- 첫 글자에 숫자 불가

- 길이 제한 x, 대소문자 구별 o

- 다음의 키워드(keywords)는 예약어(reserved words)이며 사용할 수 없음
  
  ```python
  import keyword
  print(keyword.kwlist)
  
  # 출력 결과
  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
   'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 
  'while', 'with', 'yield']
  ```

- 내장 함수나 모듈 등의 이름도 사용 x
  
  ```python
  print(5)
  print = 'hi'
  print(5) # TypeError: 'str' object is not callable
  # 내장 함수 print가 아닌, 문자열 hi가 할당된 변수 print로 사용됨
  ```

> 연산자

- 산술 연산자 (Arithmetic Operator)

```python
i = 5
j = 3

print(i+j) # 5 + 3 = 8
print(i-j) # 5 - 3 = 2
print(i*j) # 5 * 3 = 15
print(i//j) # 5 // 3 = 1 몫
print(i/j) # 5 / 3 = 1.6666666666666667 
print(i**j) # 5의 3제곱 = 125
```

- 연산자 우선순위

| 우선순위 | 연산자                                             | 설명                                 |
| ---- | ----------------------------------------------- | ---------------------------------- |
| 1    | (값...), [값...],<br>{키: 값...}, {값...}            | 튜플, 리스트, 딕셔너리, 세트 생성               |
| 2    | x[인덱스],<br>x[인덱스:인덱스],<br>x(인수...), x.속성        | 리스트(튜플) 첨자, 슬라이싱, 함수 호출, 속성 참조     |
| 3    | await x                                         | await 표현식                          |
| 4    | **                                              | 거듭제곱                               |
| 5    | +x, -x, ~x                                      | 단항 덧셈(양의 부호), 단항 뺄셈(음의 부호), 비트 NOT |
| 6    | *, @, /, //, %                                  | 곱셈, 행렬 곱셈, 나눗셈, 버림 나눗셈, 나머지        |
| 7    | +, -                                            | 덧셈, 뺄셈                             |
| 8    | <<, >>                                          | 비트 시프트                             |
| 9    | &                                               | 비트 AND                             |
| 10   | ^                                               | 비트 XOR                             |
| 11   | \|                                              | 비트 OR                              |
| 12   | in, not in, is, is not,<br><, <=, >, >=, !=, == | 포함 연산자, 객체 비교 연산자, 비교 연산자          |
| 13   | not x                                           | 논리 NOT                             |
| 14   | and                                             | 논리 AND                             |
| 15   | or                                              | 논리 OR                              |
| 16   | if else                                         | 조건부 표현식                            |
| 17   | lambda                                          | 람다 표현식                             |

> 자료형 (Datatype) 분류

- 자료형 : 사용할 수 있는 데이터의 종류들
  
  - Boolean (불린형)
  
  - Numeric (수치형)
    
    - Int (정수)
    
    - Float (실수)
    
    - Complex (복소수)
  
  - String (문자열)

> 수치형 (Numeric Type)

- 정수 (Int)
  
  - 일반적인 수학 연산 가능

- 진수 표현
  
  - 2진수 (binary) : 0b
  
  - 8진수 (octal) : 0o
  
  - 16진수 (hexadecimal) : 0x
  
  - ```python
    print(0b10) # 2
    print(0o30) # 24
    print(0x10) # 16
    ```

- 실수 (float)
  
  - 유리수, 무리수를 포함 (ex. 0.1, 100.0, -0.001 등)
  
  - 부동 소수점 주의 (Floating point rounding error)
    
    - 컴퓨터는 2진수, 사람은 10진법 사용
    
    - 10진수 0.1은 2진수로 표현하면 0.0001100110011001100110... 무한 반복
    
    - 사람이 사용하는 10진법의 근사값만 표시, but 동일하진 않음
    
    - ```python
      print(3.2 - 3.1) # 0.10000000000000009
      print(1.2 - 1.1) # 0.09999999999999987
      ```
    
    - 값 비교 과정에서는 해결책이 필요!
    
    - ```python
      a = 3.2 - 3.1
      b = 1.2 - 1.1
      
      # 1. 임의의 작은 수 활용
      print(abs(a-b) <= 1e-10) #True
      
      # 2. math 모듈 활용
      import math
      
      print(math.isclose(a,b)) #True
      ```

> 문자열 (String)

- 모든 문자는 str 타입

- '' 나 ""를 활용해 표기
  
  - 문자열 묶을 때 동일한 문장부호 활용
  
  - PEP8에서는 소스코드 내에서 하나의 문장부호를 선택하여 유지

- 중첩 따옴표
  
  ```python
  print("문자열 안에 '작은따옴표'를 사용하려면 큰따옴표로 묶는다.")
  
  print('문자열 안에 "큰따옴표"를 사용하려면 작은 따옴표로 묶는다.')
  ```

- 삼중 따옴표
  
  ```python
  print('''문자열 안에 '작은따옴표'나 
  "큰따옴표"를 사용할 수 있고 
  여러 줄을 사용할 때도 편리하다.''')
  ```

- Escape Sequence
  
  | 예약문자 | 내용(의미)    |
  |:----:|:---------:|
  | \\n  | 줄 바꿈      |
  | \t   | 탭         |
  | \r   | 캐리지 리턴    |
  | \0   | 널(Null)   |
  | \\\  | \         |
  | \'   | 단일인용부호(') |
  | \"   | 이중인용부호(") |

- 문자열 연산
  
  - 덧셈 (문자열 연결- String Concatenation)
    
    ```python
    print("hello"+"world") #helloworld
    ```
  
  - 곱셈
    
    ```python
    print("python"*3) #pythonpythonpython
    ```

- String Interpolation
  
  - %-formatting
    
    ```python
    name = 'Kim'
    score = 4.5
    
    print('내 이름은 %s' % name)
    print('성적은 %d' % score) # 4
    print('성적은 %f' % score) # 4.5
    ```
  
  - str.format()
    
    ```python
    print('내 이름은 {}! 성적은 {}!'.format(name,score))
    ```
  
  - f-strings
    
    ```python
    print(f'내 이름은 {name}! 성적은 {score}')
    
    import datetime
    today = datetime.datetime.now()
    
    print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d})
    
    pi = 3.141592
    print(f'원주율은 {pi:.2f}. 반지름이 2일 때 원의 넓이는 {pi*2*2}')
    
    #원주율은 3.14. 반지름이 2일때 원의 넓이는 12.566368
    ```

> None

- 파이썬 자료형 중 하나

- 값이 없음을 표현하기 위해 None 타입이 존재

- 일반적으로 반환 값이 없는 함수에서 사용하기도 함

> 불린형 (Boolean)

- 논리 자료형, 참과 거짓을 표현

- True / False

- 비교 / 논리 연산에서 활용

- **비교 연산자** : True/ False 값 리턴

| 비교 연산자 | 내용(의미)          |
|:------:|:---------------:|
| \<     | 미만              |
| <=     | 이하              |
| >      | 초과              |
| >=     | 이상              |
| ==     | 같음              |
| !=     | 같지않음            |
| is     | 객체 아이덴티티(OOP)   |
| is not | 객체 아이덴티티가 아닌 경우 |

```python
print(3.0 == 3) #True
```

- 논리 연산자
  
  - 여러 가지 조건이 있을 때
  
  - 모든 조건 만족(and), 여러 조건 중 하나만 만족(or) 할때 특정 코드 실행
  
  - | 연산자     | 내용(의미)                   |
    |:-------:|:------------------------:|
    | A and B | A와 B 모두 True이면, True     |
    | A or B  | A와 B 모두False이면, False    |
    | Not     | True->False, False->True |
  
  - ```python
    #22가 지나고 졸리면 True, 졸리지 않다면 False
    hour = 23
    status = 'sleepy'
    print(hour >= 22 and status == 'sleepy') #True
    
    hour = 23
    status = 'nice'
    print(hour >= 22 and status = 'sleepy') # False
    ```
  
  - Falsy : False는 아니지만 False로 취급
    
    -> 0, 0.0, (), [], {}, None, ""(빈 문자열)
  
  - 논리 연산자도 우선 순위 존재
    
    -> not, and, or 순으로 높음
    
    ```python
    print(not True) # False
    print(not 0) # True
    print(not 'hi') # False
    print(not True and False or not False)
    print(((not True)and False)or (not False)) # True
    ```
  
  - 논리 연산자의 단축 평가
    
    - 결과가 확실한 경우 두번째 값은 확인하지 않고 첫번째 값 반환
    
    - and 연산에서 첫번째 값이 False인 경우 무조건 False -> 첫번째 값 반환
    
    - or 연산에서 첫번째 값이 True인 경우 무조건 True -> 첫번째 값 반환
    
    - ```python
      print(3 and 5) # 5
      print(3 and 0) # 0
      print(0 and 3) # 0
      print(0 and 0) # 0
      
      print(5 or 3) # 5
      print(3 or 0) # 3
      print(0 or 3) # 3
      print(0 or 0) # 0
      ```

> 컨테이너

- 여러 개의 값을 담을 수 있는 객체, 서로 다른 자료형을 저장 가능 (ex. List)

- Ordered  vs.  Unordered

- But, 순서가 있다 != 정렬되어 있다.

- 컨테이너
  
  - 시퀀스형
    
    - 리스트 (가변형 mutable)
    
    - 튜플 (불변형 immutable)
    
    - 레인지 (불변형 immutable)
  
  - 비시퀀스형
    
    - 세트 (가변형 mutable)
    
    - 딕셔너리 (가변형 mutable)

> 리스트 (시퀀스형)

- 여러 개의 값을 순서가 있는 구조로 저장

- [] or list() 통해 생성

- 어떠한 자료형도 저장 가능, 리스트 안 리스트 저장 가능

- 가변 자료형(mutable)

- 순서가 있는 시퀀스, 인덱스 통해 접근 가능

> 튜플 (시퀀스형)

- 여러 개의 값을 순서가 있는 구조로 저장

- But, 담고 있는 값 변경 불가 (불변 자료형 immutable)

- () or tuple() 통해 생성

- 시퀀스이기에 인덱스로 접근 가능

- 단일 항목 튜플의 경우 값 뒤에 쉼표 필수 (ex. (1, ))

- 복수 항목의 경우에는 필수는 아니나, 권장 (ex. (1, 2, 3,))

- 튜플 대입 (Tuple assignment)
  
  - 우변의 값을 좌변의 변수에 한 번에 할당
  
  - 일반적으로 파이썬 내부에서 활용
  
  - 함수에서 복수의 값을 반환 시 활용
  
  - ```python
    x, y = 1, 2   # (1, 2) 실제 튜플로 처리
    print(x, y)  
    ```

> Range (시퀀스형)

- 숫자의 시퀀스를 나타냄

- 주로 반복문과 함께 사용
  
  - 기본형 range(n)
  
  - 범위 지정 range(n, m)
  
  - 범위 및 스텝 지정 range(n, m, s)
    
    ```python
    print(list(range(1, 5, 2))) # [1, 3]
    
    # 역순
    print(list(range(6, 1, -1))) # [6, 5, 4, 3, 2]
    print(list(range(6, 1, -2))) # [6, 4, 2]
    print(list(range(6, 1, 1))) # []
    ```

> 슬라이싱 연산자

- 시퀀스를 특정 단위로 슬라이싱

- 콜론 기준, 앞 인덱스 해당 문자는 포함 but 뒤 인덱스 해당 문자는 미포함

- ```python
  # 리스트 (k 간격으로)
  print([1, 2, 3, 5][0:4:2]) # [1, 3]
  #튜플
  print((1, 2, 3, 5)[0:4:2]) # (1, 3)
  #range
  print(range(10)[1:5:3]) # range(1,5,3)
  #문자열
  print('abcdefg'[1:3:2]) # b
  print('abcdefghi'[5:2:-1]) # 'fed' 
  ```

- ```python
  s = 'abcdefghi'
  s[::] = 'abcdefghi' = s[0:len(s):1]
  s[::-1] = 'ihgfedcba' = s[-1:-(len(s)+1):-1]
  ```

> 셋 (비시퀀스형)

- Set은 중복되는 요소 없이, 순서에 상관없는 데이터들의 묶음

- 데이터 중복을 허용하지 않아, 중복 원소는 하나만 저장
  
  ```python
  print({1, 2, 3, 1, 2}) # {1, 2, 3} 중복 제거
  ```

- 순서가 없기에 인덱스 통한 접근 불가

- 집합 연산이 가능

- 가변 자료형 (mutable) -> 담고 있는 요소 삽입 변경 삭제 가능

- {} or set() 을 통해 생성 -> 빈 set 생성을 위해선 반드시 set()  

- Set을 활용하면 중복 값 제거 가능, But 이 후 순서가 무시됨 !

- 셋 (Set) 연산자
  
  ```python
  A = {1, 2, 3, 4}
  B = {1, 2, 3, "Hello", (1, 2, 3)}
  #합집합
  print(A | B) # {1, 2, 3, 4, (1, 2, 3), "Hello"}
  #교집합
  print(A & B) # {1, 2, 3}
  #차집합
  print(B - A) # {(1, 2, 3), "Hello"}
  #대칭차집합
  print(A ^ B) # {"Hello", 4, (1, 2, 3)} 둘이 안 겹치는거
  #여집합은 없음
  ```

> 딕셔너리 (비시퀀스형) - 3.7부터는 ordered/ 이하 버전은 unordered

- key-value 쌍으로 이뤄진 자료형

- key는 변경 불가능한 데이터(immutable)만 활용 가능
  
  - string, integer, float, boolean, tuple, range

- values 는 어떤 형태든 관계 x

- {} or dict() 통해 생성

> 형 변환 (Typecasting)

- 파이썬에서 데이터 형태는 서로 변환 가능
  
  - 암시적 형 변환 (implicit)
    
    : 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환
    
    - bool
    
    - Numeric type (int, float)
      
      ```python
      print(True + 3) # 4 (bool)
      
      print(3 + 5.0) # 8.0 (Numeric type - int, float)
      ```
  
  - 명시적 형 변환 (explicit)
    
    : 사용자가 특정 함수를 활용해 의도적으로 자료형 변환
    
    - int
      
      - str (형식에 맞는 문자열만 가능) , float -> int
      
      ```python
      print(int('3') + 4) # 7
      
      print(int('3.5') + 5) # ValueError 
      # -> 정수 형식이 아닌 경우 타입 변환 불가
      ```
    
    - float
      
      - str (형식에 맞는 문자열만), int -> float
      
      ```python
      print(float('3')) # 3.0
      
      print(float('3/4') + 5.3) # ValueError
      # -> float 형식이 아닌 경우 타입 변환 불가
      ```
    
    - str
      
      - int, float, list, tuple, dict -> str
      
      ```python
      print(str(1)) # 1
      print(str(1.0)) # 1.0
      print(str([1, 2, 3]) # [1, 2, 3]
      print(str((1, 2, 3))) # (1, 2, 3)
      print(str({1, 2, 3})) # {1, 2, 3}
      ```

> 컨테이너 형 변환

![https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png](https://user-images.githubusercontent.com/18046097/61180466-a6a67780-a651-11e9-8c0a-adb9e1ee04de.png)
