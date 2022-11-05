# 숨바꼭질 3
# 걷기는 1초 / 순간이동은 0초
# 큐에서 순간이동이 우선순위를 가져야함!!!

import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def bfs(s,e):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        s = q.popleft()

        if s == e:
            return visited[s]-1

        else:
            for pos in [s-1,s+1,s*2]:
                if 0<=pos<100001 and visited[pos] == 0:
                    if pos == s*2:
                        q.appendleft(pos)
                        visited[pos] = visited[s]
                    else:
                        q.append(pos)
                        visited[pos] = visited[s] + 1


N,K = map(int,input().split())

visited = [0] * 100001

print(bfs(N,K))
