# 숨바꼭질

import sys
sys.stdin = open('input.txt')

from collections import deque

N, K = map(int, input().split())

visited = [[] for _ in range(100001)]


def bfs(n, cnt):
    q = deque([(n, cnt)])

    while q:

        n, cnt = q.popleft()

        if n == K:
            return cnt

        for next in [n - 1, n + 1, n * 2]:
            if 0 <= next <= 100000 and next not in visited[n]:
                q.append((next, cnt + 1))
                visited[n].append(next)


print(bfs(N, 0))
