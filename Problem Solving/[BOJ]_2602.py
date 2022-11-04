# 바이러스

import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

V = int(input())
E = int(input())
adjList = [[] for _ in range(V+1)]

for _ in range(E):
    a,b = map(int,input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * (V+1)

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    cnt = 0
    while q:
        now = q.popleft()

        for nxt in adjList[now]:
            if visited[nxt] == 0:
                cnt += 1
                q.append(nxt)
                visited[nxt] = 1
    return cnt

print(bfs(1))