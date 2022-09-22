import sys
sys.stdin = open('input.txt')


def dfs(i,j,s,N):
    global minV
    if i == N-1 and j == N-1:
        if minV > s:  # 최소합
            minV = s
        return
    else:
        visited[i][j] = 1   # 아예 방문 표시안하면 무한 loop
        for di, dj in [[0,1], [1,0]]:  # 아래 오른쪽 방향만 이동
            ni, nj = i+di , j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0:
                if s+arr[ni][nj] > minV:  # 백트래킹 조건
                    continue
                else:
                    dfs(ni,nj,s+arr[ni][nj],N)
        visited[i][j] = 0   # 다른쪽을 통해서 오는 것을 허용해줌!
        return


T = int(input())

for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    minV = 10*N*N
    visited = [[0] * N for _ in range(N)]
    dfs(0,0,arr[0][0],N)

    print(f'#{tc} {minV}')