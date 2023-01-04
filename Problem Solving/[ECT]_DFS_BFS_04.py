# 연구소
# 안전영역의 수가 최대가 되게 벽 3개 세우기
# 0은 빈칸, 1은 벽, 2는 바이러스
# 벽을 세웠다가 없앴다가 하며 완탐

import sys, copy
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 0

def bfs():
    global ans
    q = deque()
    tmp_arr = copy.deepcopy(arr)

    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 2:
                q.append((i,j))

    while q:
        i,j = q.popleft()

        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni,nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and tmp_arr[ni][nj] == 0:
                tmp_arr[ni][nj] = 2
                q.append((ni,nj))

    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 0:
                cnt += 1
    ans = max(cnt,ans)
    return

def wall(cnt):

    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

wall(0)
print(ans)


