# 최대 상금

from itertools import combinations
import sys
sys.stdin = open('input.txt')

def swap(i):

    global max_money

    if i == chg:
        now_money = int(''.join(map(str,nums_lst)))

        if now_money > max_money:
            max_money = now_money

        return

    else:
        for comb in idx_combs:
            l,r = comb[0] , comb[1]

            nums_lst[l], nums_lst[r] = nums_lst[r], nums_lst[l]

            temp = int(''.join(map(str,nums_lst)))

            if temp not in visited[i]:
                visited[i].append(temp)
                swap(i + 1)

            nums_lst[l], nums_lst[r] = nums_lst[r], nums_lst[l]


T = int(input())

for tc in range(1,1+T):
    nums, chg = input().split()
    chg = int(chg)
    nums_lst = list(map(int,list(nums)))

    visited = [[] for _ in range(10)]

    idxs = [i for i in range(len(nums_lst))]
    idx_combs = list(combinations(idxs,2))

    max_money = 0
    swap(0)
    print(f'#{tc} {max_money}')