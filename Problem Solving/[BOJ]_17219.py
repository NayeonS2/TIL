# 비밀번호 찾기

import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline

N,M = map(int,input().split())

dic = dict()

for _ in range(N):
    mail,pw = input().split()
    dic[mail] = pw

for _ in range(M):
    now_mail = input().strip("\n")
    print(dic[now_mail])
