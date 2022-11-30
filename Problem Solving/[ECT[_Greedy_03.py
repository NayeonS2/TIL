# 1이 될 때까지

import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(cnt,n):
    q = deque()
    q.append((cnt,n))
    visited.append(n)

    while q:
        cnt,n = q.popleft()
        if n == 1:
            return cnt
        else:
            if n%K == 0:
                for next in [n-1,n//K]:
                    if next not in visited:
                        q.append((cnt+1, next))
                        visited.append(next)
            else:
                for next in [n-1]:
                    if next not in visited:
                        q.append((cnt+1, next))
                        visited.append(next)


N,K = map(int,input().split())
visited = []

print(bfs(0,N))
