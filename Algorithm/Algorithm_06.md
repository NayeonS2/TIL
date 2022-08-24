# 6. 큐 (Queue)

> 큐의 특성
- 스택과 마찬가지로 삽입 삭제 위치가 제한적인 자료구조
- 큐 뒤에서는 삽입만, 큐 앞에서는 삭제만
- 선입선출 (FIFO)
- 큐에 삽입한 순서대로 원소 저장, 가장 먼저 삽입된 원소가 가장 먼저 삭제

> 큐의 선입선출 구조
- 머리 (Front) : 저장된 원소 중 첫번째 원소 (또는 삭제된 위치) - 마지막으로 꺼낸 자리
- 꼬리 (Rear) : 저장된 원소중 마지막 원소 - 마지막 저장 위치

> 큐의 기본 연산
- 삽입 : enQueue 큐 뒤쪽(rear 다음)에 원소를 삽입
  - rear += 1
  - Q[real] = A
- 삭제 : deQueue 큐 앞쪽(front)에서 원소를 삭제하고 반환
  - front == rear 이면 큐가 빈 상태가 됨
- createQueue() : 공백 상태 큐 생성
  - Q = [0] * N
  - front = rear = -1
- isEmpty() : 큐가 공백인지 확인
- isFull() : 큐가 포화인지 확인
- Qpeek() : 큐 앞쪽(front)에서 원소를 삭제없이 반환

> 큐의 구현
- 선형큐
  - 1차원 배열을 이용한 큐
    - 큐의 크기 = 배열 크기
    - front : 저장된 첫번째 원소 인덱스
    - rear : 저장된 마지막 원소 인덱스

  - 상태표현
    - 초기상태 : front = rear = -1
    - 공백상태 : front == rear
    - 포화상태 : rear == n-1 (n: 배열크기, n-1: 배열 마지막 인덱스)

- 초기 공백 큐 생성
  - 크기 n인 1차원 배열 생성
  - front, rear를 -1로 초기화

- 삽입 : enQueue(item)
  - 마지막 원소뒤에 새로운 원소 삽입위해
  - rear 값을 하나 증가시며 새로운 원소 삽입 자리 마련
  - 그 인덱스에 해당하는 배열원소 Q[rear]에 item 저장
  - ```python
    def enQueue(item):
        global rear
        if isFull(): print("Queue_Full")
        else:
            rear += 1
            Q[rear] = item
    ```

- 삭제 : deQueue()
  - 가장 앞에 있는 원소 삭제 위해
  - front 값을 하나 증가시켜 큐에 남아있게 될 첫번째 원소 이동
  - 새로운 첫번째 원소를 리턴함으로써 삭제와 동일한 기능
  - ```python
    deQueue()
    global front
        if(isEmpty()) then Queue_Empty();
        else{
            front += 1
            return Q[front]
        }
    ```

- 공백상태 및 포화상태 검사 : isEmpty() isFull()
  - 공백상태 : front == rear
  - 포화상태 : rear == n-1

- 검색 : Qpeek()
  - 가장 앞에있는 원소 검색하여 반환
  - 현재 front의 한자리 뒤(front+1)에 있는 원소, 즉 큐의 첫번째 원소 반환
  - ```python
    def Qpeek():
        if isEmpty() : print("Queue_Empty")
        else: return Q[front+1]
    ```

---

> 선형 큐 이용시 문제점
- 잘못된 포화상태 인식
  - 선형 큐 이용하여 삽입 삭제 계속하면, 배열 앞부분에 활용할 수 있는 공간이 있음에도 rear = n-1 상태 즉 포화상태로 인식하여 더이상 삽입 수행 x
  - 해결방법1
    - 매 연산이 이루어질때마다 저장된 원소들을 배열 앞부분으로 모두 이동
    - 원소이동에 많은 시간 소요, 효율성 저하
  - 해결방법2
    - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정

> 원형 큐의 구조
- 초기 공백 상태
  - front = rear = 0
- Index의 순환
  - front와 rear 위치가 배열 마지막 인덱스인 n-1가리킨후 그다음에는 논리적 순환, 배열 첫 인덱스인 0으로 이동
  - 나머지 연산자 mod사용
  - front 변수
    - 공백 상태와 포화상태 구분을 쉽게 하기 위해 front가 있는 자리는 사용하지 않고 **항상 빈자리로 둠**
  - 삽입 위치 및 삭제 위치
    - 선형 큐
      - 삽입 위치 : rear = rear + 1
      - 삭제 위치 : front = front + 1
    - 원형 큐
      - 삽입 위치 : rear = (rear+1)mod n
      - 삭제 위치 : front = (front+1)mod n

> 원형 큐의 구현
- 초기 공백 큐 생성
  - 크기 n인 1차원 배열 생성
  - front와 rear를 0으로 초기화

- 공백상태 및 포화상태 검사 : isEmpty() isFull()
  - 공백상태 : front == rear
  - 포화상태 : 삽입할 rear의 다음 위치 == 현재 front
    - (real+1)mod n == front
  - ```python
    def isEmpty() :
        return front == rear
    def isFull() :
        return (rear+1) % len(cQ) == front
    ```

- 삽입 : enQueue(item)
  - 마지막 원소 뒤에 새로운 원소삽입위해
  - rear 값 조정, 새로운 원소 삽입 자리 마련
  - rear = (real+1)mod n
  - 그 인덱스에 해당하는 배열원소 cQ[rear]에 item을 저장
  - 포화상태일땐 밀면서 덮어쓰는 느낌
  - ```python
    def enQueue(item):
        global rear
        if isFull(): print("Queue_Full")
        else:
            rear = (rear + 1) % len(cQ)
            cQ[rear] = item
    ```

- 삭제 : deQueue(), delete()
  - 가장 앞 원소 삭제 위해
  - front 값 조정, 삭제할 자리 준비
  - 새로운 front 원소를 리턴, 삭제와 동일 기능
  - ```python
    def deQueue(item):
        global front
        if isEmpty(): print("Queue_Empty")
        else:
            front = (front + 1) % len(cQ)
            return cQ[front]    
    ```
---

> 우선순위 큐 (Priority Queue)
- 우선순위를 가진 항목들을 저장하는 큐
- FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나감
- ex) 시뮬레이션 시스템, 네트워크 트래픽 제어, 운영체제의 테스크 스케줄링

> 우선순위 큐의 구현
- 배열을 이용한 우선순위 큐
- 리스트를 이용한 우선순위 큐

> 우선순위 큐 기본 연산
- 삽입 : enQueue
- 삭제 : deQueue

> 배열을 이용하여 우선순위 큐 구현
- 배열은 이용해 자료 저장
- 원소를 삽입하는 과정에서 우선순위 비교하여 적절 위치에 삽입
- 가장 앞에 최고 우선순위 원소가 위치
- 배열 + 트리구조
- but, 배열을 사용하므로 삽입이나 삭제 연산이 일어날때 원소 재배치가 발생
- 이에 소요되는 시간이나 메모리 낭비가 큼

---

> 큐의 활용: 버퍼(Buffer)
- 버퍼 : 데이터를 한곳에서 다른 한곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리의 영역
- 버퍼링 : 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작


  > 버퍼의 자료 구조
  - 버퍼는 일반적으로 입출력 및 네트워크와 관련된 기능에서 이용됨
  - 순서대로 입출력 전달 되어야하므로 FIFO방식의 자료구조인 큐가 활용됨

---

> BFS (Breadth Frist Search)
- 그래프 너비 우선 탐색
- 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문
- 인접 정점들에 대해 탐색 후, 차례로 다시 너비우선탐색을 진행해야하므로, 선입선출 형태의 큐를 활용
- ex) 미로, 그래프 
  - A->B : 경로가 있는가? (DFS, BFS)
  - A->B : 경로의 개수는? (DFS)
  - A->B : 최단 경로 길이는? (BFS > DFS)

- ```python
  def BFS(G,v)                          # 그래프 G, 탐색시작점 v
    visited = [0] * (n+1)               # n : 정점 개수
    queue = []                          # 큐 생성
    queue.append(v)                     # 시작점 v를 큐에 삽입

    while queue:                        # 큐가 비어있지 않은 경우
        t = queue.pop(0)                # 큐 첫번째 원소 반환
        if not visited[t]:              # 방문되지 않은 곳이라면
            visited[t] = 1              # 방문한 것으로 표시
            visit(t)                    # 정점 t에서 할일
            for i in G[t]:              # t와 연결된 모든 정점에 대해
                if not visited[i]:      # 방문되지 않은 곳이라면
                    queue.append(i)     # queue에 넣기
                    visited[i] = visited[n] +1 # n으로부터 1만큼
    ```

```python
# 기본 BFS
# A~G :
# adjList = [[1,2],[0,3,4],[0,4],[1,5],[1,2,5],[3,4,6],[5]] -> 0~6

def BFS(v,N):   # 탐색 시작점 v, 마지막 정점 N
    visited = [0]*(N+1)
    q = []

    q.append(v)
    visited[v] = 1

    while q:
        v = q.pop(0)
        #visit(t)
        print(V)
        for w in adjList[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1     # t로부터 1만큼


V, E = map(int,input().split())
N = V+1
adjList = [[] for _ in range(N)]

for _ in range(E):
    a,b = map(int,input().split())
    adjList[a].append(b)
    adjList[b].append(a)

BFS(0,V)
```

```python
# swea 길찾기

def bfs(v, N, t):
    visited = [0] * (N+1)
    q= []
    q.append(v)
    visited[v] = 1
    while q:
        v = q.pop(0)
        if v == t:
            return 1
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] +1

    return 0



T = 10
for _ in range(1,T+1):
    tc, E = map(int,input().split())
    arr = list(map(int,input().split()))

    adjList = [[] for _ in range(100)]

    for i in range(E):
        a,b = arr[i*2], arr[i*2+1]
        adjList[a].append(b)

    bfs(0,99, 99)   # 시작, 마지막, 목표
```

```python
# swea 미로
# visited 디버깅하면 최단경로 찾기 가능!

import sys
sys.stdin = open('input.txt')


def bfs(i,j,N):
    visited = [[0]*N for _ in range(N)]
    q = []
    q.append((i,j))
    visited[i][j] = 1

    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return visited[i][j]    # 최단경로 길이
            #return 1

        for di, dj in [[0,1], [1,0],[0,-1],[-1,0]]:
            ni, nj = i+di , j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return -1
    #return 0



T = int(input())

for tc in range(1,1+T):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break
    print(f'#{tc} {bfs(sti,stj,N)}')
```

```python
# DFS 최단경로 -> 모든 경로를 돌아봐야함 (경로의 수)


import sys
sys.stdin = open('input.txt')


def dfs(i,j,N):
    global answer
    if maze[i][j] == 3:
        answer += 1
        return
    else:
        visited[i][j] = 1   # 아예 방문 표시안하면 무한 loop
        for di, dj in [[0,1], [1,0],[0,-1],[-1,0]]:
            ni, nj = i+di , j+dj
            if maze[ni][nj]!=1 and visited[ni][nj]==0:  # 벽으로 둘러쌓인 미로
                dfs(ni,nj,N)
        visited[i][j] = 0   # 다른쪽을 통해서 오는 것을 허용해줌!
        return





T = int(input())

for tc in range(1,1+T):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    answer = 0  # 경로 수
    visited = [[0] * N for _ in range(N)]
    dfs(sti,stj,N)
    print(answer)
```

```python
# dfs 최단경로 길이

import sys
sys.stdin = open('input.txt')


def dfs(i,j,s,N):
    global minV
    if maze[i][j] == 3:
        if minV > s+1:  # 출발도착 포함 길이
            minV = s+1
        return
    else:
        visited[i][j] = 1   # 아예 방문 표시안하면 무한 loop
        for di, dj in [[0,1], [1,0],[0,-1],[-1,0]]:
            ni, nj = i+di , j+dj
            if maze[ni][nj]!=1 and visited[ni][nj]==0:  # 벽으로 둘러쌓인 미로
                dfs(ni,nj,s+1,N)
        visited[i][j] = 0   # 다른쪽을 통해서 오는 것을 허용해줌!
        return





T = int(input())

for tc in range(1,1+T):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    sti = -1
    stj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    answer = 0  # 경로 수
    minV = N*N  # 최단거리 길이
    visited = [[0] * N for _ in range(N)]
    dfs(sti,stj,0,N)
    if minV == N*N:
        minV = -1
    print(minV)
```

```python
# 복수 출발 미로 (방향제 퍼지는 시간?)
#bfs

import sys
sys.stdin = open('input.txt')


def bfs(N):
    visited = [[0]*N for _ in range(N)]
    q = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                q.append((i,j))
                visited[i][j] = 1

    while q:
        i, j = q.pop(0)

        for di, dj in [[0,1], [1,0],[0,-1],[-1,0]]:
            ni, nj = i+di , j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return
    #return 0



T = int(input())

for tc in range(1,1+T):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]


    print(f'#{tc} {bfs(N)}')
```



### 탐색
- 빠짐없이, 중복없이 : DFS / BFS
- 최단거리 : DFS / BFS
- 경로의 수 : DFS
- 확산 (출발 여러곳) : BFS
