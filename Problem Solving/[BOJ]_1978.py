# 소수 찾기

N = int(input())

nums = list(map(int,input().split()))

cnt = 0
for n in nums:
    flag = 1
    if n == 1:
        flag = 0
    else:
        for i in range(2,n):
            if n%i == 0:
                flag = 0
                break
    if flag == 1:
        cnt += 1
print(cnt)