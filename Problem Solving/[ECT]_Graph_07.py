# 행성 터널
# combination쓰니까 메모리초과!
# x,y,z축에 대해 정렬 후, 각각 N-1개 간선만 고려

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

N = int(input())
E = N-1
parent = [0]*(N+1)

# 각 노드 위치 정보
x_pos = []
y_pos = []
z_pos = []

for i in range(1,N+1):
    parent[i] = i
    x,y,z = map(int,input().split())
    x_pos.append((x,i))
    y_pos.append((y,i))
    z_pos.append((z,i))

# x,y,z축에 대해 정렬 후, 각각 N-1개 간선만 고려
x_pos.sort()
y_pos.sort()
z_pos.sort()

# 인접노드끼리 x,y,z 축별로 cost계산해서 간선리스트에 정보 추가
edges = []
for e in range(E):
    edges.append((abs(x_pos[e+1][0]-x_pos[e][0]),x_pos[e][1],x_pos[e+1][1]))
    edges.append((abs(y_pos[e + 1][0] - y_pos[e][0]), y_pos[e][1], y_pos[e + 1][1]))
    edges.append((abs(z_pos[e + 1][0] - z_pos[e][0]), z_pos[e][1], z_pos[e + 1][1]))

# 비용기준 오름차순 정렬
edges.sort()
result = 0

# 사이클발생안하면 union
for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost

print(result)
