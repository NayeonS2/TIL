# 최종순위
# 위상정렬
# 정해진 우선순위에 맞게 전체 팀들의 순서를 나열해야함
# 자기보다 낮은 등수 팀을 가리키도록 방향그래프
# 위상정렬 수행 시, 큐에서 노드를 뽑을때 큐 원소가 항상 1개로 유지되는 경우에만 고유한 순위가 존재

# 진입차수가 0인 노드를 큐에 넣음
# 큐가 빌때까지 다음 과정 반복
#   큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거
#   새롭게 진입차수가 0이 된 노드를 큐에 넣음


from collections import deque
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1,T+1):
    n = int(input())

    indegree = [0]*(n+1)
    graph = [[0]*(n+1) for _ in range(n+1)]

    # 작년 순위
    last_rank = list(map(int,input().split()))

    for i in range(n):
        for j in range(i+1, n):
            graph[last_rank[i]][last_rank[j]] = 1
            indegree[last_rank[j]] += 1

    # 올해 변경 순위
    m = int(input())
    for i in range(m):
        a,b = map(int,input().split())
        if graph[a][b] == 1:
            # 간선방향뒤집기
            graph[a][b] = 0
            graph[b][a] = 1
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = 1
            graph[b][a] = 0
            indegree[a] -= 1
            indegree[b] += 1

def topology():
    result = []
    q = deque()

    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

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
