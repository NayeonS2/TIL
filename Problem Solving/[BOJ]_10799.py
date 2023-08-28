# 쇠막대기

import sys
from collections import defaultdict
sys.stdin = open('input.txt')

blk = input()
lst = []

nl = 0
nr = 0
for i in range(len(blk)):
    now = blk[i]
    if now != '(':
        continue
    else:
        nl += 1
    for j in range(i+1,len(blk)):

        if blk[j] == ')':
            nr += 1
        else:
            nl += 1

        if nl>0 and nr>0 and nl == nr:
            lst.append((i,j))
            nl = 0
            nr = 0
            break

dic = defaultdict(int)

point = []
for l,r in lst:
    if r-l == 1:
        point.append((l,r))
for pl,pr in point:
    for l,r in lst:
        if (l,r) not in point:
            if pl>l and pr<r:
                dic[(l,r)] += 1
        else:
            continue

cnt = 0
for k,v in dic.items():
    cnt += (v+1)
print(cnt)







