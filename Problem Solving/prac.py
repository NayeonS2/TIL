import sys
from itertools import combinations
sys.stdin = open('input.txt')

L,C = map(int,input().split())

chars = list(input().split())



alphs = [chr(c) for c in range(ord('a'),ord('z')+1)]

moum = ['a', 'e', 'i', 'o', 'u']
jaum = list(set(alphs) - set(moum))

combs = list(combinations(alphs,L))

def moum_chk(txt):
    cnt = 0

    for m in moum:
        if m in txt:
            cnt += 1

    if cnt > 0:
        return True


def jaum_chk(txt):

    cnt = 0

    for j in jaum:
        if cnt > 2:
            break

        if j in txt:
            cnt += 1


    if cnt >= 2:
        return True



for comb in combs:

    if comb == sorted(comb) and moum_chk(comb) and jaum_chk(comb):
        print(comb)












