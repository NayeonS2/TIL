# 아기상어2
# 상어 위치로 부터 거리 표시하기

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

def bfs():
    q = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i,j))

    while q:
        i,j = q.popleft()

        for di,dj in [[-1,0],[1,0],[0,-1],[0,1],[1,1],[-1,1],[1,-1],[-1,-1]]:
            ni, nj = i+di, j+dj

            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                arr[ni][nj] = arr[i][j]+1
                q.append((ni,nj))


bfs()
print(max(map(max,arr))-1)

