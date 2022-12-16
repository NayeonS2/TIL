# 도시 분할 계획
# BOJ 1647
# 2개의 분리된 마을로 분할할 계획
# 길을 없애고 남은 유지비의 합의 최솟값 (MST)

# 최소신장트리를 찾은 후 가장 비용이 큰 간선을 제거!

import sys
sys.stdin = open('input.txt')

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b


v,e = map(int,input().split())
parent = [0]*(v+1)
for i in range(1,v+1):
    parent[i] = i

edges = []
result = 0

for _ in range(e):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()
last = 0

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost

print(result-last)


