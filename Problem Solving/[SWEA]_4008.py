# 숫자 만들기

import sys
import math
sys.stdin = open('input.txt')

def dfs(result, j):
    global max_res, min_res

    if j == N:
        if result > max_res:
            max_res = result
        if result < min_res:
            min_res = result
        return

    else:
        for i in range(4):
            if oper_num[i] > 0:
                oper_num[i] -= 1

                if i == 0:
                    dfs(result+nums[j],j+1)
                elif i == 1:
                    dfs(result-nums[j],j+1)
                elif i == 2:
                    dfs(result*nums[j],j+1)
                else:
                    dfs(math.trunc(result/nums[j]),j+1)

                oper_num[i] += 1



T = int(input())

for tc in range(1,1+T):
    N = int(input())
    oper_num = list(map(int,input().split()))
    nums = list(map(int,input().split()))

    max_res = -100000001
    min_res = 100000001

    dfs(nums[0],1)

    print(f'#{tc} {max_res-min_res}')