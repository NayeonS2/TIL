import sys
sys.stdin = open('input.txt')

def bfs(start,N,goal):
    visited = [0] * N
    q = []
    q.append(start)

    visited[start] = 1

    while q:
        start = q.pop(0)
        if start == goal:
            return visited[start] - 1
        for next in adj_List[start]:
            if visited[next] == 0:
                q.append(next)
                visited[next] = visited[start] + 1
    return 0




T = int(input())

for tc in range(1,1+T):
    V, E = map(int,input().split())

    N = V + 1

    adj_List = [[] for _ in range(N)]

    for _ in range(E):
        A, B = map(int,input().split())
        adj_List[A].append(B)
        adj_List[B].append(A)


    S, G = map(int,input().split())


    print(f'#{tc} {bfs(S,N,G)}')