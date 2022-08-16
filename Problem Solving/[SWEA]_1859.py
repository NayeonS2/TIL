import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    N = int(input())
    price = list(map(int, input().split()))

    length = len(price)

    margin = 0

    max_price = price[-1]
    for i in range(length-2,-1,-1):
        if price[i] > max_price:
            max_price = price[i]
        else:
            margin += max_price - price[i]
    print(f'#{tc} {margin}')









