maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

from collections import deque

def bfs(i,j,maps):

    N = len(maps)
    M = len(maps[0])
    q = deque()
    visited = [[0]*M for _ in range(N)]
    q.append((i,j))
    visited[i][j] = 1


    while q:

        i,j = q.popleft()


        if i == N-1 and j == M-1:
            return visited[i][j]


        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni,nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and maps[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1


    return -1



def solution(maps):
    answer = bfs(0,0,maps)

    return answer

print(solution(maps))