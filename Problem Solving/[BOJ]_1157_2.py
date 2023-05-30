# 단어공부

import sys
sys.stdin = open('input.txt')

word = input()

dic = dict()

for w in word:
    dic[w.upper()] = 0

for w in word:
    dic[w.upper()] += 1

max_ = 0
for k,v in dic.items():
    max_ = max(max_,v)

ans = ''
tmp_cnt = 0
for k,v in dic.items():
    if v == max_:
        ans = k
        tmp_cnt += 1

if tmp_cnt == 1:
    print(ans)
else:
    print('?')
