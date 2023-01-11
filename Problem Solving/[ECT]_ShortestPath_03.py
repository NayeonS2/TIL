# 플로이드

import sys, heapq
sys.stdin = open('input.txt')


n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    if c < graph[a][b]:
        graph[a][b] = c


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0

for i in range(1,n+1):
    print(*graph[i][1:])
