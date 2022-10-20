# 효율적인 화폐 구성
# N개의 화폐를 이용해 M원을 만드는 최소한의 화폐 개수
# 불가능할땐 -1 출력
# 1<=N<=100, 1<=M<=10000

# DP 테이블은 금액 i를 만들 수 있는 최소한의 화폐 개수
# 주어진 화폐의 단위를 k라고 할때,
# DP(i-k)를 만드는 방법이 존재할 경우: DP(i) = min(DP(i), DP(i-k) + 1)
# DP(i-k)를 만드는 방법이 존재하지 않을 경우 : DP(i) = 10001

import sys
sys.stdin = open('input.txt')

N, M = map(int,input().split())

coin = []

for _ in range(N):
    coin.append(int(input()))

d = [10001] * (M+1)

for i in range(N):
    for j in range(coin[i], M+1):
        if d[j - coin[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - coin[i]] + 1)

if d[M] == 10001:   # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[M])


