# 정수 삼각형
# 아래층으로 내려오며 합이 최대가 되게 정수 선택
# 대각선 왼,오른쪽만 선택 가능

import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

def poss(i,j):
    pos = []
    if j == 0:
        for di,dj in [[-1,0]]:
            ni,nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n:
                pos.append(d[ni][nj])
    elif j == i:
        for di,dj in [[-1,-1]]:
            ni,nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n:
                pos.append(d[ni][nj])
    else:
        for di,dj in [[-1,0],[-1,-1]]:
            ni,nj = i+di, j+dj
            if 0<=ni<n and 0<=nj<n:
                pos.append(d[ni][nj])
    return max(pos)


n = int(input())

arr = [[0]*n for _ in range(n)]

for i in range(n):
    arr[i][:i+1] = list(map(int,input().split()))

d = [[0]*n for _ in range(n)]

d[0][0] = arr[0][0]

for i in range(1,n):
    for j in range(n):
        d[i][j] = arr[i][j] + poss(i,j)


print(max(d[n-1]))




