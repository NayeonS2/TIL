# 11. 분할 정복 & 백트래킹

## 분할 정복


### 분할 정복 기법
- 분할 (Divide) : 해결할 문제를 여러 개의 작은 부분으로 나눈다
- 정복 (Conquer) : 나눈 작은 문제를 각각 해결한다
- 통합 (Combine) : (필요하다면) 해결된 해답을 모은다

### 병합 정렬 (Merge Sort)
- 여러 개의 정렬된 자료의 집합을 병합하여 한 개의 정렬된 집합으로 만드는 방식
- 자료를 최소 단위 문제까지 나눈 후에 차례대로 정렬하여 최종결과 얻어냄
- top-down
- O(nlogn)
- 병합 정렬 과정
  - 분할 : 전체 자료 집합에 대해 최소 크기 부분집합이 될 때까지 분할 작업 계속
  - <img src="./algo_11_img.md/merge_sort01.png">
  - 병합 : 2개의 부분 집합을 정렬하면서 하나의 집합으로 병합
  - <img src="./algo_11_img.md/merge_sort02.png">


### 퀵 정렬
- 주어진 배열을 두 개로 분할하고, 각각을 정렬한다.
- 병합 정렬은 그냥 두 부분으로 나누지만, 퀵 정렬은 분할할 때 기준 아이템 (pivot item)을 중심으로 이보다 작은 것은 왼편, 큰 것은 오른편에 위치
- 각 부분 정렬이 끝난 후, 병합 정렬은 "병합"이란 후처리 작업이 필요하나, 퀵 정렬은 필요하지 않음
- Hoare-Partition 알고리즘
  
- <img src="./algo_11_img.md/quick01.png">
- <img src="./algo_11_img.md/quick02.png">
- <img src="./algo_11_img.md/quick03.png">
- <img src="./algo_11_img.md/quick04.png">
- <img src="./algo_11_img.md/quick05.png">
- <img src="./algo_11_img.md/quick06.png">

- Lomuto-Partition 알고리즘

- <img src="./algo_11_img.md/quick01_2.png"> 

```python
# 퀵 정렬 (Hoare-Partition)
def partition(l,r):
    pivot = A[l]
    i, j = l, r
    while i<=j:
        while i<=j and A[i] <= pivot:
            i += 1
        while i<=j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def qsort(l,r):
    if l < r:
        s = partition(l, r)
        qsort(l, s-1)
        qsort(s+1, r)

A = [7,2,5,3,4,5]
N = len(A)
qsort(0, N-1)
print(A)
```

## 이진 검색 (Binary Search)
- 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색 범위를 반으로 줄여가면서 보다 빠르게 검색을 수행
- 이진 검색을 하기 위해서는 자료가 정렬된 상태여야 함
- 검색과정  
  - 1) 자료 중앙에 있는 원소를 고른다
  - 2) 중앙 원소의 값과 찾고자 하는 목표 값을 비교
  - 3) 목표 값이 중앙 원소 값보다 작으면 자료의 왼쪽 반에 대해서 새로 검색, 크다면 오른쪽 반에 대해 새로 검색 수행
  - 4) 찾고자 하는 값을 찾을 때까지 1~3 과정 반복

## 분할 정복의 활용
- 병합 정렬은 외부 정렬의 기본이 되는 정렬 알고리즘
- 또한 멀티코어 CPU나 다수의 프로세서에서 정렬 알고리즘을 병렬화하기 위해 병합 정렬 알고리즘이 활용됨
- 퀵 정렬은 매우 큰 입력 데이터에 대해 좋은 성능을 보이는 알고리즘


## 백트래킹
- 여러가지 옵션들이 존재하는 상황에서 한가지 선택
- 선택이 이루어지면 새로운 선택지들의 집합이 생성됨
- 올바른 선택을 계속하면 목표 상태에 도달
- 백트래킹과 DFS의 차이
  - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임 (Prunning 가지치기)
  - DFS가 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
  - DFS를 하기에는 경우의 수가 너무나 많을때 (N! 가지 경우의 수를 가진 문제) 처리 불가능
  - 백트래킹 알고리즘을 적용하면 일반적으로 경우의 수가 줄어들지만 이 역시 최악의 경우에는 여전히 지수 함수 시간을 요하므로 처리 불가능 

### 백트래킹 개념
- 예시) N-Queen
- 모든 후보를 검사하지 않음
- 백트래킹 기법
  - 어떤 노드의 유망성을 점검 후 유망(promising)하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
  - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 한다.
  - 가지치기 (prunning): 유망하지 않는 노드가 포함되는 경로는 더이상 고려 x
  - 백트래킹 적용
    - 1) 상태 공간 트리의 DFS 실시
    - 2) 각 노드가 유망한지 점검 (조건 추가)
    - 3) 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색 계속 진행

```python
# 부분집합의 합
# {1,2,3,4,5,6,7,8,9,10}의 powerset 중 원소의 합이 10인 부분집합을 모두 출력

def f1(i, k, t): # 재귀횟수, 목표횟수, 목표 합
    global cnt
    if i == k:
        s = 0
        for j in range(10):
            if bit[j]:
                s += arr[j]
        if s == t:
            for j in range(10):
                if bit[j]:
                    print(arr[j], end=' ')
            print()
    else:
        bit[i] = 0
        f1(i + 1, k, t)
        bit[i] = 1
        f1(i + 1, k, t)


def f2(i, k, t, s, rs): # 재귀횟수, 목표횟수, 목표 합, 지금까지의 합, 앞으로 더해질 수 있는 남은 원소들의 합
    global cnt
    cnt += 1

    if s > t:
        return
    if t > s + rs:  # 지금까지 합이랑 앞으로 더해질 수 있는 합을 합한게 목표합보다 작으면 의미 없음
        return

    if i == k:  # 모든 원소에 대한 검사가 끝났을 때
        if s == t:
            for j in range(10):
                if bit[j]:
                    print(arr[j], end = ' ')
            print()
    else:
        bit[i] = 0
        f2(i + 1, k, t, s, rs - arr[i])
        bit[i] = 1
        f2(i + 1, k, t, s + arr[i], rs - arr[i])


arr = [i for i in range(1, 11)]
bit = [0] * 10
cnt = 0
# f1(0, 10, 10)
f2(0, 10, 10, 0, sum(arr))
print(cnt)
```

