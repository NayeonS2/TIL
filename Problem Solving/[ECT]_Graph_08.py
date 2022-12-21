# 최종순위
# 위상정렬

# 진입차수가 0인 노드를 큐에 넣음
# 큐가 빌때까지 다음 과정 반복
#   큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#   새롭게 진입차수가 0이 된 노드를 큐에 넣음


from collections import deque
import sys
sys.stdin = open('input.txt')
T = int(input())
n = int(input())

v,e = map(int,input().split())

indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology():
    result = []
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i,end=" ")
topology()
