import sys
sys.stdin = open('input.txt')
from collections import deque

def find():
    idx = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                idx.append((arr[i][j],i,j,0))
    return sorted(idx)

def bfs():
    q = deque(find())

    while q:
        type, i, j, cnt = q.popleft()

        if cnt == S:
            return
        else:
            for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
                ni,nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = type
                        q.append((type,ni,nj,cnt+1))


N,K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

S,X,Y = map(int,input().split())

bfs()

print(arr[X-1][Y-1])

