# 7. 트리 (Tree)

## 트리

### 트리의 개념
- 비선형 구조
- 순환될 수 없는 구조
- 그래프의 하위 개념
- 원소들 간에 1:n 관계를 가지는 자료구조
- 원소들 간에 계층관계를 가지는 계층형 자료구조
- 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조
- 한 개 이상의 노드로 이루어진 유한 집합
  - 노드 중 최상위 노드를 루트(root)라 함
  - 나머지 노드들은 n(>=0)개의 분리 집합 T1,...,TN으로 분리 가능
- 이들 T1,...,TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리(subtree)라 함

### 트리 용어 정리
- 노드(node) - 트리의 원소
- 간선(edge) - 노드를 연결하는 선. 부모노드와 자식노드를 연결
- 루트노드(root node) - 트리의 시작 노드
- 형제노드(sibling node) - 같은 부모 노드의 자식 노드들
- 조상노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- 서브트리(subtree) - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손노드 - 서브트리에 있는 하위 레벨의 노드들
- 차수(degree)
  - 노드의 차수 : 노드에 연결된 자식 노드의 수
  - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
  - 단말 노드(리프노드) : 차수가 0인 노드, 자식 노드가 없는 노드
- 높이
  - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
  - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨

---
## 이진트리
- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리
  - 왼쪽 자식 노드(left child node)
  - 오른쪽 자식 노드(right child node)

### 이진트리 - 특성 **
- 레벨 i에서의 노드의 최대 개수는 **2^i 개**
- 높이가 h인 이진트리가 가질 수 있는 노드의 최소 개수는 **(h+1)개**가 되며, 최대 개수는 **(2^(h+1) - 1)개**가 됨

### 이진트리 - 종류
- **포화 이진 트리 (Full Binary Tree)**
  - **모든 레벨에 노드가 포화상태**로 차 있는 이진 트리
  - 높이가 h일때, 최대의 노드 개수인 (2^(h+1) - 1)의 노드를 가진 이진 트리
  - 루트를 1번으로 하여 (2^(h+1) - 1)까지 정해진 위치에 대한 노드 번호를 가짐
- **완전 이진 트리 (Complete Binary Tree)**
  - 높이가 h이고 노드 수가 n개 일때 (단, h+1 <= n <= (2^(h+1) - 1)), 포화 이진 트리의 노드 번호 **1번부터 n번까지 빈 자리가 없는** 이진 트리
- **편향 이진 트리 (Skewed Binary Tree)**
  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
    - 왼쪽 편향 이진 트리
    - 오른쪽 편향 이진 트리
    - 최악의 시간 복잡도

### 이진트리 - 순회 (traversal)
- **순회(traversal)**란 트리의 각 노드를 중복되지 않게 전부 방문(visit)하는 것을 말하는데 트리는 비 선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다.
- 순회(traversal) : 트리의 노드들을 체계적으로 방문하는 것
- **전위 순회 (preorder traversal)** : VLR
  - 부모 노드 방문 후, 자식 노드를 좌,우 순서로 방문
- **중위 순회 (inorder traversal)** : LVR
  - 왼쪽 자식 노드, 부모 노드, 오른쪽 자식 노드 순으로 방문
- **후위 순회 (postorder traversal)** : LRV
  - 자식 노드를 좌,우 순서로 방문 후, 부모 노드로 방문
  

### 전위 순회 (preorder traversal)
- 수행 방법
  - 1. 현재 노드 n을 방문하여 처리 -> V
  - 2. 현재 노드 n의 왼쪽 서브트리로 이동 -> L
  - 3. 현재 노드 n의 오른쪽 서브트리로 이동 -> R
- 전위 순회 알고리즘
```python
def preorder_traversal(T):
    if T:   # T is not None
        visit(T)    # print(T.item)
        preorder_traversal(T.left)
        preorder_traversal(T.right)
```

### 중위 순회 (inorder traversal)
- 수행 방법
  - 1. 현재 노드 n의 왼쪽 서브트리로 이동 -> L
  - 2. 현재 노드 n을 방문하여 처리 (**왼쪽에서 되돌아올때 방문처리!!!**) -> V
  - 3. 현재 노드 n의 오른쪽 서브트리로 이동 -> R
- 중위 순회 알고리즘
```python
def inorder_traversal(T):
    if T:   # T is not None
        inorder_traversal(T.left)
        visit(T)    # print(T.item)
        inorder_traversal(T.right)
```

### 후위 순회 (postorder traversal)
- 수행 방법
  - 1. 현재 노드 n의 왼쪽 서브트리로 이동 -> L
  - 2. 현재 노드 n의 오른쪽 서브트리로 이동 -> R
  - 3. 현재 노드 n을 방문하여 처리 -> V

- 후위 순회 알고리즘
```python
def postorder_traversal(T):
    if T:   # T is not None
        postorder_traversal(T.left)
        postorder_traversal(T.right)
        visit(T)    # print(T.item)
        
```

### 이진트리의 표현 - 배열
- 포화 or 완전 이진 트리의 경우에 한해서!!
- **노드 번호의 성질**
  - 노드 번호가 i인 노드의 부모 노드 번호 : i/2
  - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호 : 2*i
  - 노드 번호가 i인 노드의 오른쪽 자식 노드 번호 : 2*i+1
  - 레벨 n의 노드 번호 시작 번호 : 2^n
- 리스트로 표현
- 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
- 트리 중간에 새로운 노드를 삽입하거나 기존 노드를 삭제할 경우 배열의 크기 변경이 어려워 비효율적

### 이진트리의 저장
- 1. 부모 번호를 인덱스로 자식 번호를 저장
  - 순회 할 때 유용
  - 자식은 들어온 순서대로 해당 인덱스가 비어있을때만!
  - 트리에서 간선수 + 1 = 정점수
- 2. 자식 번호를 인덱스로 부모 번호를 저장
  - 루트 찾기, 조상 찾기에 유용

```python
# 정점 번호 1 ~ (E+1)
# 간선 수
# 부모-자식 순
# 4
# 1 2 1 3 3 4 3 5

def preorder(n):    # 전위순회
    if n:
        print(n)    # visit(n)
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):     # 중위순회
    if n:
        inorder(ch1[n])
        print(n)    # visit(n)
        inorder(ch2[n])

def postorder(n):   # 후위순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)    # visit(n)


def find_root(V):
    for i in range(1, V+1):
        if par[i] == 0:     # 부모가 없으면 root임
            return i



E = int(input())
arr = list(map(int,input().split()))
V = E + 1
root = 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0]*(V+1)
ch2 = [0]*(V+1)

# 자식을 인덱스로 부모 번호 저장
par = [0]*(V+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    
    if ch1[p] == 0:     # 아직 자식이 없으면
        ch1[p] = c      # 자식1로 저장
    else:
        ch2[p] = c

    par[c] = p

root = find_root(V)
print(root)

preorder(root)  # 1 2 3 4 5
inorder(root)   # 2 1 4 3 5
postorder(root) # 2 4 5 3 1
```









