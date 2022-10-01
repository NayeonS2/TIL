# 보급로
from collections import deque
import sys
sys.stdin = open('input.txt')

INF = int(1e9)

def dijkstra(i,j):
    q = deque()
    q.append((i,j))

    visited[i][j] = 1

    while q:
        i, j = q.popleft()

        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
                depth = arr[ni][nj]
                if dist[ni][nj] > dist[i][j] + depth:
                    dist[ni][nj] = dist[i][j] + depth

                    q.append((ni,nj))

    return dist[N-1][N-1]


T = int(input())

for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]

    dist = [[INF] * N for _ in range(N)]

    dist[0][0] = 0

    print(f'#{tc} {dijkstra(0,0)}')