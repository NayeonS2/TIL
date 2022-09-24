# N - Queen

import sys
sys.stdin = open('input.txt')

def dfs(i):
    global cnt

    if i == N:
        cnt += 1
        return
    else:
        for j in range(N):
            if j in col or i + j in r_diag or i - j in l_diag:
                continue

            col.add(j)
            r_diag.add(i + j)
            l_diag.add(i - j)

            dfs(i + 1)

            col.remove(j)
            r_diag.remove(i + j)
            l_diag.remove(i - j)


T = int(input())

for tc in range(1, 1 + T):
    N = int(input())

    col = set()
    l_diag = set()
    r_diag = set()

    cnt = 0

    dfs(0)

    print(f'#{tc} {cnt}')
