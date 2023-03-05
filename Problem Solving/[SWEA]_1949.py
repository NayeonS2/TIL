# 등산로 조성

import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')

def dfs(i,j,diggable):

    global ans

    ans = max(ans,visited[i][j])    # 최대 길이 갱신

    for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
            if arr[ni][nj] < arr[i][j]: # 다음 이동할 위치가 현재 위치보다 낮으면 방문, 거리저장
                visited[ni][nj] = visited[i][j] + 1
                dfs(ni,nj,diggable)
                visited[ni][nj] = 0
            elif diggable > 0 and arr[ni][nj] - K < arr[i][j]:  # 땅을 팔 기회가 남았고, 파고나서 높이가 현재 위치보다 낮으면
                tmp = arr[ni][nj]
                arr[ni][nj] = arr[i][j] - 1 # 1~k 까지 다 파보지않고도, 현재높이보다 1만큼만 낮게 만들어주면 충분
                visited[ni][nj] = visited[i][j] + 1
                dfs(ni,nj,diggable-1)
                arr[ni][nj] = tmp
                visited[ni][nj] = 0


T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]


    visited = [[0]*(N) for _ in range(N)]


    top_num = 0 # 최대 높이 구하기

    for i in range(N):
        top_num = max(top_num,max(arr[i]))


    ans = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == top_num:    # 최대높이지점이면 방문처리하고 dfs
                visited[i][j] = 1
                dfs(i,j,1)  # 최대 길이 갱신
                visited[i][j] = 0

    print(f'#{tc} {ans}')







