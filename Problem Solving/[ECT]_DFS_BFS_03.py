# 특정 거리의 도시 찾기
# 최단 거리 테이블 생성해서 풀기!!!

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N,M,K,X = map(int,input().split())

adjList = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    adjList[a].append(b)

distance = [-1] * (N+1)

def bfs():
    q = deque()
    q.append(X)
    distance[X] = 0

    while q:
        now = q.popleft()
        for next in adjList[now]:
            if distance[next] == -1:
                distance[next] = distance[now] + 1
                q.append(next)

bfs()

flag = 0
for i in range(len(distance)):
    if distance[i] == K:
        print(i)
        flag = 1
if flag == 0:
    print(-1)




