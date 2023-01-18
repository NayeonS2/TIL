# 모험가 길드

import sys
sys.stdin = open('input.txt')

N = int(input())
scared = list(map(int,input().split()))

temp = []

scared.sort(reverse=True) # 내림차순

cnt = 1
for person in scared:
    if person not in temp:  # 가장 큰 수 보다 작은 수들
        temp.append(person)
    else:   # 중복된 작은 수가 나오면 cnt + 1
        cnt += 1
        temp = []

print(cnt)

