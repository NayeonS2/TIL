import sys
sys.stdin = open('input.txt')

N = int(input())

a, b = map(int, input().split())

E = int(input())

adjList = [[] for _ in range(N + 1)]

for _ in range(E):
    p, c = map(int, input().split())

    adjList[p].append(c)
    adjList[c].append(p)


def dfs(v, cnt):
    flag = 0

    visited = [0] * (N + 1)

    stack = [(v, cnt)]
    visited[v] = 1

    while stack:

        now, cnt = stack.pop()

        if now == b:
            flag = 1
            return cnt

        for next in adjList[now]:
            if visited[next] == 0:
                stack.append((next, cnt + 1))
                visited[next] = 1

    if flag == 0:
        return -1


print(dfs(a, 0))