# 01. 배열 1 (Array 1)
> 알고리즘
- 문제를 해결하기 위한 절차나 방법
- 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법
- 의사코드(슈도코드) vs. 순서도

> 무엇이 좋은 알고리즘인가?
- 정확성 : 얼마나 정확하게 동작
- 작업량 : 얼마나 적은 연산 
- 메모리 사용량 : 얼마나 적은 메모리
- 단순성 : 얼마나 단순
- 최적성 : 더이상 개선 여지없이 최적화 

> 알고리즘 성능 분석
- 알고리즘의 작업량 비교
- 작업량은 시간복잡도로 표현

> 시간 복잡도 (Time Complexity)
- 실제 걸리는 시간을 측정
- 실행되는 명령문의 개수를 계산
- 빅-오(O) 표기법
  - 시간복잡도 함수 중 가장 큰 영향력을 주는 n에 대한 항만을 표시
  - 계수는 생략
  - O(3n+2) = O(n)
  - O(2n^2+10n+100) = O(n^2)
  - O(4) = O(1)

> 배열
- 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
- 하나의 선언을 통해 둘 이상의 변수 선언 가능
- 단순히 다수의 변수 선언을 의미하는게 아니라 다수의 변수로는 하기힘든 작업을 배열을 통해 쉽게 가능

> 1차원 배열 선언
- 별도 선언 방법이 없으면 변수에 처음 값을 할당할 때 생성
- Arr = list()
- Arr = []
- Arr = [1,2,3]
- Arr = [0] * 10

> 1차원 배열 접근
- Arr[0] = 10
- Arr[idx] = 20


> 알고리즘 풀이 (낙차)
- ```python
    N = int(input())

    arr = list(map(int, input().split()))

    maxV = arr[0]   # 첫 원소를 최대값으로 가정

    for i in range(0, N):   # 나머지 모든 원소에 대해
        if arr[i] > maxV:
            maxV = arr[i]

    print(maxV)
    ```
- '절대값 10억이하인 n개의 정수 중 최대값 구해라' 일때는 maxV = 0으로 초기화하면 안됨!!!

---
> 정렬
- 2개이상의 자료를 특정 기준에의해 작은 값부터 큰값 (ascending 오름차순), 혹은 그 반대 순서로 (descending 내림차순) 재배열하는 것
- 키 : 자료를 정렬하는 기준이 되는 특정 값

> 버블 정렬 (Bubble Sort)
- 인접한 두개의 원소를 비교하며 자리를 계속 교환하는 방식
- 첫번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
- 한단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬
- 시간복잡도 : O(n^2)
- ```
  [55,7,78,12,42]

  <첫번째 패스>
  55 7 78 12 42
  7 55 78 12 42
  7 55 78 12 42
  7 55 12 78 42
  7 55 12 42 78
  
  <두번째 패스>
  7 55 12 42 |78
  7 55 12 42 |78
  7 12 55 42 |78
  7 12 42 55 |78

  <세번째 패스>
  7 12 42 55 78
  7 12 42 55 78
  7 12 42 55 78

  <네번째 패스>
  7 12 42 55 78
  7 12 42 55 78
  ```
- 시작 0 - 끝 N-1  ~  시작0 - 끝 1
- ```python
  <슈도코드>
  for i: N-1 -> 1   # 구간의 끝을 정하면
    for j: 0 -> i-1 # 인접 원소중 왼쪽 인덱스
        if arr[j] > arr[j+1]    # 왼쪽이 크면
           arr[j] <-> arr[j+1] # 자리바꿈
  
  <코드>
  def BubbleSort(a, N):
    for i in range(N-1, 0 , -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
  ```

> 카운팅 정렬 (Counting Sort)
- 항목들의 순서 결정을 위해 집합에 각 항목이 몇개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적 알고리즘
- 정수나 정수로 표현할 수 있는 자료에 대해서만 적용 가능
- 각 항목의 발생 회수를 기록하기 위해, 정수 항목으로 인덱스 되는 카운트들의 배열을 사용하기 때문
- 카운트들을 위한 충분한 공간을 할당하려면 집합 내의 가장 큰 정수를 알아야함
- 시간 복잡도 : O(n+k) -> n은 리스트 길이, k는 정수의 최대값
- 정렬된 집합에서 각 항목의 앞에 위치할 항목의 개수를 반영하기 위해 counts의 원소를 조정
- ```
  DATA 0 4 1 3 1 2 4 1
  COUNTS 1 3 1 1 2
  COUNTS 1 4 5 6 8 <누적합>
  
  for i: 1 -> N-1
    COUNTS[i] = COUNTS[i-1] + COUNTS[i]

    counts[1]을 감소시키고 Temp에 1을 삽입
    INDEX 0 1 2 3 4
    DATA 0 4 1 3 1 2 4 1(J=7)
    COUNTS 1 3 5 6 8
    TEMP [][][] 1 [][][][] (네번째 숫자)

    counts[4]를 감소시키고 Temp에 4를 삽입
    INDEX 0 1 2 3 4
    DATA 0 4 1 3 1 2 4 1(J=7)
    COUNTS 1 3 5 6 7
    TEMP [][][] 1 [][][] 4 (여덟번째 숫자)

    counts[2]를 감소시키고 Temp에 2를 삽입
    INDEX 0 1 2 3 4
    DATA 0 4 1 3 1 2 4 1(J=7)
    COUNTS 1 3 4 6 7
    TEMP [][] 2 1 [][][] 4 (세번째 숫자)

    정렬 완료
    DATA 0 4 1 3 1 2 4 1
    COUNTS 0 1 4 5 6
    TEMP 0 1 1 1 2 3 4 4
    ```

- ```python
  def Counting_Sort(A, B, k):
  # A [] : 입력 배열 (1 to k)
  # B [] : 정렬된 배열
  # C [] : 카운트 배열

    C = [0] * (k+1)
    
    for i in range(0, len(A)):
        c[A[i]] += 1

    for i in range((1, len(C))):
        C[i] += C[i-1]

    for i in range(len(B)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[[i]]]] = A[i]
  ```

> 정렬 알고리즘 비교
- 버블정렬 / 평균 O(n^2) / 최악 O(n^2) / 비교와 교환 / 코딩이 가장 손쉬움
- 카운팅 정렬 / 평균 O(n+k) / 최악 O(n+k) / 비교환 방식 / n이 비교적 작을 때만 가능


> 완전 검색 (Exaustive Search)
- 문제 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인
- Brute-force or generate-and-test
- 모든 경우의 수를 테스트 한 후 최종 해법 도출
- 일반적으로 경우의 수가 작을때 유용
- 수행속도는 느리지만 해답 발견 실패 확률이 작다
- Baby-gin 문제

> 순열 (Permutation)
- 서로 다른 것들 중 몇개를 뽑아서 한 줄로 나열
- 서로 다른 n개중 r개를 택하는 순열 (nPr)
- nPr = n * (n-1) * (n-2) * ... * (n-r+1) = n! / (n-r)!
- nPn = n! = n * (n-1) * (n-2) * ... * 2 * 1
- ```python
  # {1,2,3}을 포함하는 모든 순열을 생성하는 함수
  for i1 in range(1,4):
    for i2 in range(1,4):
        if i2 != i1:
            for i3 in range(1,4):
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
  ```
  ```python
  def recursive_permutation(arr, depth, n, r):
    if depth == r:
        print(arr[:depth])
        return
    
    for i in range(depth, n):
        swap(arr, depth, i)
        recursive_permutation(arr, depth + 1, n, r)
        swap(arr, depth, i)

  def swap(arr, depth, i):
      arr[i], arr[depth] = arr[depth], arr[i]

  arr = [1, 2, 3]
  recursive_permutation(arr, 0, 3, 2)
  ```
  ```python
  def dfs(arr, depth, n, r):
      if depth == r:
          print(result)
          return
      
      for i in range(n):
          if not visited[i]:
              visited[i] = True
              result[depth] = arr[i]
              dfs(arr, depth + 1, n, r)
              visited[i] = False

  arr = [1, 2, 3]
  n, r = len(arr), 2

  visited = [False for _ in range(n)]
  result = [0 for _ in range(r)]
  dfs(arr, 0, n, r)
  ```



> 탐욕 (Greedy) 알고리즘
- 최적해를 구하는 데 사용되는 근시안적 방법
- 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라 생각되는 것을 선택해 나가는 방식으로 진행하여 최종 해답에 도달
- 각 선택 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여 그것이 최적이란 보장은 없다
- 1) 해 선택 : 현재 상태에서 부분 문제의 최적해를 구한뒤 이를 부분해 집합(solution set)에 추가
- 2) 실행가능성 검사 : 새로운 부분해 집합이 실행 가능한지 확인, 문제의 제약 조건을 위반하지 않는지 검사
- 3) 해 검사 : 새로운 부분해 집합이 문제의 해가 되는지 확인, 아직 전체 문제의 해가 완성되지 않았다면 1) 해선택 부터 다시 시작


> Baby-gin 구현

- ```python
  num = 456789
  c = [0] * 12  # run구하기위해 12칸으로 설정
  #1
  for i in range(6):
    c[num%10] += 1
    num // = 10
  #2
  while num > 0:
    c[num % 10] +=1 
    num // = 10


  i = 0
  tri = run = 0
  while i < 10:
    if c[i] >= 3:
        c[i] -= 3
        tri += 1
        continue;
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >=1:
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

  if run + tri == 2 : print("Baby Gin")
  else : print("Lose")
  ```

  
