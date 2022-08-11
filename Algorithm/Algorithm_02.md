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
> 델타를 이용한 2차 배열 탐색
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
            if 0 <= ni < N and 0 <= nj < N: #유효한 인덱스면
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
- << : 피연산자의 비트 열을 왼쪽으로 이동
- '>> : 피연산자의 비트 열을 오른쪽으로 이동

> << 연산자
- 1 << n : 2^n (즉 원소가 n개일경우 모든 부분집합의 수)

> & 연산자
- i & (1<<i) : i의 j번째 비트가 1인지 검사 (0이면 결과가 0)

> 보다 간결하게 부분집합을 생성하는 방법!!
- ```python
  arr = [3,6,7,1,5,4]
  n = len(arr)  # 원소의 개수
  for i in range(1<<n): # 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트 비교
        if i & (1<<j):  # i의 j번 비트가 1인 경우
            print(arr[j], end=", ")     # j번 원소 출력!
    print()
  print()

        

  