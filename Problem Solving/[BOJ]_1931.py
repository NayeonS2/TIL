# 회의실 배정

import sys
sys.stdin = open('input.txt')

times = []
N = int(input())
for _ in range(N):
    s,e = map(int,input().split())
    times.append((s,e))
times.sort(key=lambda x:(x[1],x[0]))

cnt = 1
end = times[0][1]
for i in range(1,N):
    if times[i][0] >= end:
        cnt += 1
        end = times[i][1]
print(cnt)