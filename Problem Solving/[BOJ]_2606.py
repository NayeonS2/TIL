# 바이러스

import sys
sys.stdin = open('input.txt')

N = int(input())

E = int(input())

adjList = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b = map(int, input().split())

    adjList[a].append(b)
    adjList[b].append(a)

cnt = 0
visited = [0] * (N + 1)


def dfs(v):
    global cnt

    stack = [v]
    visited[v] = 1

    while stack:
        now = stack.pop()

        for next in adjList[now]:
            if visited[next] == 0:
                stack.append(next)
                cnt += 1
                visited[next] = 1


dfs(1)
print(cnt)