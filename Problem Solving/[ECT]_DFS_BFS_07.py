# 연산자 끼워넣기

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

min_ = 1000000001
max_ = -1000000001


def dfs(idx, total, add, subs, mult, div):
    global max_, min_

    if idx == N:
        max_ = max(max_, total)
        min_ = min(min_, total)

    else:
        if add:
            dfs(idx + 1, total + nums[idx], add - 1, subs, mult, div)
        if subs:
            dfs(idx + 1, total - nums[idx], add, subs - 1, mult, div)
        if mult:
            dfs(idx + 1, total * nums[idx], add, subs, mult - 1, div)
        if div:
            dfs(idx + 1, int(total / nums[idx]), add, subs, mult, div - 1)


dfs(1, nums[0], oper[0], oper[1], oper[2], oper[3])
print(max_)
print(min_)
