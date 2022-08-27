import sys
sys.stdin = open('input.txt')

def oselo(i,j,col):                                                                 # 게임 진행 함수 따로 생성
    color = [1,2]                                                                   # color = 본인 돌 / counter = 상대방 돌
    if col == color[0]:
        counter = color[1]
    else:
        counter = color[0]


    if board[i][j] == 0:                                                            # 돌을 둘 자리가 비어있으면 자기 돌을 둠
        board[i][j] = col

    for dr,dc in d:                                                                 # dr,dc는 8방향에서의 i, j
        way = []

        if 0<=i+dr<N and 0<=j+dc<N:                                                 # 각 방향으로 나아갔을때 위치가 구간안에 있을때
            nr = i + dr
            nc = j + dc

            while board[nr][nc] == counter and 0<=nr<N and 0<=nc<N:                 # 해당 방향에 상대방 돌이 있으면서, 구간안에 위치할동안
                way.append((nr,nc))                                                 # 전진하는 경로를 리스트에 담아두면서 이동
                nr += dr
                nc += dc

                if nr < 0 or nr >= N or nc < 0 or nc >= N or board[nr][nc] == 0:    # 해당 위치가 구간에서 벗어나거나, 0을 만났을때 경로 리스트 초기화시키고 break
                    way = []
                    break
        for x in way:
            board[x[0]][x[1]] = col                                                 # 경로 리스트에 담긴 board 위치들을 자신의 돌 색으로 바꿔줌



T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split())

    board = [[0]*N for _ in range(N)]



    board[N//2-1][N//2-1] = 2                   # 기본 시작 배치
    board[N // 2-1][N // 2 ] = 1
    board[N // 2 ][N // 2-1] = 1
    board[N // 2][N // 2] = 2




    dr_lst = [-1,1,0,0,-1,-1,1,1]               # 상하좌우 좌대각 우대각
    dc_lst = [0,0,-1,1,1,-1,1,-1]
    d = list(zip(dr_lst,dc_lst))

    turns = []
    for _ in range(M):
        x,y,col = map(int,input().split())
        turns.append((x,y,col))

    while True:
        if turns:                               # 턴을 돌면서 돌을 둘 포지션 리스트를 앞에서부터 팝시켜서 i,j,color 설정
            temp = turns.pop(0)
            i = temp[1]  -1
            j = temp[0] - 1
            col = temp[2]
        else:
            break


        oselo(i,j,col)
    #print(board)   # [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
    b_cnt = 0
    w_cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                b_cnt += 1
            elif board[i][j] == 2:
                w_cnt += 1



    print(f'#{tc} {b_cnt} {w_cnt}')

