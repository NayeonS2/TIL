# 특정 거리의 도시 찾기
# 최단 거리 테이블 생성해서 풀기!!!

import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
from collections import deque

def bfs(start):
    global distance

    distance[start] = 0

    q = deque()
    q.append(start)

    while q:
        now = q.popleft()

        for next in adjList[now]:
            if distance[next] == -1:
                distance[next] = distance[now] + 1
                q.append(next)

N, M, K, X = map(int,input().split())

adjList = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    adjList[a].append(b)


distance = [-1] * (N+1)     # 최단거리 테이블 생성 !!!!!!!

bfs(X)

flag = 0
for l in range(1,N+1):
    if distance[l] == K:
        flag = 1
        print(l)
if flag == 0:
    print(-1)







