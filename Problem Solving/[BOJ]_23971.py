# ZOAC 4

import sys, math
sys.stdin = open('input.txt')

H,W,N,M = map(int,input().split())

wid = math.ceil(W/(M+1))

heig = math.ceil(H/(N+1))

print(wid*heig)


