# 약수 구하기

N,K = map(int,input().split())

nums = []
for i in range(1,N+1):
    if N%i == 0:
        nums.append(i)

try:
    print(nums[K-1])
except:
    print(0)


