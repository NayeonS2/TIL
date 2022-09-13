import sys
sys.stdin = open('input.txt')

from collections import deque

def dfs(v,N):
    visited = [0]*N
    stack = []
    print(v, end=' ')
    visited[v] = 1

    while True:
        for w in adj_list[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w
                print(v,end=' ')
                visited[w] = 1
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break
def bfs(v, N):
    visited = [0]*N
    q = deque([v])


    visited[v] = 1

    while q:
        v = q.popleft()
        print(v,end=' ')
        for w in adj_list[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1



V, E, S = map(int,input().split())
N = V+1
adj_list = [[] for _ in range(N)]


for _ in range(E):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for edge in adj_list:
    edge.sort()



dfs(S,N)
print()
bfs(S,N)



