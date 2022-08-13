def MinValue(A):
    Temp = 0
    for i in A :
        if Temp == 0 or i < Temp :
            Temp = i
    return Temp
 
 
 
 
T = 10
 
for t in range(1, T+1):
    ans = 0
    L = int(input())
    nums = list(map(int, input().split()))
    diffs = []
    for n in range(2,L-2):
        diff1 = nums[n] - nums[n-2]
 
        diff2 = nums[n] - nums[n-1]
 
        diff3 = nums[n] - nums[n+1]
 
        diff4 = nums[n] - nums[n+2]
 
        if diff1 > 0 and diff2 > 0 and diff3 > 0 and diff4 > 0:
            ans += MinValue([diff1,diff2,diff3,diff4])
 
 
 
 
 
    print(f'#{t} {ans}')
