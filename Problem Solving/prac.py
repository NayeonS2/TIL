import sys
import itertools
import copy
sys.stdin = open('input.txt')

def game(j):
    for i in range(H):
        if new_block[i][j] != 0:
            bomb(i,j)
            break

def bomb(i,j):
    num = new_block[i][j]
    new_block[i][j] = 0
    for n in range(1,num):
        for di,dj in [[1,0],[-1,0],[0,-1],[0,1]]:
            ni = i+n*di
            nj = j+n*dj

            if 0<=ni<H and 0<=nj<W and new_block[ni][nj]!=0:
                bomb(ni,nj)

def down(new_block):
    down_block = [[0]*W for _ in range(H)]

    for w in range(W):
        s_h = H - 1
        for h in range(H-1,-1,-1):
            if new_block[h][w]:
                down_block[s_h][w] = new_block[h][w]
                s_h -= 1
    return down_block


T = int(input())
for tc in range(1,1+T):
    N,W,H = map(int,input().split())

    block = [list(map(int,input().split())) for _ in range(H)]

    shoots = list(itertools.product([w for w in range(W)],repeat=N))

    min_cnt = 987654321

    for shoot in shoots:
        new_block = copy.deepcopy(block)
        for sht in shoot:
            game(sht)
            new_block = down(new_block)

        cnt = 0
        for i in range(H):
            for j in range(W):
                if new_block[i][j] != 0:
                    cnt += 1

        min_cnt = min(cnt,min_cnt)

        if min_cnt == 0:
            break

    print(f'#{tc} {min_cnt}')


