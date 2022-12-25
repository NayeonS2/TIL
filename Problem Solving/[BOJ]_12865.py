# 평범한 배낭

# N개의 물건
# 각 물건은 무게 W와 가치 V
# 최대 K만큼의 무게 만을 넣을 수 있는 배낭
# 배낭에 넣을 수 있는 물건들의 가치의 최댓값

# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

import sys
sys.stdin = open('input.txt')

weight = []
value = []

N,K = map(int,input().split())

D = [[0]*(K+1) for _ in range(N+1)]

for _ in range(N):
    W,V = map(int,input().split())
    weight.append(W)
    value.append(V)

for i in range(1,N+1):
    for w in range(1,K+1):
        if weight[i-1] <= w:
            D[i][w] = max(D[i-1][w], value[i-1]+D[i-1][w-weight[i-1]])
        else:
            D[i][w] = D[i-1][w]

print(D[N][K])