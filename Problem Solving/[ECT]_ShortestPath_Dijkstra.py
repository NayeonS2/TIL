# 다익스트라
# 한 지점에서 다른 특정 지점까지의 최단 경로를 구해야하는 경우
# 단계마다 최단 거리를 가지는 노드를 하나씩 반복적으로 선택

import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

n,m = map(int,input().split())
start = int(input())

graph = [[] for _ in range(n+1)]

INF = int(1e9)
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for next in graph[now]:
            cost = dist + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost,next[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])

