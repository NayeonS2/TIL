# 경쟁적 전염
# 1초당 상하좌우 1칸씩 S초동안 바이러스 타입별로 동시에 전염 (bfs!)
# 숫자가 작은 것이 더 전염시 우위선점
# S초후 (X-1,Y-1) 위치의 바이러스 종류 구하기

import sys
sys.stdin = open('input.txt')

from collections import deque

input = sys.stdin.readline

def find():
    idxs = []
    for i in range(N):
        for j in range(N):
            if tmp[i][j] != 0:
                idxs.append((tmp[i][j],i,j,0))
    return sorted(idxs)

def bfs():

    q = deque(find())   # 복수 시작점 리스트 넣은 채로 시작!

    while q:
        type, i, j ,cnt = q.popleft()

        if cnt == S:
            return
        else:
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    if tmp[ni][nj] == 0:
                        tmp[ni][nj] = type
                        q.append((type,ni,nj,cnt+1))


N,K = map(int,input().split())

tmp = [list(map(int,input().split())) for _ in range(N)]

S,X,Y = map(int,input().split())


bfs()

print(tmp[X-1][Y-1])