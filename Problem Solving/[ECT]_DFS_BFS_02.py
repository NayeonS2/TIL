# 미로 탈출

import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited[i][j] = 1

    while q:
        i,j = q.popleft()

        if i == N - 1 and j == M - 1:
            return visited[i][j]

        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni,nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj] == 1:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1


N,M = map(int,input().split())

arr = [list(map(int,input())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

print(bfs(0,0))