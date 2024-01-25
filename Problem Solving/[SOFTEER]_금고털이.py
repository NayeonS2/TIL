# 루팡은 배낭을 하나 메고 은행금고에 들어왔다. 금고 안에는 값비싼 금, 은, 백금 등의 귀금속 덩어리가 잔뜩 들어있다.
# 배낭은 W ㎏까지 담을 수 있다.
# 각 금속의 무게와 무게당 가격이 주어졌을 때 배낭을 채울 수 있는 가장 값비싼 가격은 얼마인가?
# 루팡은 전동톱을 가지고 있으며 귀금속은 톱으로 자르면 잘려진 부분의 무게만큼 가치를 가진다.

# 1 ≤ N ≤ 106인 정수
# 1 ≤ W ≤ 104인 정수
# 1 ≤ Mi, Pi ≤ 104인 정수

# 첫 번째 줄에 배낭의 무게 W와 귀금속의 종류 N이 주어진다.
# i + 1 (1 ≤ i ≤ N)번째 줄에는 i번째 금속의 무게 Mi와 무게당 가격 Pi가 주어진다.

# 첫 번째 줄에 배낭에 담을 수 있는 가장 비싼 가격을 출력하라.



import sys
import heapq
input = sys.stdin.readline

W,N = map(int,input().split())

q = []

for _ in range(N):
    M,P = map(int,input().split())
    heapq.heappush(q,(-P,M))

value = 0
poss_weight = W
while q:

    if poss_weight == 0:
        break

    now = heapq.heappop(q)
    now_p, now_m = -now[0],now[1]

    if poss_weight >= now_m:
        value += now_p*now_m
        poss_weight -= now_m
    else:
        value += poss_weight*now_p
        poss_weight = 0

print(value)





