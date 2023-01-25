# 트리의 지름
# 트리에서 루트노드에서 가장 먼 노드를 dfs로 구한다.
# 2번에서 구한 가장 먼 노드에서 한번 더 가장 먼 노드를 dfs로 구한다.
# 3번에서 구한 가장 먼 길이가 정답이 된다.

import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**5)

N = int(input())
E = N-1

parent = [0]*(N+1)

adjList = [[] for _ in range(N+1)]
distance = [-1]*(N+1)
distance[1] = 0
def dfs(node, cost):

    for next in adjList[node]:
        c,next_n = next
        if distance[next_n] == -1:
            distance[next_n] = cost + c
            dfs(next_n,cost+c)


for _ in range(E):
    a,b,c = map(int,input().split())

    adjList[a].append((c,b))
    adjList[b].append((c, a))


dfs(1,0)

first_furthest = distance.index(max(distance))
distance = [-1]*(N+1)
distance[first_furthest] = 0

dfs(first_furthest,0)

print(max(distance))



