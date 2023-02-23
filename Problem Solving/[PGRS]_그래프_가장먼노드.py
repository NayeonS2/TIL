n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

from collections import deque
def solution(n, edge):
    answer = 0

    adjList = [[] for _ in range(n+1)]
    visited = [-1]*(n+1)

    for vert in vertex:
        adjList[vert[0]].append(vert[1])
        adjList[vert[1]].append(vert[0])


    def bfs(v):
        cnt = 0
        q = deque()
        q.append((v,cnt))

        while q:
            now,cnt = q.popleft()

            if visited[now] == -1:
                visited[now] = cnt
                cnt += 1
                for next in adjList[now]:
                    q.append((next,cnt))

    bfs(1)

    for n in visited:
        if n == max(visited):
            answer += 1

    return answer
print(solution(n,vertex))