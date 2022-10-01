# 그룹 나누기

import sys
sys.stdin = open('input.txt')

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b


T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split())

    parent = [0] * (N+1)

    edges = []

    for i in range(1, N+1):
        parent[i] = i

    info = list(map(int, input().split()))
    for i in range(0,M*2,2):
        a, b = info[i:i+2][0], info[i:i+2][1]

        union_parent(parent, a, b)
    answer = set()

    for i in parent:
        answer.add(find_parent(parent,i))

    print(f'#{tc} {len(answer)-1}')