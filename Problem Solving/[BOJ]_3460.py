# 이진수

import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    n = int(input())
    binar = bin(n)[2:][::-1]

    for i in range(len(binar)):
        if binar[i] == '1':
            print(i, end=" ")