# 데이터 구조 및 활용

- **데이터 구조.메서드()** => 주어.동사()

- 메서드 ex) List.append(10), String.split()

- 파이썬 공식 문서 표기법
  
  - 문법 표현하기 위한 것 
  
  - ex) str.replace(old, new[, count])
  
  - old, new 는 필수 / [,count]는 선택적 인자

---

## 순서가 있는 데이터 구조

> 문자열

- 모든 문자는 str (=> immutable)

- 하나의 문장부호로 통일 '' / ""

- ```python
  word = 'ssafy'
  print(word)  # ssafy
  print(id(word))  # 메모리 주소 확인 2503713912048
  word = 'test'
  print(word)  # test -> str이 변경x (immutable) / 갈아끼운 것
  print(id(word))  # 메모리 주소 확인 2503713942768
  ```

- 문자열 조회/탐색
  
  ```
  s.find(x) -> x의 첫번째 위치 반환. 없으면 -1 반환 (프로그램 계속 진행)
  s.index(x) -> x의 첫번째 위치 반환. 없으면 오류 발생 (프로그램 중
  s.isalpha() -> 알파벳 문자 여부 (숫자가 아님)
  s.isupper() -> 대문자 여부
  s.islower() -> 소문자 여부
  s.istitle() -> 타이틀 형식 여부 (첫번째가 대문자, 나머지 소문)
  ```
  
  - s.find(x)
    
    - ```python
      print('apple'.find('p')) #1
      print('apple'.find('k')) #-1
      ```
  
  - s.index(x)
    
    - ```python
      print('apple'.index('k')) # Error
      ```

- 문자열 검증
  
  - ```python
    print('abc'.isalpha()) # True
    print('ㄱㄴㄷ'.isalpha()) # True
    print('Ab'.isupper()) # False
    print('Title Title!'.istitle()) # True
    ```
  
  - isdecimal() : 숫자
  
  - isdigit() : 수
  
  - isnumeric() : 수로 볼 수도 있는 것
  
  - isdecimal() < isdigit() < isnumeric

- 문자열 변경 메서드
  
  - s.replace(old, new[,count])
    
    - ```python
      print('woooowoo'.replace('o','!',2)) # w!!oowoo
      ```
  
  - s.strip([chars]) : 공백이나 특정 문자 제거
    
    - ```python
      print('    와우!\n'.strip())  # 와우!
      print('    와우!\n'.lstrip())  # 와우!
      print('    와우!\n'.rstrip())  #     와우!
      ```
  
  - s.split(sep=None, maxsplit=-1)
  
  - 'separator'.join([iterable])
  
  - s.capitalize() : 가장 첫 글자를 대문자로 (원본유지)
  
  - s.title() : 띄어쓰기 기준, 각 단어 첫글자는 대문자로 나머지는 소문자로, 어포스트로피(')나 공백 이후를 대문자로 만들어 반환 (원본유지)
  
  - s.upper() : (원본유지)
  
  - s.lower()
  
  - s.swapcase() : 대소문자 서로 변경
    
    - ```python
      msg = 'hI! Everyone, I\'m ssafy'    
      
      print(msg)  # hI! Everyone, I'm ssafy
      print(msg.capitalize()) # Hi! everyone, i'm ssafy
      print(msg.title())  # Hi! Everyone, I'M Ssafy
      print(msg.upper())  # HI! EVERYONE, I'M SSAFY
      print(msg.lower())  # hi! everyone, i'm ssafy
      print(msg.swapcase())   # Hi! eVERYONE, i'M 
      
      print('*'.join('ssafy'))    # s*s*a*f*y
      print(' '.join(['3', '5'])) # 3 5
      print(' '.join(['3', '5', '8']))  # 3 5 8SAFY
      ```

> 리스트

- 리스트 메서드
  
  - ```
    L.append(x)
    L.insert(i,x) -> 인덱스 i에 항목 x 삽입
    L.remove(x) -> 가장 먼저 찾은 x를 제거/ 항목 없을 경우 ValueError
    L.pop() -> 가장 마지막을 반환 후 제거
    L.extend(iterable) -> 리스트 합치기
    L.index(x, start, end) -> 리스트 항목 중 가장 왼쪽에 있는 항목 x의 인덱스 반환
    L.reverse() -> 리스트를 거꾸로 정렬
    L.sort() -> 리스트 정렬
    L.count(x) -> 항목 x가 몇개 존재하는지
    ```
  
  - L.append(x) : 리스트에 값 추가 (마지막에)
  
  - L.insert(i, x) : 정해진 i위치에 x값을 추가
    
    - ```python
      cafe = ['starbucks','tomntoms','hollys']
      cafe.insert(0, 'start')
      cafe.insert(2, 'start')
      cafe.insert(100, 'end')
      print(cafe) 
      # ['start', 'starbucks', 'start', 'tomntoms', 'hollys', 'end']
      ```
  
  - L.extend(iterable)
    
    - ```python
      cafe = ['starbucks','tomntoms','hollys']
      cafe.extend(['coffee'])
      print(cafe)  # ['starbucks', 'tomntoms', 'hollys', 'coffee']
      cafe.extend('cup')
      print(cafe)  
      # ['starbucks', 'tomntoms', 'hollys', 'coffee', 'c', 'u', 'p']
      ```
  
  - L.remove(x) : 리스트에서 값이 x인 첫번째 항목을 삭제, 항목이 없으면 ValueError가 발생
    
    - ```python
      nums = [1, 2, 3, 'hi']
      print(nums)  # [1, 2, 3, 'hi']
      nums.remove('hi')
      print(nums)  # 1, 2, 3]
      nums.remove('hii')  # value error
      ```
  
  - L.pop(i)
    
    - ```python
      nums = [1, 2, 3, 'hi']
      word = nums.pop()
      print(word) # hi
      print(nums) # [1, 2, 3]
      ```
  
  - L.clear() : 모든 항목 삭제
  
  - L.index(x) : x 값을 찾아 index 반환 / 없으면 Value Error
  
  - L.count(x)
    - ```python
      # 원하는 값을 모두 삭제하려면 다음과 같이 할 수 있습니다.
      a = [1, 2, 1, 3, 4]
      target_value = 1
      for i in range(a.count(target_value)):
          a.remove(target_value)
      print(a)
      ```
  
  - L.sort() : 원본 리스트를 정렬함 (원본 바꿈) . None 반환
    
    - sorted와 비교
    
    - ```python
      nums = [3, 2, 5, 7]
      result = nums.sort()
      print(nums, result) 
      # [2, 3, 5, 7] None
      
      nums = [3, 2, 6, 8]
      # result = nums.sorted() 틀린것
      result = sorted(nums)
      print(nums, result)
      # [3, 2, 6, 8] [2, 3, 6, 8]
      ```
  
  - L.reverse() : 원본을 뒤집음, 내장함수 reversed() 와는 다르게 원본 list를 변형시키고, None을 리턴
    
    - ```python
      nums = [3, 2, 5, 1]
      result = nums.reverse()
      print(nums, result)  # [1, 5, 2, 3] None
      ```

> 튜플

- 여러개의 값을 순서가 있는 구조로 저장

- immutable -> 값에 영향을 미치지 않는 메서드만 지원

- ```python
  day_name = ('월', '화', '수', '목', '금')
  print(type(day_name))
  print(id(day_name)) # 2694461611440
  
  print(day_name[-3]) # 수
  print(day_name * 2) # ('월', '화', '수', '목', '금', '월', '화', '수', '목', '금')
  day_name += False, True
  print(day_name) # ('월', '화', '수', '목', '금', False, True)
  print(id(day_name)) # 2694462990272 (새로만든것)
  ```

- 멤버십 연산자
  
  - 포함 여부 확인 (in / not in)

- 시퀀스형 연산자
  
  - 산술연산자(+) : 시퀀스 간 concatenation
  
  - 반복연산자(*) : 시퀀스 반복

---

## 비시퀀스형 데이터 구조

> 셋

- 중복 요소 없음 

- 순서 없음 (unordered)

- 집합 연산 가능
- 순회가능 (iterable)

- 변경가능 (mutable)

- 셋 메서드
  
  - ```
    s.copy() : 셋의 얕은 복사본 반환
    s.add(x) : 항목 x가 셋에 없다면 추가
    s.pop() : 셋에서 랜덤하게 항목 반환, 제거/ set 빈경우 keyerror 
    s.remove(x) : x 삭제/ 항목 없는 경우 keyerror
    s.discard(x) : x 삭제/ 에러 안남
    s.update(t) : 셋 t에 있는 항목 중 셋 s에 없는 항목을 추가
    s.clear() : 모든 항목 제거
    s.isdisjoint(t) : 
    셋s가 셋t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True
    s.issubset(t) : 셋s가 셋t의 하위 셋인 경우, True
    s.issuperset(t) : 셋s가 셋t의 상위 셋인 경우, True
    ```
  
  - s.update(*others) : 여러 값을 추가, 반드시 iterable 데이터 구조를 전달
    
    - ```python
      a = {'사과', '바나나'}
      a.update({'딸기', '바나나', '참외'})
      
      print(a)    # {'참외', '딸기', '바나나', '사과'}

      a = {'사과', '바나나', '수박'}
      a.update({'토마토', '토마토', '딸기'}, {'포도', '레몬'})
      print(a) 
      # {'토마토', '바나나', '수박', '사과', '레몬', '포도', '딸기'}
      ```
  
  - s.remove(x) : 삭제할 항목 없으면 keyerror
  
  - s.discard(x) : 삭제할 항목 없어도 에러 안남
    
    - ```python
      a = {'사과', '바나나'}
      a.update({'딸기', '바나나', '참외'})
      
      print(a)    # {'참외', '바나나', '딸기', '사과'}
      a.remove('딸기')    
      print(a)    # {'참외', '바나나', '사과'}
      a.remove('딸기')
      print(a)    # KeyError: '딸기'
      
      
      a.discard('바나나')
      print(a)    # {'딸기', '사과', '참외'}
      a.discard('바나나')
      print(a)    # {'딸기', '사과', '참외'} -> 에러 발생 x
      
      ```
      
      

- s.pop() : 셋은 순서가 없기때문에 임의의 원소 제거, 반환

- s.clear() : 원소 모두 제거 -> set() 출력

- 집합 관련 함수
  
  - s.isdisjoint(t)
  
  - s.issubset(t)
  
  - s.issuperset(t)
  
  - ```python
    a = {'사과','바나나','수박'}
    b = {'포도','망고'}
    c = {'사과','포도','망고','수박','바나나'}
    
    print(a.isdisjoint(b))  # True (a와 b가 서로소인가?)
    print(a.isdisjoint(c))  # False (a와 c가 서로소인가?)
    print(a.issubset(c))    # True (a는 c의 하위 셋인가?)
    print(b.issubset(c))    # True (b는 c의 하위 셋인가?)
    print(b.issubset(a))    # False (b는 a의 하위 셋인가?)
    print(c.issuperset(a))  # True (c는 a의 상위 셋인가?)
    print(c.issuperset(b))  # True (c는 b의 상위 셋인가?)
    print(a.issuperset(c))  # False (a는 c의 상위 셋인가?)
    ```

> 딕셔너리
- 변경 가능하고(mutable)
- 순서가 없고(unordered),
- 순회 가능한(iterable)

- 딕셔너리 메서드
  
  - ```
    d.clear()
    d.copy()
    d.keys()
    d.values()
    d.items()
    d.get(k) : 키 k의 값 반환, k가 딕셔너리에 없을 경우 None 반환(error X)
    d.get(k, v) : 키 k의 값 반환, k가 딕셔너리에 없을 경우 V 반환
    d.pop(k)
    d.pop(k, v)
    d.update([other])
    ```
    
    
    
    

- d.get(key[,default])
  
  - key를 통해 value 가져옴
  
  - KeyError 발생 x
  
  - default값 설정 가능 (기본 : None) <- key가 존재하지 않을 경우 None을 반환
  
  - d[key] 는 key가 없을때 KeyError

- d.pop(key[,default])
  
  - key가 딕셔너리에 있으면 제거하고 해당 값 반환
  
  - 그렇지 않으면 default 반환
  
  - default 값이 없으면 KeyError
  
  - ```python
    my_dict = {'apple':'사과', 'banana':'바나나'}
    data = my_dict.pop('apple') # key값
    print(data, my_dict)    # 사과 {'banana': '바나나'}
    
    data = my_dict.pop('apple')
    print(data) # KeyError: 'apple'
    
    data = my_dict.pop('apple',0)
    print(data) # 0
    ```

- d.update()
  
  - ```python
    my_dict = {'apple':'사', 'banana':'바나나'}
    my_dict.update(apple='사과') # key = value
    print(my_dict)  # {'apple': '사과', 'banana': '바나나'}
    ```

---

## 얕은 복사와 깊은 복사

> 할당 (assignment)

- 대입 연산자 (=)  ->  '사물함을 같이 쓰는 느낌!' (주소를 공유)

- 대입연산자 통한 복사는 해당 객체에 대한 객체 참조를 복사!

- ```python
  original_list = [1,2,3]
  copy_list = original_list # 주소 공유
  print(original_list,copy_list)  # [1, 2, 3] [1, 2, 3]
  
  copy_list[0] = 'hello'
  print(original_list,copy_list)  # ['hello', 2, 3] ['hello', 2, 3]
  ```

> 얕은 복사 (shallow copy)

- Slice 연산자 활용, 같은 원소의 리스트지만 연산된 결과를 복사 (다른 주소!)

- ```python
  a = [1,2,3]
  b = a[:]    # But, 1차원에서만 가능!!!
  print(a,b)  # [1, 2, 3] [1, 2, 3]
  b[0] = 5
  print(a,b)  # [1, 2, 3] [5, 2, 3]
  ```

- 주의사항 : 복사하는 리스트의 원소가 주소를 참조하는 경우
  
  - ```python
    a = [1,2,['a','b']]
    b = a[:]
    print(a,b)  # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
    b[2][0] = 0  # 2차원에서는
    print(a,b)  # [1, 2, [0, 'b']] [1, 2, [0, 'b']] # 둘다바뀜
    ```

> 깊은 복사 (deep copy)

- ```python
  import copy
  a = [1,2,['a','b']]
  b = copy.deepcopy(a)
  print(a,b)  # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
  b[2][0] = 0
  print(a,b)  # [1, 2, ['a', 'b']] [1, 2, [0, 'b']] # b만 바뀜
  ```

## Python 03 포인트!!!

> Dictionary

- D.update([other])
  
  - ```python
    my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
    my_dict.update(apple = '사과아',coconut = '코코넛') # 키값은 따옴표 제외
    print(my_dict)
    #{'apple': '사과아', 'banana': '바나나', 'melon': '멜론', 'coconut': '코코넛'}
    
    d = {'mango':'망고','watermelon':'수박'}
    my_dict.update(d) 
    print(my_dict)
    '''
    {'apple': '사과아',
     'banana': '바나나',
     'melon': '멜론',
     'coconut': '코코넛',
     'mango': '망고',
     'watermelon': '수박'}
    '''
    ```
- .setdefault(key[, default]) : 
  - dict.get() 메서드와 비슷한 동작을 하는 메서드로, key가 딕셔너리에 있으면 value를 돌려줌
  - key가 딕셔너리에 없을 경우, default 값을 갖는 key 를 삽입한 후 default 를 반환한다는 점입니다. 만일 default가 주어지지 않을 경우, None 
  - ```python
    my_dict = {'apple': '사과', 'banana': '바나나', 'melon': '멜론'}
    my_dict.setdefault('pineapple', '파인애플') # '파인애플'
    print(my_dict) # {'apple': '사과', 'banana': '바나나', 'melon': '멜론', 'pineapple': '파인애플'}
    ```



> String

- S.strip() : 특정한 문자들을 지정하면 **문자열의 모든 조합을 제거**합니다. 인자가 없을 경우 공백을 제거
  
  - ```python
    a = '   hello!  \n'
    b = 'hihihihahahahihi'
    c = 'monty python'
    
    
    print(a.strip()) #'hello!'
    print(a.lstrip()) #'hello!  \n'
    print(b.rstrip('hi')) #'hihihihahaha'
    print(b.lstrip('hi')) #'ahahahihi'
    
    print(c.rstrip(' python')) #m
    
    # monty만 남을것같지만 '공백,p,y,t,h,o,n' 이 들어간 모든 문자를 제거해서
    
    #m만 남게됨!!!!!


    www = 'www.saffy.com'
    print(www.strip('.')) #www.saffy.com
    # 왼쪽과 오른쪽에서 부터 시작해서 다른 문자를 만나면 탐색 중지
    ```  
- S.split([chars]) : 문자열을 특정한 단위로 나누어 **리스트**로 반환
  - ```python
    'a_b_c'.split('_') #['a', 'b', 'c']       
    ```

- S.isspace()

  - ```python
    a = '    n'
    b = '\n \t '

    print(a.isspace()) # False
    print(b.isspace()) # True
    ```

-  'separator'.join(iterable)
   -  ```python
      words = ['안녕', 'hello']
      ''.join(words) #'안녕hello'
      ```
    
    

> List

- L.sort()

- ```
  .sort() : 원본 변경 (원본에서 진행해야되므로 .이 붙음), None 반환
  sorted() : 새롭게 정렬된 것을 반환
  ```
  
  - ```python
    # sort
    print(lotto.sort()) #None
    print(lotto) #[10, 11, 18, 21, 41, 43]
    print(lotto.sort(reverse=True) #None
    print(lotto) #[43, 41, 21, 18, 11, 10]
    
    #sorted
    import random
    lotto = random.sample(range(1, 46), 6)
    print(lotto, sorted(lotto))
    print(lotto)
    #[24, 27, 20, 45, 33, 2] 
    #[2, 20, 24, 27, 33, 45]
    #[24, 27, 20, 45, 33, 2]
    ```
- L.append(x) : 리스트에 값을 추가 (a[len(a):] = [x])
- L.extend(iterable) : 리스트에 iterable(list, range, tuple, string) 값을 붙일 수가 있음 (a[len(a):] = iterable)
  - ```python
    cafe.extend(['twosome_place']) 
    #['starbucks', 'tomntoms', 'hollys', 'banapresso', 'wcafe', '빽다방', 'twosome_place']
    cafe.extend('ediya') 
    #['starbucks', 'tomntoms', 'hollys', 'banapresso', 'wcafe', '빽다방', 'twosome_place', 'e', 'd', 'i', 'y', 'a']
    ```
- L.insert(i,x) : 정해진 i 위치에 값 추가
  - ```
    # a.insert(0, x)는 리스트의 처음에 x를 삽입하고,
    # a.insert(len(a), x) 는 a.append(x) 와 같습니다.
    # 리스트의 길이를 넘어서는 인덱스는 마지막에 아이템이 추가됩니다.
    ```






> 얕은복사와 깊은복사

- **변경 불가능한 (immutable) 데이터**
  
  - 리터럴
    
    - 숫자/ 글자/ 참거짓
  
  - range()
  
  - tuple()
  
  - frozenset()
  
  - ```python
    a = 20
    b = a
    b = 10
    
    print(a) #  b와함께 바뀌지않음
    print(b)
    ```

- 변경 가능한 (mutable) 데이터
  
  - 할당
    
    - ```python
      original_list = [1, 2, 3]
      
      copy_list = original_list
      print(copy_list) #[1, 2, 3]
      
      copy_list[0] = 5
      print(original_list) #[5, 2, 3]
      
      print(id(copy_list),id(original_list)) # 동일 주소 공유
      ```
  
  - 얕은복사
    
    - ```python
      # slice 연산자 사용 [:]
      a = [1, 2, 3]
      b = a[:]
      b[0] = 5
      print(a,b) #[1, 2, 3] [5, 2, 3]
      
      #list() 활용
      a = [1, 2, 3]
      b = list(a)
      b[0] = 5
      print(a,b) #[1, 2, 3] [5, 2, 3]
      
      #copy모듈 활용
      import copy
      a = [1,2,3]
      b = copy.copy(a)
      b[0] = 5
      print(a,b) #[1, 2, 3] [5, 2, 3]
      
      
        ```
      
    
    - ```python
      #하지만, 이렇게 하는 것도 일부 상황에만 
      #서로 다른 얕은 복사(shallow copy)입니다.
      #2차원 리스트와 같이 mutable 객체 안에 mutable 객체가 있는 경우 
      #문제가 됩니다. 아래 예시를 통해 확인해봅시다.
      
      a = [1, 2, [1, 2]]
      
      b = a[:]
      b[2][0] = 5
      print(a,id(a),b,id(b))  
      # 동일주소는 아님 but, 2차원이상부턴 다시 주소공유
      #a와 b의 id는 다르다는 것을 확인하였지만, 내부 값은 영향을 받게 되었습니다.
      
      print(id(a[2]),id(b[2])) 
      #내부의 객체 id(a[2])과 id(b[2])은 같은 주소를 바라보고 있기 때문입니다.
      ```

  - 깊은복사
    - 만일 중첩된 상황에서 복사를 하고 싶다면, 깊은 복사(deep copy)
    - 깊은 복사는 새로운 객체를 만들고 원본 객체 내에 있는 객체에 대한 복사를 재귀적으로 삽입
    - 즉, 내부에 있는 모든 객체까지 새롭게 값이 변경
    - ```python
      import copy

      a = [1, 2, [1, 2]]
      b = copy.deepcopy(a)

      b[2][0] = 3
      print(a,b) # [1, 2, [1, 2]] [1, 2, [3, 2]]
      ```


