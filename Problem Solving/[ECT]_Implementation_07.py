# 뱀

# 사과를 먹으면 뱀 길이 늘어남
# 벽 또는 자신의 몸과 부딪히면 게임 끝
# NxN 정사각 보드, 몇몇칸엔 사과, 보드 상하좌우 끝에 벽
# 게임 시작 시 뱀은 맨위 맨좌측 위치, 뱀 길이는 1, 처음에 오른쪽을 향함

# 뱀은 몸길이를 늘려 머리를 다음칸에 위치
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
# 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워줌, 즉 몸길이는 변하지 않음

# 사과 위치와 뱀 이동경로가 주어질 때, 이 게임이 몇 초에 끝나는지 계산

import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
K = int(input())

arr = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(K):
    i, j = map(int, input().split())
    arr[i][j] = 1

L = int(input())

turns = []
for _ in range(L):
    X, C = input().split()
    turns.append((int(X), C))

t = 0               # 시간
h_i, h_j = 1, 1     # 뱀머리위치
arr[h_i][h_j] = 2   # 뱀있는곳 표시

snake = deque()     # 꼬리위치 찾기위해 queue 사용
snake.append((h_i, h_j))
d = 0               # 상하좌우 방향 인덱스
turn_idx = 0        # 방향 전환 정보 인덱스

direc = [[0, 1], [1, 0], [0, -1], [-1, 0]]      # 우 하 좌 상
while True:

    ni, nj = h_i + direc[d][0], h_j + direc[d][1]

    if 1>ni or ni>N or 1>nj or nj>N or arr[ni][nj] == 2: # 벽 또는 몸과 부딪히면 게임끝
        t += 1
        break
    else:
        if arr[ni][nj] == 1:    # 사과있으면 몸길이 그대로
            arr[ni][nj] = 2
            snake.append((ni, nj))

        else:
            arr[ni][nj] = 2     # 사과 없으면
            snake.append((ni, nj))
            t_i, t_j = snake.popleft()  # 꼬리위치 칸 비워줌
            arr[t_i][t_j] = 0
        t += 1

    h_i, h_j = ni, nj   # 머리위치 이동

    if turn_idx < len(turns):   # 방향전환 정보 확인
        time, direction = turns[turn_idx]
        if t==time: # 전환 시간이 되면 전환
            if direction == "D":    # 시계방향
                d = (d + 1) % 4
            elif direction == "L":  # 반시계방향
                d = (d - 1) % 4
                if d<0:
                    d +=4
            turn_idx += 1

print(t)
