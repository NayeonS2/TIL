# 특정 거리의 도시 찾기
# 최단 거리 테이블 생성해서 풀기!!!

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

# 도시수, 도로수, 특정거리, 출발도시
N,M,K,X = map(int,input().split())

adjList = [[] for _ in range(N+1)]  # 단방향

for _ in range(M):
    a,b = map(int,input().split())
    adjList[a].append(b)

# 최단 거리 테이블
distance = [-1] * (N+1)

def bfs():
    q = deque()
    q.append(X)
    # 출발지까지의 거리는 0
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
# 해당 도시가 없으면 -1
if flag == 0:
    print(-1)




