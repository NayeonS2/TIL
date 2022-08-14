# 02. 배열 2 (Array 2)
> 2차원 배열의 선언
- 1차원 list를 묶어놓은 list
- 2차원 이상의 다차원 list는 차원에 따라 index를 선언
- 2차원 list의 선언 : 세로길이(행의 개수), 가로길이(열의 개수)를 필요로 함
- python에서는 데이터 초기화를 통해 변수선언과 초기화 가능
- arr = [[0,1,2,3],[4,5,6,7]]
- ```python
  3
  1 2 3
  4 5 6
  7 8 9

  N, M = map(int,input().split())
  arr = [list(map(int,input().split()) for _ in range(N))]

  for i in range(N):        # N = len(arr)
    for j in range(M):      # M = len(arr[0])
        print(arr[i][j], end =' ')
        print()
  ```
> 배열 순회
- n x m 배열의 n*m개의 모든 원소를 빠짐없이 조사하는 방법
- ```python
  for i in range(n):    # 행우선 순회
    for j in range(m):
        Array[i][j]

  for j in range(m):    # 열우선 순회
    for i in range(n):
        Array[i][j]

  for i in range(n):
    for j in range(m):
        Array[i][j + (m-1 - 2*j) * (i % 2)] # 지그재그 순회

  # 원래 arr[i][m-1-j] 하면 j가 증가할때 index는 감소
  # 여기서는 i%2 넣어서 홀수 행일때만 진행 (앞에 j가 하나있어서 -2*j)
  ```

---
> 델타를 이용한 2차 배열 탐색 *****
- 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색
- 0 (우)부터 시계방향 0 - 1 - 2 - 3 
- 0  |  1  | 2 |  3
- i+0 | i+1 | i+0 | i-1     # di = [0, 1, 0, -1]
- j+1 | j+0 | j-1 | j+0     # dj = [1, 0, -1, 0]
- ```python
  for i in range(N):
    for j in range(N):
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N: #유효한 인덱스면 ***중요
                test(arr[ni][nj])

  for i in range(N):
    for j in range(M):
        for di, dj in [[0,1] , [1,0], [0,-1], [-1,0]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M :
                print(ni, nj)

  #상하좌우 두칸씩일때
  for i in range(N):
    for j in range(M):
        for k in range(4):
            for d in range(1,3):
                ni = i + di[k]*d
                nj = j + dj[k]*d
                if 0<=ni<N and 0<=nj<M :    
                    print(ni, nj)
  ```


> 전치행렬
- ```python
  # 3x3 행렬 
  for i in range(3):
    for j in range(3):
        if i<j:
            arr[i][j] , arr[j][i] = arr[j][i], arr[i][j]

  ---
  a = [[1,2,3],[4,5,6],[7,8,9]]
  b = list(zip(*a))
  # [[1,4,7],[2,5,8],[3,6,9]]
  ```

---

> 부분집합 합 문제
- 집합 원소 n개일때, 공집합 포합 부분집합 수 2^n
- 각 원소가 부분집합에 포함되었는지를 loop이용해 확인하고 부분집합 생성하는 방법
  - ```python
    bit = [0,0,0,0]
    for i in range(2):
        bit[0] = i  # 0번째 원소
        for j in range(2):
            bit[1] = j  # 1번째 원소
            for k in range(2):
                bit[2] = k  # 2번째 원소
                for l in range(2):
                    bit[3] = l  # 3번째 원소

                    print_subset(bit)   # 생성된 부분집합?
    ```

> 비트 연산자
- & : 비트 단위로 AND연산
- | : 비트 단위로 OR 연산
- << : 피연산자의 비트 열을 왼쪽으로 이동 (x2)
- '>> : 피연산자의 비트 열을 오른쪽으로 이동 (/2)

> << 연산자
- 1 << n : 2^n (즉 원소가 n개일경우 모든 부분집합의 수)

> & 연산자 (둘다 1일때 1 !!!)
- i & (1<<i) : i의 j번째 비트가 1인지 검사 (0이면 결과가 0)

> 보다 간결하게 부분집합을 생성하는 방법!! *****
- ```python
  arr = [3,6,7,1,5,4]
  n = len(arr)  # 원소의 개수 6
  for i in range(1<<n): # 부분 집합의 개수 (2^n = 64만큼!)
    for j in range(n):  # 원소의 개수만큼 비트 체크
        if i & (1<<j):  # i의 j번 비트가 1인 경우
            print(arr[j], end=", ")     # j번 원소 출력!
    print()
  print()
  ```

---

> 검색 (Search)
- 저장되어 있는 자료중에서 원하는 항목을 찾는 작업
- 목적하는 탐색 키를 가진 항목을 찾는 것
    - 탐색키

> 순차검색 (Sequential Search)
- 일렬로 되어있는 자료를 순서대로 검색
    - 가장 간단하고 직관적
    - 배열이나 연결리스트 등 순차구조로 구현된 자료구조에서 유용
    - 알고리즘이 단순하여 구현 쉬움, but 검색 대상 수가 많을 경우 수행시간 급격히 증가
- 정렬되어 있지 않은 경우 / 정렬되어 있는 경우
    - 정렬되어 있지 않는 경우
        - 첫번째 원소부터 순서대로 검색대상과 키 값이 같은 원소가 있는지 비교하며 찾는다
        - 키값이 동일한 원소를 찾으면 그 원소의 인덱스 반환
        - 자료구조의 마지막에 이를때까지 검색대상 찾지못하면 검색 실패
        - 찾고자 하는 원소의 순서에 따라 비교회수 결정 = (1/n) * (1+2+3+4..+n) = (n+1)/2
        - 시간복잡도 : O(n)
        - ```python
          def sequential(a,n,key):
            i=0
            while i<n and a[i] != key:
                i += 1
            if i<n:
                return i
            else:
                return -1
          ```
    - 정렬되어 있는 경우
        - 찾고자 하는 원소의 순서에 따라 비교회수 결정
        - 정렬이 되어있어 검색실패를 반환하는 경우 평균 비교횟수가 반으로 준다
        - 시간복잡도 : O(n)
        - ```python
          def sequential(a,n,key):
            i = 0
            while i<n and a[i]<key :
                i +=1
            if i<n and a[i] == key:
                return i
            else:
                return -1
          ```
---

> 이진검색 (Binary Search)
- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 목적 키를 찾을 때까지 이진검색을 순환적으로 반복 수행, 검색 범위를 반으로 줄여가면서 보다 빠르게 검색 수행
- 자료가 정렬된 상태여야함! **
- 검색과정
    - 자료 중앙 원소 고른다
    - 중앙 값과 목표값 비교
    - 목표값이 중앙 원소 값보다 작으면 왼쪽 반에 대해 새로 검색, 크면 자료 오른쪽반에 대해 새로 검색
    - 찾고자하는 값 찾을때까지 반복
- 구현
    - 검색 범위의 시작점과 종료점을 이용하여 검색 반복 수행
    - 자료 삽입 삭제 발생할때 배열 상태를 항상 정렬 상태로 유지하는 추가작업 필요
    - ```python
      def binarySearch(a, N, key):
        start = 0
        end = N-1
        while start <= end:
            middle = (start + end)//2
            if a[middle] == key:    # 검색 성공
                return true
            elif a[middle] > key:
                end = middle - 1
            else:
                start = middle + 1
        return false    # 검색 실패
      ```
---

> 인덱스
- 테이블 동작속도 높여주는 자료구조
- 인덱스 (키-필드만 갖고있음) 저장 디스크 공간은 테이블 저장 디스크 공간보다 작음
- 배열을 사용한 인덱스
    - 대량 데이터 성능 저하 문제 해결


> 선택 정렬 (Selection Sort)
- 주어진 자료 중 가장 작은 값의 원소부터 차례대로 선택하여 위치 교환
- 정렬과정  
    - 주어진 리스트 중 최소값을 찾는다
    - 그 값을 리스트 맨앞에 위치한 값과 교환
    - 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위 과정 반복
- 시간복잡도 : O(n^2)
- 알고리즘 기법 : 비교와 교환
- 교환 회수가 버블, 삽입 정렬보다 작다
- ```python
  def selectionSort(a, N):
    for i in range(N-1):
        minIdx = i  # 구간 맨앞을 최소값으로 가정
        for j in range(i+1, N): # 실제 최소값 인덱스 찾기
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]     # 최소값을 구간 맨앞으로! (j가 아니라 i!!!)
  ```

> 셀렉션 알고리즘 (Selection Algorithm)
- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
- 최소값, 최대값 혹은 중간값을 찾음
- 선택과정
  - 정렬을 통해 자료 정렬
  - 원하는 순서의 원소 가져오기


  