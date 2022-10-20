# 음료수 얼려 먹기

def dfs(i,j):

    if i<0 or i>=N or j<0 or j>=M:
        return False
    if arr[i][j] == 0:
        arr[i][j] = 1
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)
        return True
    return False

import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())

arr = [list(map(int,input())) for _ in range(N)]

res = 0
for i in range(N):
    for j in range(M):
        if dfs(i,j):
            res += 1
print(res)

