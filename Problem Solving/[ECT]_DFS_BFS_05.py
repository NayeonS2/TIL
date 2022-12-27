# 경쟁적 전염
# 1초당 상하좌우 1칸씩 S초동안 바이러스 타입별로 !동시에! 전염 (bfs!)
# 숫자가 작은 것이 더 전염시 우위선점 -> heapq 사용
# S초후 (X-1,Y-1) 위치의 바이러스 종류 구하기

import sys,heapq
sys.stdin = open('input.txt')

input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

S, X, Y = map(int, input().split())

def bfs():
    q = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                num = arr[i][j]
                heapq.heappush(q, (num, (i, j)))
    # S초동안
    for _ in range(S):
        virus = []

        while q:
            num, (i, j) = heapq.heappop(q)

            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    arr[ni][nj] = num
                    # virus 배열에 넣어뒀다가
                    virus.append((num, (ni, nj)))
        # 1초가 지나는 시점에 한꺼번에 heappush!
        for vir in virus:
            heapq.heappush(q, vir)

bfs()

print(arr[X - 1][Y - 1])
