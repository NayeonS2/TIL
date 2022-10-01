# 창용 마을 무리의 개수

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


T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split())

    parent = [0] * (N+1)

    edges = []

    for i in range(1,N+1):
        parent[i] = i

    for _ in range(M):
        a,b = map(int,input().split())

        union_parent(parent,a,b)

    cnt = set()

    for i in parent:
        cnt.add(find_parent(parent,i))

    print(f'#{tc} {len(cnt)-1}')