# 곱하기 혹은 더하기

S = '576'

nums = list(map(int,S))

temp = nums[0]  # 첫값
for i in range(1,len(nums)):
    temp = max(temp*nums[i],temp+nums[i])   # 매번 더 큰값 선택

print(temp)



