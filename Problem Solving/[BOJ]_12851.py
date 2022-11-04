# 숨바꼭질 2

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

def bfs(s,e,time):
    global min_time, ways

    q = deque()
    q.append((s,time))

    while q:
        s, time = q.popleft()
        visited[s] = 1

        if s == e:
            min_time = min(time,min_time)
            ways += 1


        if time > min_time:
            return

        else:
            for pos in [s-1,s+1,s*2]:
                if 0<=pos<=100000 and visited[pos] == 0:
                    q.append((pos,time+1))


N,K = map(int,input().split())

visited = [0] * 100001

min_time = 987654321
ways = 0

bfs(N,K,0)
print(min_time)
print(ways)
