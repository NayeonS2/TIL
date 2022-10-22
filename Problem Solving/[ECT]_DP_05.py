# 금광
# 오른쪽위, 오른쪽, 오른쪽아래로만 이동가능할때 채굴가능한 금의 최대 크기
# 1열은 주어짐

import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

def poss(i,j):
    pos = []
    for di,dj in [[-1,-1],[0,-1],[1,-1]]:
        ni,nj = i+di, j+dj
        if 0<=ni<n and 0<=nj<m:
            pos.append((d[ni][nj]))
    return max(pos)

T = int(input())
for _ in range(T):
    n,m = map(int,input().split())

    info = list(map(int,input().split()))
    gold = []
    for i in range(0,n*m,m):
        gold.append(info[i:i+m])

    d = [[0]*m for _ in range(n)]

    for i in range(n):
        d[i][0] = gold[i][0]


    for j in range(1,m):
        for i in range(n):
            d[i][j] = gold[i][j] + poss(i,j)

    ans = 0
    for i in range(n):
        ans = max(ans,d[i][m-1])

    print(ans)






