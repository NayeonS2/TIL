import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    sum_lst = []
    for i in range(N-M+1):
        for j in range(N-M+1):
            flies = 0
            for k in range(M):
                flies += sum(arr[i+k][j:j+M])
            sum_lst.append(flies)
    print(f'#{tc} {max(sum_lst)}')