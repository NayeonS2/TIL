# 플로이드 워셜
# 모든 지점에서 다른 모든 지점까지의 최단경로를 모두 구해야하는 경우
# A에서 B로가는 최소 비용과 A에서 K를 거쳐 B로가는 비용을 비교하여 더 작은 값으로 갱신

import sys
sys.stdin = open("input.txt")

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF:
            print("INFINITY",end=" ")
        else:
            print(graph[a][b], end=" ")
    print()