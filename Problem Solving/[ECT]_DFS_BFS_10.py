# 블록 이동하기

# [(i,j),(i,j+1)] 상하좌우 -> [(i-1,j),(i-1,j+1)], [(i+1,j),(i+1,j+1)] ,[(i,j-1),(i,j)], [(i,j+1),(i,j+2)]
# 90도 시계, 반시계 -> [(i,j),(i+1,j)], [(i+1,j+1),(i,j+1)]

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

from collections import deque

def bfs(i,j,board):
    cnt = 0
    N = len(board)
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append([(i,j),(i,j+1)])
    visited[i][j] = 1
    visited[i][j+1] = 1
    while q:
        now = q.popleft()
        l,r = now[0],now[1]


        if l == (N-1,N-1) or r == (N-1,N-1):
            return cnt

        for dir in [[(l[0]-1,l[1]),(r[0]-1,r[1])], [(l[0]+1,l[1]),(r[0]+1,r[1])] ,[(l[0],l[1]-1),(r[0],r[1]-1)], [(l[0],l[1]+1),(r[0],r[1]+1)], [(l[0],l[1]),(r[0]+1,r[1]-1)], [(l[0]+1,l[1]+1),(r[0],r[1])]]:
                n_l,n_r = dir[0],dir[1]

                # 가로방향

                if [n_l,n_r] == [(l[0],l[1]),(r[0]+1,r[1]-1)]:

                    if 0 <= n_l[0] < N and 0 <= n_r[0] < N and 0 <= n_l[1] < N and 0 <= n_r[1] < N and 0 <= n_l[0]+1 < N and 0 <= n_l[1]+1 < N:
                        if board[n_l[0]][n_l[1]] != 1 and board[n_r[0]][n_r[1]] != 1 and board[n_l[0]+1][n_l[1]+1]!=1 and visited[n_l[0]][n_l[1]] != 1 and visited[n_r[0]][n_r[1]] != 1:
                            cnt += 1
                            q.append([n_l,n_r])


                if [n_l,n_r] == [(l[0]+1,l[1]+1),(r[0],r[1])]:
                    if 0 <= n_l[0] < N and 0 <= n_r[0] < N and 0 <= n_l[1] < N and 0 <= n_r[1] < N and  0 <= n_l[0]+1 < N:
                        if board[n_l[0]][n_l[1]] != 1 and board[n_r[0]][n_r[1]] != 1 and board[n_l[0]+1][n_l[1]]!=1 and visited[n_l[0]][n_l[1]] != 1 and visited[n_r[0]][n_r[1]] != 1:
                            cnt += 1
                            q.append([n_l,n_r])


                # 세로방향




                # 상하좌우
                if [n_l,n_r] == [(l[0]-1,l[1]),(r[0]-1,r[1])] or [(l[0]+1,l[1]),(r[0]+1,r[1])] or[(l[0],l[1]-1),(r[0],r[1]-1)] or [(l[0],l[1]+1),(r[0],r[1]+1)]:
                    if 0 <= n_l[0] < N and 0 <= n_r[0] < N and 0 <= n_l[1] < N and 0 <= n_r[1] < N:
                        if board[n_l[0]][n_l[1]] != 1 and board[n_r[0]][n_r[1]] != 1 and visited[n_l[0]][n_l[1]] != 1 and visited[n_r[0]][n_r[1]] != 1:
                            cnt += 1
                            q.append([n_l,n_r])



def solution(board):
    answer = bfs(0,0,board)
    return answer

print(solution(board))