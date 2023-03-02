import sys,heapq

sys.stdin = open('input.txt')

T = int(input())

def dijkstra(i,j):
    q = []
    heapq.heappush(q,(0,i,j))
    distance[0][0] = 0


    while q:
        dist,i,j = heapq.heappop(q)

        if distance[i][j] < dist:
            continue

        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:

            ni,nj = i+di, j+dj

            if 0<=ni<N and 0<=nj<N:

                tmp = max(0,arr[ni][nj]-arr[i][j])+1
                cost = dist+tmp
                if cost<distance[ni][nj]:
                    distance[ni][nj] = cost

                    heapq.heappush(q,(cost,ni,nj))



for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    INF = int(1e9)
    distance = [[INF]*(N) for _ in range(N)]

    dijkstra(0,0)

    print(f'#{tc} {distance[N-1][N-1]}')


