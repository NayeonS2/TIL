# 어두운 길
# 일부 가로등 비활성화하여 절약할 수 있는 최대 금액
# mst

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

N,M = map(int,input().split())

parent = [0]*(N+1)

for i in range(1,N+1):
    parent[i] = i

edges = []
money = 0
saving = 0
for _ in range(M):
    a, b, cost = map(int,input().split())
    edges.append((cost,a,b))

edges.sort()

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        #money += cost
    else:
        # 절약된 금액 구하기 위해 else일때만 saving 갱신
        saving += cost

print(saving)

