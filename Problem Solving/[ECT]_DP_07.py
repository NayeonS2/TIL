# 퇴사
# 상담을 완료하는데 걸리는 기간 T와 상담을 했을 때 받을 수 있는 금액 P
# 상담을 적절히 했을 때, 얻을 수 있는 최대 수익

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
T = []  # 소요시간
P = []  # 수익

for _ in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

d = [0] * (N+1)


for i in range(N-1,-1,-1):                    # 마지막 일부터 거꾸로 돌면서 확인
    after = i + T[i]
    if after <= N:                            # 상담완료 일자가 퇴사일을 넘기지 않으면
        d[i] = max(P[i] + d[after], d[i+1])   # i일에 상담을 하는 것과 안하는 것중에 더 큰 이익 선택

    else:
        d[i] = d[i+1]                         # 퇴사일을 넘기면 그냥 이때까지의 최대값인 d[i+1] 넣어줌

print(d[0])