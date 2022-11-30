# 숫자 카드 게임

import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    arr[i] = sorted(arr[i], reverse=True)

last = []
for i in range(N):
    last.append((i,arr[i][M-1]))
last.sort(key=lambda x:x[1])
print(last[len(last)-1][1])
