# 벽부수고 이동하기

# 3차원 행렬 이용해서 벽의 파괴 상태 파악

# 중간에 벽을 부수면 그 이후부터는 벽을 지나갈 수 없음 -> 벽이 아닌 곳들만 탐색하면 됨
# 중간에 벽을 부수지 않은 상황이면 그 이후 경로에서 벽 부수기 선택권 O

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
            if arr[ni][nj] == 1 and hit == 0:   # 이동할 곳이 벽이고, 부수기 기회 사용 안한 경우
                visited[ni][nj][1] = visited[i][j][0] + 1
                q.append((ni, nj, 1))
            elif arr[ni][nj] == 0 and visited[ni][nj][hit] == 0:    # 이동할 곳이 벽이아니고, 한번도 방문한적 없는 경우
                visited[ni][nj][hit] = visited[i][j][hit] + 1
                q.append((ni, nj, hit))

    return -1


N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]   # visited[x][y][0]은 벽 파괴 가능, [x][y][1]은 불가능
visited[0][0][0] = 1

print(bfs(0,0,0))



