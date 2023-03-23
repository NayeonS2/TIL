# 리모컨

import sys
from itertools import product
sys.stdin = open('input.txt')
input = sys.stdin.readline

res = 0
N = int(input())
len_n = len(list(str(N)))
M = int(input())

if M == 0:
    channel = [x for x in range(0,10)]
else:
    broken = list(map(int,input().split()))

    channel = []

    for x in range(0,10):
        if x not in broken:
            channel.append(x)

if len(channel) == 0:
    res = abs(N-100)
    print(res)

else:
    posss = []
    poss = set()
    for i in range(1,len_n+2):

        posss += list(product(channel,repeat=i))

    for tm in posss:
        tmp = ''
        for x in tm:
            tmp += str(x)
        tmp_pos = int(tmp)
        #tmp_pos = int(''.join(list(map(str, tm))))
        poss.add(tmp_pos)


    min_diff = 987654321
    str_poss = []
    for now_N in poss:
        # pos = list(map(str,pos))
        # now_N = int(''.join(pos))
        now_diff = abs(now_N-N)
        if now_diff < min_diff:
            min_diff = now_diff

    for now_N in poss:
        # pos = list(map(str,pos))
        # now_N = int(''.join(pos))
        now_diff = abs(now_N-N)
        if now_diff == min_diff:
            str_poss.append(now_N)

    if len(str_poss) == 0:
        start = 100
        start_len = len(list(str(start)))
        res = abs(N - start) + start_len
        if abs(N - 100) < res:
            print(abs(N - 100))
        else:
            print(res)

    elif len(str_poss) == 1:
        start = str_poss[0]
        start_len = len(list(str(start)))
        res = abs(N - start) + start_len
        if abs(N - 100) < res:
            print(abs(N - 100))
        else:
            print(res)

    else:
        min_res = 987654321
        for x in str_poss:
            start = x
            start_len = len(list(str(start)))
            res = abs(N - start) + start_len
            min_res = min(min_res,res)
        if abs(N - 100) < min_res:
            print(abs(N - 100))
        else:
            print(min_res)







