# 블록 이동하기
# 가로
# [(i,j),(i,j+1)] 상하좌우 -> [(i-1,j),(i-1,j+1)], [(i+1,j),(i+1,j+1)] ,[(i,j-1),(i,j)], [(i,j+1),(i,j+2)]
# 90도 시계, 반시계 -> [(i,j),(i+1,j)], [(i+1,j+1),(i,j+1)]
# 세로

input = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]

from collections import deque


def next_pos(pos, board):
    (i1, j1), (i2, j2) = pos

    pos_list = []

    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        n_i1, n_j1, n_i2, n_j2 = i1 + di, j1 + dj, i2 + di, j2 + dj
        if board[n_i1][n_j1] == 0 and board[n_i2][n_j2] == 0:
            pos_list.append({(n_i1, n_j1), (n_i2, n_j2)})

    if i1 == i2:
        for d in [1, -1]:
            if board[i1 + d][j1] == 0 and board[i2 + d][j2] == 0:
                pos_list.append({(i1, j1), (i1 + d, j1)})
                pos_list.append({(i2, j2), (i2 + d, j2)})

    elif j1 == j2:
        for d in [1, -1]:
            if board[i1][j1 + d] == 0 and board[i2][j2 + d] == 0:
                pos_list.append({(i1, j1), (i1, j1 + d)})
                pos_list.append({(i2, j2), (i2, j2 + d)})

    return pos_list


def solution(board):
    n = len(board)

    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            new_board[i][j] = board[i - 1][j - 1]

    pos = {(1, 1), (1, 2)}

    visited = []
    q = deque()
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, time = q.popleft()

        if (n, n) in pos:
            return time

        for now in next_pos(pos, new_board):
            if now not in visited:
                visited.append(now)
                q.append((now, time + 1))



print(solution(input))
