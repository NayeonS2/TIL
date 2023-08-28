# 숫자카드 2

import sys
from collections import defaultdict

sys.stdin = open('input.txt')

N = int(input())
cards = list(map(int,input().split()))
M = int(input())
nums = list(map(int,input().split()))

dic = defaultdict(int)

for c in cards:
    dic[c] += 1

for n in nums:
    print(dic[n], end=" ")