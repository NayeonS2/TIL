# 기둥 2 / 보 3
n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
               [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

from copy import deepcopy

def check(n,arr):
    for i in range(n + 1):
        for j in range(n + 1):
            if arr[i][j] == 2:
                if i == n or arr[i][j - 1] == 3 or arr[i][j] == 3 or arr[i + 1][j] == 2:
                    continue
                else:
                    return False
            if arr[i][j] == 3:
                if arr[i + 1][j] == 2 or arr[i + 1][j + 1] == 2 or (arr[i][j - 1] == 3 and arr[i][j + 1] == 3):
                    continue
                else:
                    return False
    return True


arr = [[0] * (n + 1) for _ in range(n + 1)]

for info in build_frame:
    x, y, a, b = info
    i, j = n - y, x

    tmp = deepcopy(arr)
    if a == 0:
        if b == 0:
            tmp[i][j] = 0
            if check(n,tmp):
                arr = tmp
            else:
                tmp[i][j] = arr[i][j]
        if b == 1:
            if i == n or arr[i][j - 1] == 3 or arr[i][j] == 3 or arr[i + 1][j] == 2:
                arr[i][j] = 2

    if a == 1:
        if b == 0:
            tmp[i][j] = 0
            if check(n,tmp):
                arr = tmp
            else:
                tmp[i][j] = arr[i][j]
        if b == 1:
            if arr[i + 1][j] == 2 or arr[i + 1][j + 1] == 2 or (arr[i][j - 1] == 3 and arr[i][j + 1] == 3):
                arr[i][j] = 3

answer = []
for i in range(n + 1):
    for j in range(n + 1):
        if arr[i][j] == 2:
            answer.append([j, n - i, 0])
        if arr[i][j] == 3:
            answer.append([j, n - i, 1])

answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))

print(answer)



