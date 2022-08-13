import sys

sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())
    cnt = 0
    for _ in range(1, N + 1):

        s_i, s_j, e_i, e_j, color = map(int, input().split())

        if color == 1:
            color = 'r'
        elif color == 2:
            color = 'b'

        for i in range(s_i, e_i + 1):
            for j in range(s_j, e_j + 1):
                if color == 'r':
                    if arr[i][j] == 0:
                        arr[i][j] = 'r'
                    elif arr[i][j] == 'b':

                        arr[i][j] = 'v'
                        cnt += 1


                elif color == 'b':
                    if arr[i][j] == 0:
                        arr[i][j] = 'b'
                    elif arr[i][j] == 'r':

                        arr[i][j] = 'v'
                        cnt += 1

    print(f'#{tc} {cnt}')