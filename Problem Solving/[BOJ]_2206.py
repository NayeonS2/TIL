# 벽부수고 이동하기

from collections import deque

import sys
sys.stdin = open('input.txt')

def bfs(i, j, hit):
    q = deque()
    q.append((i, j, hit))

    while q:
        i, j, hit = q.popleft()

        if i == N - 1 and j == M - 1:
            return visited[i][j][hit]

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 > ni or ni >= N or 0 > nj or nj >= M:
                continue
            if arr[ni][nj] == 1 and hit == 0:
                visited[ni][nj][1] = visited[i][j][0] + 1
                q.append((ni, nj, 1))
            elif arr[ni][nj] == 0 and visited[ni][nj][hit] == 0:
                visited[ni][nj][hit] = visited[i][j][hit] + 1
                q.append((ni, nj, hit))

    return -1


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

print(bfs(0,0,0))



