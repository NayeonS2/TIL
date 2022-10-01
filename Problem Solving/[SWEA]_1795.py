# 인수의 생일파티
import sys
import heapq
sys.stdin = open('input.txt')
INF = int(1e9)

def dijkstra(start):

    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return distance


T = int(input())

for tc in range(1,1+T):
    N,M,X = map(int,input().split())

    graph = [[] for _ in range(N+1)]

    distance = [INF] * (N+1)

    for _ in range(M):
        x,y,c = map(int,input().split())
        graph[x].append((y,c))

    house = [x for x in range(1,N+1)]
    house.remove(X)

    go_time = []
    for h in house:
        go_time.append(dijkstra(h)[X])
        q = []
        distance = [INF] * (N + 1)


    back_time = []
    for h in house:
        back_time.append(dijkstra(X)[h])
        q = []
        distance = [INF] * (N + 1)


    max_time = 0
    for i in range(N-1):
        if max_time < go_time[i]+back_time[i]:
            max_time = go_time[i]+back_time[i]

    print(f'#{tc} {max_time}')