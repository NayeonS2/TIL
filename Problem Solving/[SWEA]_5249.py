# 최소신장트리

import sys
sys.stdin = open('input.txt')

def find_parent(parent,x):
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


T = int(input())

for tc in range(1,1+T):
    V, E = map(int,input().split())

    edges = []
    result = 0

    parent = [0] * (V+1)

    for i in range(1,V+1):
        parent[i] = i

    for _ in range(E):
        a, b, w = map(int,input().split())

        edges.append((w,a,b))

    edges.sort()

    for edge in edges:
        w, a, b = edge

        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += w

    print(f'#{tc} {result}')