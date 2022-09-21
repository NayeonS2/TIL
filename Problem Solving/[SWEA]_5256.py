import sys
sys.stdin = open('input.txt')

# 이항계수 공식 : (nC0 , nC1 , nC2 , ..., nCn)
# ex) N = 3, (x+y)^3 = x^3 + 3x^2y + 3xy^2 + y^3  => 3C0 = 1, 3C1 = 3, 3C2 = 3, 3C3 = 1
# ex) N = 4, (x+y)^4 = x^4 + 4x^3y + 6x^2y^2 + 4xy^3 + y^4  => 4C0 = 1, 4C1 = 4, 4C2 = 6, 4C3 = 4, 4C4 = 1

def binom_coef(n,r):    # n개 중 r개를 뽑는 조합
    d = [[0] * (r+1) for _ in range(n+1)]   # (n+1) * (r+1) 2차원 배열

    for i in range(n+1):    # r이 0이거나 n과 같으면 1 저장 ( nC0 , nCn )
        d[i][0] = 1
    for i in range(r+1):
        d[i][i] = 1

    for i in range(1,n+1):
        for j in range(1,r+1):
            d[i][j] = d[i-1][j] + d[i-1][j-1]   # 4C2 = 3C1 + 3C2 , 3C2 = 2C1 + 2C2, ..

    return d[n][r]


T = int(input())

for tc in range(1,1+T):
    n, a, b = map(int, input().split())

    print(f'#{tc} {binom_coef(n,a)}')   # 어차피 n = a + b 이기때문에 nCa = nCb !