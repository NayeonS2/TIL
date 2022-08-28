import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    N,M = map(int,input().split())

    arr = [list(input()) for _ in range(N)]
    rev_arr = list(zip(*arr))
    for i in range(N):
        for j in range(N-M+1):
            if arr[i][j:j+M] == arr[i][j:j+M][::-1]:
                ans = ''.join(arr[i][j:j+M])
                print(f'#{tc} {ans}')

    for i in range(N):
        for j in range(N-M+1):
            if rev_arr[i][j:j+M] == rev_arr[i][j:j+M][::-1]:
                ans = ''.join(rev_arr[i][j:j+M])
                print(f'#{tc} {ans}')