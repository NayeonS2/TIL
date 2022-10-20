import sys

sys.stdin = open('input.txt')


def dfs(i, j, type):
    global cnt

    if i < 0 or i >= N or j < 0 or j >= M:
        return False

    if visited[i][j] == 0 and arr[i][j] == type:
        visited[i][j] = 1
        cnt += 1

        dfs(i - 1, j, type)
        dfs(i + 1, j, type)
        dfs(i, j - 1, type)
        dfs(i, j + 1, type)
        return True
    return False


M, N = map(int, input().split())

arr = [list(input()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]

cnt = 0
res_w = 0
res_b = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j, 'W'):
            res_w += cnt ** 2
            cnt = 0
        elif dfs(i, j,'B'):
            res_b += cnt ** 2
            cnt = 0

print(res_w,res_b)


