import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    ab_lst = []
    for i in range(N):
        A, B = map(int, input().split())
        ab_lst.append([A, B])

    P = int(input())

    blk = [0] * P


    C_lst = []
    for j in range(P):
        C = int(input())
        C_lst.append(C)

    for idx, val in enumerate(C_lst):
        for ab in ab_lst:
            if val in range(ab[0],ab[1]+1):
                blk[idx] += 1

    ans = ''
    for x in blk:
        ans = ans + str(x) + ' '
    print(f'#{tc} {ans}')