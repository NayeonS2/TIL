# N과 M(3)

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구해라
from itertools import product
N,M = map(int,input().split())

nums = [n for n in range(1,N+1)]

result = set(product(nums,repeat=M))

result = sorted(list(result))

for item in result:
    print(*item)


