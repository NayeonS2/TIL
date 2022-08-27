import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())

    square = [list(input()) for _ in range(N)]


    draw_cnt = []
    for i in range(1,N-1):              # 모든 가능한 w, b, r 행의 수 조합을 먼저 구함
        for j in range(1, N-i):
            w = i
            b = j
            r = N-i-j

            idx = 0
            draw = 0

            while idx < w:              # 위에서 구한 각 색깔의 행 인덱스까지 돌면서 색을 칠해줘야하는 수를 카운팅
                draw += (M - square[idx].count('W'))
                idx += 1
            while idx < w + b:
                draw += (M - square[idx].count('B'))
                idx += 1
            while idx < N:
                draw += (M - square[idx].count('R'))
                idx += 1

            draw_cnt.append(draw)
    print(f'#{tc} {min(draw_cnt)}')     # 가장 작은 색칠 카운팅 출력