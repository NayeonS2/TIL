# 고정점 찾기
# 고정점 : 수열의 원소 중 그 값이 인덱스와 동일한 원소
# N개의 서로다른 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
# 이때 수열에서 고정점이 있다면 고정점 출력 , 없다면 -1 출력
# 고정점은 최대 1개만 존재
# O(logN)

import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().split()))

def fixed_point(nums):
    for num in nums:
        idx = bisect_left(nums,num)+1   # 오름차순을 위배하지않고 num을 삽입할 수 있는 가장 왼쪽 인덱스 + 1 == num의 첫번째 인덱스
        try:
            if nums[idx] == idx:
                return idx
        except:
            return -1

print(fixed_point(nums))


