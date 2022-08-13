import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, Q = map(int, input().split())
    lst = [0]*N
    for i in range(1,Q+1):
        L, R = map(int, input().split())
        for j in range(L-1,R):
            lst[j] = i
    ans = ''
    for x in lst:
        ans = ans + str(x) + ' '
    print(f'#{tc} {ans}')