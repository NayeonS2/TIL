# 볼링공 고르기

import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())

nums = list(map(int,input().split()))

dic = dict()
for i in range(1,len(nums)+1):
    dic[str(i)] = nums[i-1]

cnt = 0
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if dic[str(i)] != dic[str(j)]:
            cnt += 1
print(cnt)

