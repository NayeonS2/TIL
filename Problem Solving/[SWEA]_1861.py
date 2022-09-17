import sys

sys.stdin = open('input.txt')

T = int(input())


def bfs(i,j,N):

    rooms = []  # 방 번호를 담아줄 리스트
    rooms.append(arr[i][j])

    q = [(i,j)]

    visited[i][j] = 1


    while q:
        i,j = q.pop(0)

        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:   # 상하좌우 방향벡터
            ni, nj = i + di, j + dj
            # 좌표가 범위안에 있고, 방문한적이없고, 현재 위치 값과의 차이가 1일때
            if 0<=ni<N and 0<=nj<N and abs(arr[ni][nj]-arr[i][j]) ==  1 and visited[ni][nj] == 0:
                q.append((ni,nj))
                rooms.append(arr[ni][nj])
                visited[ni][nj] = 1
    return min(rooms), len(rooms)   # 방문한 방 번호의 최소값과 방문한 방의 개수 반환




for tc in range(1,1+T):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]


    max_n_of_rooms = 0
    start_room = 1001
    for i in range(N):
        for j in range(N):
            room_n , n_of_rooms = bfs(i,j,N)
            # 이동할 수 있는 방 개수가 최대이며, 그중에 가장 작은 방번호
            if n_of_rooms > max_n_of_rooms or n_of_rooms == max_n_of_rooms and start_room > room_n:
                max_n_of_rooms = n_of_rooms
                start_room = room_n

    print(f'#{tc} {start_room} {max_n_of_rooms}')