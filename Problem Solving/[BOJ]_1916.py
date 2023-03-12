# 최소비용구하기

import sys, heapq
sys.stdin = open('input.txt')

N = int(input())
M = int(input())

def dijkstra(s):

    q = []
    heapq.heappush(q,(0,s))
    distance[s] = 0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next_dist, next in adjList[now]:

            cost = dist + next_dist

            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q,(cost,next))


INF = int(1e9)
adjList = [[] for _ in range(N+1)]

distance = [INF]*(N+1)

for _ in range(M):
    s,e,c = map(int,input().split())
    adjList[s].append((c,e))

start,end = map(int,input().split())

dijkstra(start)

print(distance[end])


