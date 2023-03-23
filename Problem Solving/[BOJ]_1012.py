# 유기농 배추

import sys
sys.setrecursionlimit(100000)
sys.stdin = open('input.txt')

T = int(input())

def dfs(arr,i,j):

    if i>=N or i<0 or j>=M or j<0:
        return False

    if arr[i][j] == 1:
        arr[i][j] = 0
        dfs(arr,i+1,j)
        dfs(arr,i-1,j)
        dfs(arr,i,j-1)
        dfs(arr,i,j+1)
        return True

    return False


for tc in range(1,T+1):
    M,N,K = map(int,input().split())
    arr = [[0]*M for _ in range(N)]

    for _ in range(K):
        X,Y = map(int,input().split())
        arr[Y][X] = 1

    res = 0
    for i in range(N):
        for j in range(M):
            if dfs(arr,i,j) == True:
                res += 1

    print(res)


