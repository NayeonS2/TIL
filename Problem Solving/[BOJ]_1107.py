# 리모컨

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
M = int(input())

if M == 0:
    channel = [x for x in range(0,10)]
else:
    broken = list(map(int,input().split()))

    channel = []

    for x in range(0,10):
        if x not in broken:
            channel.append(x)

min_cnt = abs(N-100)

for i in range(0,1000001):
    now = str(i)
    for j in range(len(now)):
        if int(now[j]) not in channel:
            break
        elif j == len(now)-1:
            min_cnt = min(min_cnt, abs(i-N)+len(now))

print(min_cnt)