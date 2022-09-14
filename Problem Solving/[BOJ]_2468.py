import sys
import copy
sys.stdin = open('input.txt')
sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if arr_[x][y] == 1:
        arr_[x][y] = 0

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)

        return True
    return False


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
arr_ = copy.deepcopy(arr)

max_cnt = 0
cnt = 0

for k in range(1, max(max(arr_)) + 1):
    for i in range(N):
        for j in range(N):
            if arr_[i][j] >= k:
                arr_[i][j] = 1
            else:
                arr_[i][j] = 0

    cnt = 0
    for i in range(N):
        for j in range(N):
            if dfs(i, j) == True:
                cnt += 1
    if max_cnt < cnt:
        max_cnt = cnt

    arr_ = copy.deepcopy(arr)

print(max_cnt)