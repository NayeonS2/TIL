# dfs와 bfs

def dfs(v):
    visited = [0] * (N + 1)
    visited[v] = 1
    stack = []
    print(v,end=" ")
    while True:
        for w in adjList[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append(v)
                v = w
                print(v,end=" ")
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

def bfs(v):
    q = []
    q.append(v)
    visited = [0]*(N+1)
    visited[v] = 1

    while q:
        v = q.pop(0)
        print(v,end=" ")
        for w in adjList[v]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = visited[v] + 1


N,M,V = map(int,input().split())


adjList = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    adjList[a].append(b)
    adjList[b].append(a)

for lst in adjList:
    lst.sort()


dfs(V)
print()
bfs(V)


# import sys
# sys.stdin = open('input.txt')
#
# from collections import deque
#
# def dfs(v,N):
#     visited = [0]*N
#     stack = []
#     print(v, end=' ')
#     visited[v] = 1
#
#     while True:
#         for w in adj_list[v]:
#             if visited[w] == 0:
#                 stack.append(v)
#                 v = w
#                 print(v,end=' ')
#                 visited[w] = 1
#                 break
#         else:
#             if stack:
#                 v = stack.pop()
#             else:
#                 break
# def bfs(v, N):
#     visited = [0]*N
#     q = deque([v])
#
#
#     visited[v] = 1
#
#     while q:
#         v = q.popleft()
#         print(v,end=' ')
#         for w in adj_list[v]:
#             if not visited[w]:
#                 q.append(w)
#                 visited[w] = visited[v] + 1
#
#
#
# V, E, S = map(int,input().split())
# N = V+1
# adj_list = [[] for _ in range(N)]
#
#
# for _ in range(E):
#     a,b = map(int,input().split())
#     adj_list[a].append(b)
#     adj_list[b].append(a)
#
# for edge in adj_list:
#     edge.sort()
#
#
#
# dfs(S,N)
# print()
# bfs(S,N)



