# 삼각형과 세 변

import sys
sys.stdin = open('input.txt')

while True:

    a,b,c = map(int,input().split())

    if a==0 and b==0 and c==0:
        break

    if max([a, b, c]) >= sum([a, b, c]) - max([a, b, c]):
        print("Invalid")
    else:
        if a == b and b == c:
            print("Equilateral")
        elif (a != b and a == c and b != c) or (b != c and a != c and a == b) or (a != c and b == c and a != b):
            print("Isosceles")
        elif a != b and b != c and a != c:
            print("Scalene")



