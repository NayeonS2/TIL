import sys
sys.stdin = open('input.txt')

A, P = map(int,input().split())

nums = [A]
while True:
    tmp = 0
    for n in str(nums[-1]):
        tmp += int(n)**P

    if tmp in nums:
        break
    else:
        nums.append(tmp)

print(nums.index(tmp))



#재귀

import sys
sys.stdin = open('input.txt')

def dfs(num):
    temp = 0
    nums.append(num)

    for n in str(num):
        temp += int(n)**P

    if temp in nums:
        nums.append(temp)
        return
    else:
        dfs(temp)

A, P = map(int,input().split())
nums=[]
dfs(A)
print(nums.index(nums[-1]))