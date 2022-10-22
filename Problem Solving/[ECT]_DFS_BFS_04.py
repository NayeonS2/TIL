# 연구소
# 안전영역의 수가 최대가 되게 벽 3개 세우기
# 벽을 세웠다가 없앴다가 하며 완탐하려면 dfs!

import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def virus(i,j):

    for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and tmp[ni][nj] == 0:
            tmp[ni][nj] = 2
            virus(ni,nj)

def safe_cnt():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt

def dfs(wall):
    global ans
    if wall == 3:
        for i in range(N):
            for j in range(M):
                tmp[i][j] = arr[i][j]

        for i in range(N):
            for j in range(M):
                if tmp[i][j] == 2:
                    virus(i,j)
        ans = max(ans, safe_cnt())
        return

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall += 1
                dfs(wall)
                arr[i][j] = 0
                wall -= 1

N, M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
tmp = [[0] * M for _ in range(N)]

ans = 0

dfs(0)
print(ans)