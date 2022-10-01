# 최소비용

import sys
sys.stdin = open('input.txt')
INF = int(1e9)

def dijkstra(i,j):
    q = []
    q.append((i,j))

    visited[i][j] = 1

    while q:
        i, j = q.pop(0)

        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                diff = 0
                if arr[ni][nj] > arr[i][j]:
                    diff = arr[ni][nj] - arr[i][j]

                if dist[ni][nj] > dist[i][j] + diff + 1:
                    dist[ni][nj] = dist[i][j] + diff + 1

                    q.append((ni, nj))

    return dist[N-1][N-1]


T = int(input())

for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    dist = [[INF]*N for _ in range(N)]

    dist[0][0] = 0

    print(f'#{tc} {dijkstra(0,0)}')