import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    N = int(input())

    farm = [list(map(int,input())) for _ in range(N)]


    profit_t = 0
    i = 0
    j = N // 2
    while i < N//2:
        profit_t += sum(farm[i][j:j+2*i+1])
        i += 1
        j -= 1

    profit_b = 0
    i = N-1
    j = N // 2
    j_s = 0
    while i > N // 2:
        profit_b += sum(farm[i][j:j + 2 * j_s + 1])
        i -= 1
        j -= 1
        j_s += 1

    ans = profit_t + profit_b + sum(farm[N//2])
    print(f'#{tc} {ans}')
