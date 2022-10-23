# 퇴사

import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
T = []
P = []

for _ in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

d = [0] * (N+1)
max_prof = 0

for i in range(N-1,-1,-1):                      # 마지막 일부터 거꾸로 돌면서 확인
    after = i + T[i]
    if after <= N:
        d[i] = max(P[i] + d[after], max_prof)   # i일부터 마지막날까지 얻을 수 있는 최대 수익
        max_prof = d[i]
    else:
        d[i] = max_prof

print(max_prof)