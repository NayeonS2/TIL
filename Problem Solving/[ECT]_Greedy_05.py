# 곱하기 혹은 더하기

S = '576'

nums = list(map(int,S))

temp = nums[0]
for i in range(1,len(nums)):
    temp = max(temp*nums[i],temp+nums[i])

print(temp)



