# 음식물 피하기

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(i,j):
    global cnt

    if i<0 or i>=N or j<0 or j>=M:
        return False

    if visited[i][j] == 0 and arr[i][j] == 3:

        visited[i][j] = 1
        cnt += 1

        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
        return True
    return False

N,M,K = map(int,input().split())

arr = [[0]*M for _ in range(N)]

visited = [[0]*M for _ in range(N)]


for _ in range(K):
    i_,j_ = map(int,input().split())
    i,j = i_-1, j_-1
    arr[i][j] = 3

cnt = 0
res = []
for i in range(N):
    for j in range(M):
        if dfs(i,j):
            res.append(cnt)
            cnt = 0
print(max(res))


