# 신장트리
# 하나의 그래프가 있을때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분그래프

# 최소신장트리 (크루스칼)
# 최소한의 비용으로 연결할때
# 신장 트리 중 최소 비용으로 만들 수 있는 신장 트리를 찾는 알고리즘

# 비용에따라 간선을 오름차순 정렬
# 사이클이 발생하지 않으면 MST에 포함
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

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
print(result)

