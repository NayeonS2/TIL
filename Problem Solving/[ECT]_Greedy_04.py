# 모험가 길드

import sys
sys.stdin = open('input.txt')

N = int(input())
scared = list(map(int,input().split()))

temp = []

scared.sort(reverse=True)

cnt = 1
for person in scared:
    if person not in temp:
        temp.append(person)
    else:
        cnt += 1
        temp = []

print(cnt)

