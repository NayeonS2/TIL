# 암호만들기
import sys
from string import ascii_lowercase
sys.stdin = open('input.txt')

def f(i,k,r):
    global result

    if i == r:
        if not len(set(p)&vowel) < 1 and not len(set(p)&cons) < 2:
            if sorted(p) == p:
                result.append(''.join(p))

    else:
        for j in range(k):
            if i >= 1:
                if alphabet_list.index(a[j]) < alphabet_list.index(p[i-1]):
                    continue
            if used[j] == 0:    # a[j]가 아직 사용되지 않았으면
                used[j] = 1     # a[j] 사용됨으로  표시
                p[i] = a[j]     # p[i]는 a[j]로 결정
                f(i+1, k, r)       # p[i+1] 값을 결정하러 이동
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제

L,C = map(int,input().split())

alphs = list(input().split())

alphabet_list = list(ascii_lowercase)

vowel = {'a','e','i','o','u'}
cons = set(alphabet_list) - vowel

N = C
R = L
used = [0] * N
p = [0] * R
a = alphs
result = []
f(0, N, R)
for x in sorted(result):
    print(x)