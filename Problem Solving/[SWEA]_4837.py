import sys

sys.stdin = open('input.txt')

def sum_(lst):
    sum_v = 0
    for x in lst:
        sum_v += x
    return sum_v

nums = [x for x in range(1,13)]
n = len(nums)
T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    ans = 0
    for i in range(1<<n):
        subset = []
        for j in range(n):
            if i & (1<<j):
                subset.append(nums[j])



        if len(subset) == N and sum_(subset) == K:
            ans += 1



    print(f'#{tc} {ans}')