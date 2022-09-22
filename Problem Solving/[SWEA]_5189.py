import sys

sys.stdin = open('input.txt')

# 1 - ... - 1 가능한 경우의 수를 순열로 생성

def f(i,k):
    global result

    if i == k:
        temp = p[:]
        result.append(temp)
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = a[j]
                f(i+1, k)
                used[j] = 0



T = int(input())

for tc in range(1,1+T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    result = []

    a = [i for i in range(2, N + 1)]
    used = [0] * (N-1)
    p = [0] * (N-1)
    f(0, N-1)

    min_v = 100 * N * N

    for res in result:
        tmp = [1] + res + [1]

        route_sum = 0

        for j in range(0, len(tmp) - 1):
            route_sum += arr[tmp[j] - 1][tmp[j + 1] - 1]
        if route_sum < min_v:
            min_v = route_sum
        else:
            continue
    print(f'#{tc} {min_v}')