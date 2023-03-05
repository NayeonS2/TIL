# 디저트 카페

import sys

sys.stdin = open('input.txt')

di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

def dfs(x, y, path, dir):
    global cnt,i,j

    if dir == 3 and x == i and y == j and len(path) > 2:
        cnt = max(cnt,len(path))

    if 0<=x<N and 0<=y<N and arr[x][y] not in path:
        new_path = path + [arr[x][y]]

        #직진
        nx,ny = x+di[dir] , y+dj[dir]
        dfs(nx,ny,new_path,dir)

        #꺾기
        if dir < 3:
            nx, ny = x + di[dir+1], y + dj[dir+1]
            dfs(nx,ny,new_path,dir+1)

T = int(input())

for tc in range(1, 1 + T):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = -1

    for i in range(N):
        for j in range(1, N):
            dfs(i,j,[],0)

    print(f'#{tc} {cnt}')
