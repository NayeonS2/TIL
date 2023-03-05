# 프로세서 연결하기

import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def side_check(i,j):    # 상하좌우 체크
    dir = [0]*4     # 해당 방향으로 연결 가능하면 길이 표시
    for d in range(4):
        ni,nj = i,j
        tmp = 0
        while 0<ni<N-1 and 0<nj<N-1:
            tmp += 1
            ni += dx[d]
            nj += dy[d]
            if arr[ni][nj] == 1:    # 이미 코어나 선이 존재하면 break
                break
        else:
            dir[d] = tmp
    return dir

def con_discon(i,j,d):  # 선 연결 해제
    ni,nj = i,j

    while 0<ni<N-1 and 0<nj<N-1:
        ni += dx[d]
        nj += dy[d]

        if arr[ni][nj] == 1:
            arr[ni][nj] = 0
        elif arr[ni][nj] == 0:
            arr[ni][nj] = 1

def dfs(turn, min_length, now_cnt):
    global answer

    if now_cnt > answer[0]: # 연결된 코어 개수 최대로 갱신
        answer[0] = now_cnt
        answer[1] = min_length
    elif now_cnt == answer[0]:  # 개수가 같을경우엔 길이합이 작게
       if answer[1] > min_length:
            answer[1] = min_length

    if turn == core_cnt:    # 코어 다돌았으면 return
        return

    i,j = cores[turn][0], cores[turn][1]    # 첫번째 코어부터 돌면서 체크
    dir = side_check(i,j)   # 상하좌우 연결 가능 길이

    for d in range(4):
        if dir[d] == 0: # 연결 못하면 continue
            continue
        con_discon(i,j,d)  # 연결 -> 다음 코어 연결 -> 연결해제 (백트래킹)
        dfs(turn+1, min_length+dir[d], now_cnt+1)
        con_discon(i,j,d)
    dfs(turn+1, min_length, now_cnt) # 연결 건너뛰고 다음 코어로


for tc in range(1,T+1):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    cores = []  # 가장자리 제외 코어들
    core_cnt = 0    # 코어 총 개수

    for i in range(1,N-1):
        for j in range(1,N-1):
            if arr[i][j] == 1:
                cores.append((i,j))
                core_cnt += 1

    answer = [0,0]  # 연결 개수 / 총 연결길이
    dfs(0,0,0)
    print(f'#{tc} {answer[1]}')
