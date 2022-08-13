import sys
sys.stdin = open('input.txt')

def sorting(lst):

    for i in range(len(lst)-1):
        min_idx = i
        for j in range(i+1,len(lst)):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst




T = int(input())

for tc in range(1,T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = ''

    i=0
    while i < 10//2:
        ans = ans + str(sorting(nums)[-(i+1)]) + ' ' + str(sorting(nums)[i]) + ' '
        i +=1
    print(f'#{tc} {ans}')