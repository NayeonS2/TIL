import sys
sys.stdin = open('input.txt')

T = int(input())

def find_blk(arr, N, K):
    cnt = 0
    for i in range(N):
        for j in range(N - K + 1):
            if arr[i][j:j + K] == [1, 1, 1] or arr[i][j:j + K] == (1, 1, 1):
                s_j = j
                if s_j == 0:
                    if arr[i][j + K] != 1:
                        cnt += 1
                elif s_j == N - K:
                    if arr[i][j - 1] != 1:
                        cnt += 1
                else:
                    if arr[i][j + K] != 1 and arr[i][j - 1] != 1:
                        cnt += 1
    return cnt


for tc in range(1,1+T):
    N,K = map(int,input().split())

    arr = [list(map(int,input().split())) for _ in range(N)]

    rev_arr = list(zip(*arr))