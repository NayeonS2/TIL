# ATM

import sys
sys.stdin = open('input.txt')

N = int(input())
times = list(map(int,input().split()))

dic = dict()

for i in range(1,len(times)+1):
    dic[i] = times[i-1]

dic_sort = sorted(dic.items(),key=lambda x : x[1])

cnt = 0
tmp = 0
for elem in dic_sort:
    tmp += elem[1]
    cnt += tmp

print(cnt)