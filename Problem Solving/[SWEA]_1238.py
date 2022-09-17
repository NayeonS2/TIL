import sys
sys.stdin = open('input.txt')

def bfs(v,N):
    global result
    q = [v]

    while q:
        v = q.pop(0)
        result.append((v,visited[v]))   # 노드번호와 연락 순서 튜플로 리스트에 담음


        for w in adjlist[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = visited[v] + 1
    return result




T = 10
for tc in range(1,1+T):
    L, S = map(int,input().split())

    arr = list(map(int,input().split()))

    V = max(arr)    # 노드 최댓값
    N = V+1


    adjlist = [[] for _ in range(N)]    # 인접리스트
    visited = [0] * (N+1)   # 방문 기록

    result = []

    for i in range(0,len(arr)-1,2):
        a,b = arr[i:i+2][0], arr[i:i+2][1]  # 단방향으로
        adjlist[a].append(b)

    bfs(S, N)   # 시작 노드 넣어서 bfs 돌려줌


    max_h = 0
    for elem in result:
        if elem[1] > max_h:
            max_h = elem[1]

    max_node = 0    # 가장 늦게 연락받은 노드중에 가장 큰 노드번호 반환
    for elem in result:
        if elem[1] == max_h:
            if elem[0] > max_node:
                max_node = elem[0]

    print(f'#{tc} {max_node}')





