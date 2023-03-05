import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(i,j,diggable):
    global ans

    ans = max(ans,visited[i][j])

    for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:
        ni,nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0:
            if arr[ni][nj] < arr[i][j]:
                visited[ni][nj] = visited[i][j] + 1
                dfs(ni,nj,diggable)
                visited[ni][nj] = 0
            elif diggable > 0 and arr[ni][nj] - K < arr[i][j]:
                tmp = arr[ni][nj]
                visited[ni][nj] = visited[i][j] + 1
                arr[ni][nj] = arr[i][j] - 1
                dfs(ni,nj,diggable-1)
                visited[ni][nj] = 0
                arr[ni][nj] = tmp


for tc in range(1,T+1):
    N,K = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    ans = 0

    top_num = 0

    for i in range(N):
        top_num = max(top_num, max(arr[i]))

    for i in range(N):
        for j in range(N):
            if arr[i][j] == top_num:
                visited[i][j] = 1
                dfs(i,j,1)
                visited[i][j] = 0

    print(f'#{tc} {ans}')
