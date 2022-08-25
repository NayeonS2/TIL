
import sys
sys.stdin = open('input.txt')


def bfs(i,j,N):
    visited = [[0] * N for _ in range(N)]
    q = []
    q.append((i,j))
    visited[i][j] =1

    while q:
        i, j = q.pop(0)
        if maze[i][j] == 3:
            return visited[i][j] - 2

        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0



T = int(input())

for tc in range(1,1+T):
    N = int(input())

    maze = [list(map(int,input())) for _ in range(N)]

    si = -1
    sj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j
                break
        if si != -1:
            break
    print(f'#{tc} {bfs(si,sj,N)}')