# 벽돌 깨기
# 구슬은 n번만 쏠 수 있고, 벽돌들은 w * h 배열
# 구슬은 항상 맨 위에 있는 벽돌만, 명중한 벽돌은 상하좌우로 벽돌숫자-1 칸만큼 제거
# 제거되는 범위 내에 있는 벽돌은 동시에 제거
# 빈 공간 있는 경우 벽돌은 아래로 떨어짐
# 최대한 많은 벽돌 제거하려할때 남은 벽돌 수 구하기
# 중복순열 itertools product 이용

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
        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni = i + n*di
            nj = j + n*dj

            if 0<=ni<H and 0<=nj<W and new_block[ni][nj] != 0:
                bomb(ni,nj)

def down_block(new_block):
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
    shoots = list(itertools.product([w for w in range(W)], repeat=N))

    min_res = 987654321

    for shoot in shoots:
        new_block = copy.deepcopy(block)

        for sht in shoot:
            game(sht)
            new_block = down_block(new_block)
        res = 0
        for i in range(H):
            for j in range(W):
                if new_block[i][j] != 0:
                    res += 1
        min_res = min(min_res,res)

        if min_res == 0:
            break
    print(f'#{tc} {min_res}')
