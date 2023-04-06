# 스타트 링크

import sys
sys.stdin = open('input.txt')

from collections import deque

F, S, G, U, D = map(int, input().split())


def bfs(n):
    flag = 0

    visited = [0] * (F + 1)

    q = deque([(n, 0)])

    while q:
        now, cnt = q.popleft()

        if now == G:
            flag = 1
            return cnt

        for next in [now + U, now - D]:
            if 1 <= next <= F:
                tmp = next
            else:
                tmp = now

            if visited[tmp] == 0:
                q.append((tmp, cnt + 1))
                visited[tmp] = 1

    if flag == 0:
        return "use the stairs"


print(bfs(S))