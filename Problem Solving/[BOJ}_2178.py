import sys
sys.stdin = open('input.txt')
from collections import deque

N, M = map(int,input().split())

maze = [list(map(int,input())) for _ in range(N)]

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(x,y):

    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nr = x + dr[i]
            nc = y + dc[i]

            if nr>=N or nr<0 or nc>=M or nc<0 or maze[nr][nc] == 0:
                continue

            if maze[nr][nc] == 1:
                maze[nr][nc] = maze[x][y] + 1
                q.append((nr,nc))
    return maze[N-1][M-1]

print(bfs(0,0))
