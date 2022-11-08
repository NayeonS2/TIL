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

N = int(input())
K = int(input())

arr = [[0]*N for _ in range(N)]

for _ in range(K):
    i,j = map(int,input().split())
    arr[i-1][j-1] = 1

L = int(input())

turns = deque()
for _ in range(L):
    X, C = input().split()
    turns.append((int(X),C))

t = 0
h_i,h_j = 0,0
t_i,t_j = 0,0
di,dj = 0,1
while True:
    t += 1
    while turns:
        time, direction = turns.popleft()
        if t == time:
            if direction == "D":
                di,dj = dj

    if arr[h_i+di][h_j+dj] == 1:
        h_i += di
        h_j += dj
    else:
        h_i += di
        h_j += dj
        t_i += di
        t_j += dj






