import sys
import math
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    find = 0
    if math.isclose(N ** (1 / 3), round(N ** (1 / 3))):
        print(f'#{tc} {round(N ** (1 / 3))}')
        find += 1

    if find == 0:
        print(f'#{tc} -1')
