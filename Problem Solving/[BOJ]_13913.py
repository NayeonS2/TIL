# 숨바꼭질 4
# route를 인자로 넘기면 시간초과!
# 어디서 왔었어! 식으로 배열에 기록

import sys
from collections import deque

input = sys.stdin.readline

def bfs(s, e):
    global cnt, route

    q = deque()
    q.append(s)

    visited[s] = 1

    while q:
        s = q.popleft()

        if s == e:
            print(visited[s]-1)
            final = []
            tmp = s
            for _ in range(visited[s]):
                final.append(tmp)
                tmp = route[tmp]
            final = final[::-1]
            print(' '.join(map(str,final)))

        else:
            for pos in [s - 1, s + 1, 2 * s]:
                if 0 <= pos <= 100000 and visited[pos] == -1:
                    q.append(pos)
                    visited[pos] = visited[s] + 1
                    route[pos] = s


N, K = map(int, input().split())
visited = [-1] * 100001
route = [-1] * 100001

bfs(N, K)

