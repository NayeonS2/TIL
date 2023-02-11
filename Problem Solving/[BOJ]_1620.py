# 나는야 포켓몬 마스터 이다솜

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

dic = dict()
dic2 = dict()
N,M = map(int,input().split())

for i in range(1,N+1):
    now = input().strip()
    dic[now] = i
    dic2[str(i)] = now

for _ in range(M):
    ques = input().strip()
    if ques.isdigit():
        print(dic2[ques])
    else:
        print(dic[ques])

