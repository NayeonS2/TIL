# 여행계획
# 여행이 가능한지 확인

import sys

sys.stdin = open('input.txt')


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [0] * (N + 1)
# 간선정보
edges = []

# 인접행렬
arr = [list(map(int, input().split())) for _ in range(N)]
# 여행계획
plan = list(map(int,input().split()))

# 연결된 간선 찾기 (인접행렬)
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if arr[i-1][j-1] == 1:
            edges.append((i, j))

# 연결되었으면 union
for edge in edges:
    a,b = edge
    union_parent(parent,a,b)

# 여행계획 모든 노드의 parent가 동일한지(서로 연결되어있는지) 확인
result = []
for node in plan:
    result.append(find_parent(parent,node))

if len(set(result)) == 1:
    print("YES")
else:
    print("NO")

