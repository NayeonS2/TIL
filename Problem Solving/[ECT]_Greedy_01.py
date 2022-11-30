# 큰 수의 법칙

import sys
sys.stdin = open('input.txt')

N,M,K = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort(reverse=True)

m=0
k=0
num = 0
while True:
    if m == M:
        break
    elif m < M:
        if k == K:
            k = 0
            m += 1
            num += nums[1]
        elif k < K:
            m += 1
            k += 1
            num += nums[0]

print(num)


