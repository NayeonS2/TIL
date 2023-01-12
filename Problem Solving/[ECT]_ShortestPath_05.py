# 화성 탐사

import sys, heapq
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    n = int(input())

    INF = int(1e9)
    distance = [[INF]*(n) for _ in range(n)]

    graph = [list(map(int,input().split())) for _ in range(n)]

    def dijkstra(i,j):
        visitied = [[0]*(n) for _ in range(n)]
        q = []
        heapq.heappush(q,(graph[i][j],(i,j)))
        distance[i][j] = graph[i][j]
        visitied[i][j] = 1

        while q:
            cost, (n_i, n_j) = heapq.heappop(q)

            if distance[n_i][n_j] < cost:
                continue

            for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                ni,nj = n_i+di, n_j+dj

                if 0<=ni<n and 0<=nj<n:
                    new_cost = cost + graph[ni][nj]
                    if not visitied[ni][nj] and new_cost < distance[ni][nj]:
                        distance[ni][nj] = new_cost
                        visitied[ni][nj] = 1
                        heapq.heappush(q,(new_cost,(ni,nj)))

    dijkstra(0,0)
    print(distance[n-1][n-1])


