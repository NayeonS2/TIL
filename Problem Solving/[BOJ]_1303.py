# 전쟁 - 전투

def dfs(i,j,type,cnt):

    visited[i][j] = 1

    for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
        ni,nj = i+di, j+dj
        if 0<=ni<M and 0<=nj<N and visited[ni][nj] == 0:
            if arr[ni][nj] == type:
                dfs(ni,nj,type,cnt+1)


    return cnt


N,M = map(int,input().split())

arr = [list(input()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
power_w = 0
power_b = 0

for i in range(M):
    for j in range(N):
        if arr[i][j] == 'W':

            ans = dfs(i,j,'W',1)
            power_w += ans**2


for i in range(M):
    for j in range(N):
        if arr[i][j] == 'B':

            ans = dfs(i, j, 'B',1)
            power_b+=ans**2


print(power_w,power_b)


