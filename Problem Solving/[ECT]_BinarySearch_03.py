# 정렬된 배열에서 특정 수의 개수 구하기
# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있다.
# 이때 이 수열에서 x가 등장하는 횟수를 계산하라.
# 값이 x인 원소가 하나도 없으면 -1 출력
# O(logN)

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def count_num(nums,x):
    # 오름차순을 위배하지않고 num을 삽입할 수 있는 가장 왼쪽,오른쪽 인덱스
    right_ = bisect_right(nums,x)
    left_ = bisect_left(nums, x)
    return right_ - left_


N,x = map(int,input().split())
nums = list(map(int,input().split()))

if count_num(nums,x) == 0:
    print(-1)
else:
    print(count_num(nums,x))
