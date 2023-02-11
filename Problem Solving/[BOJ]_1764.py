# 듣보잡

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dic = dict()

N,M = map(int,input().split())
for i in range(1,N+1):
    dic[input().strip()] = 0

for _ in range(M):
    now = input().strip()
    if now in dic.keys():
        dic[now] += 1

cnt = 0
for k,v in dic.items():
    if v > 0:
        cnt += 1
print(cnt)

ans = sorted(dic.items())

for elem in ans:
    if elem[1] > 0:
        print(elem[0])
