import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b



for tc in range(1,1+T):
    N = int(input())

    parent = [0]*(N)

    for i in range(N):
        parent[i] = i

    x = list(map(int,input().split()))
    y = list(map(int,input().split()))

    E = float(input())

    tmp = []

    for i in range(N):
        tmp.append((i,x[i],y[i]))

    combs = list(combinations(tmp,2))

    edges = []

    for comb in combs:
        L = (comb[0][1]-comb[1][1])**2 + (comb[0][2]-comb[1][2])**2
        w = E * L
        edges.append((w,comb[0][0],comb[1][0]))

    edges.sort()

    result = 0
    for edge in edges:
        a,b = edge[1],edge[2]

        if find_parent(parent,a) != find_parent(parent,b):
            union_parent(parent,a,b)
            result += edge[0]
    print(f'#{tc} {int(result)}')








