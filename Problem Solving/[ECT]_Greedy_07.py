# 만들 수 없는 금액

import sys
from itertools import combinations
sys.stdin = open('input.txt')

N = int(input())
units = list(map(int,input().split()))

all_ = []
for i in range(1,N+1):  # 1개~N개 고르는 모든 경우의수의 조합
    all_ += list(combinations(units,i))

sums = []
for pos in all_:
    sums.append(sum(pos))   # 각 경우의 합 리스트 -> 만들 수 있는 숫자 리스트
sums.sort()
i = 1
while True:
    if i not in sums:   # 1부터 시작해서 만들수있는 숫자 리스트에 없는 수가 나오면 print하고 break
        print(i)
        break
    i += 1
