import sys
sys.stdin = open('input.txt')

def min_v(lst):
    min_val = lst[0]
    for n in lst[1:]:
        if n < min_val:
            min_val = n
    return min_val

def max_v(lst):
    max_val = lst[0]
    for n in lst[1:]:
        if n > max_val:
            max_val = n
    return max_val




T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    nums = list(map(int,input().split()))

    intv_lst = []   # intervals 모음
    sum_lst = [] # 각각 interval의 합 모음
    for i in range(N-(M-1)):
        intv = nums[i:i+M]
        intv_lst.append(intv)
    for x in intv_lst:
        sum = 0

        for x_ in x:
            sum += x_
        sum_lst.append(sum)
    print(f'#{tc} {max_v(sum_lst) - min_v(sum_lst)}')