# 디저트 카페

import sys

sys.stdin = open('input.txt')

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

def dfs(i, j, dir_s, move, ate):
    global maxV
    for k in range(dir_s, dir_s + 2):
        if k == 4:
            continue
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] in ate:
                if visited[ni][nj] == 2:
                    if maxV < move:
                        maxV = move
                        return
                continue

            visited[ni][nj] = 1
            dfs(ni, nj, k, move + 1, ate + [arr[ni][nj]])
            visited[ni][nj] = 0

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    maxV = -1

    for i in range(N):
        for j in range(1, N):
            visited[i][j] = 2  # 도착지
            dfs(i, j, 0, 1, [arr[i][j]])
            visited[i][j] = 0

    print(f'#{tc} {maxV}')
