# AC
# 함수 R은 배열에 있는 수의 순서를 뒤집는 함수 (아이디어 떠올리는게 핵심!!!!)
# D는 첫 번째 수를 버리는 함수
# 배열이 비어있는데 D를 사용한 경우에는 에러가 발생 (error)

import sys
from collections import deque
sys.stdin = open('input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    funcs = deque(list(input()))

    n = int(input())

    num = input()
    nums = num.rstrip()[1:-1].split(",")

    nums = deque(nums)

    if "" in nums:
        nums.popleft()


    res = nums
    reversing = 0
    while funcs:

        now_f = funcs.popleft()

        if now_f == "R":
            reversing += 1

        elif now_f == "D":
            if res == deque([]):
                res = "error"
                break
            else:
                if reversing%2 == 0:
                    res.popleft()
                else:
                    res.pop()


    if res == "error":
        print(res)
    else:
        if reversing%2 == 0:
            print("[" + ",".join(res)+"]")
        else:
            res.reverse()
            print("[" + ",".join(res) + "]")



