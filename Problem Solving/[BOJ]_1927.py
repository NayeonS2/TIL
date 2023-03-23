# 최소 힙

import sys,heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N):
    x = int(input())

    if x == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q,x)


