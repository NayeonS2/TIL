# N번째 큰 수

T = int(input())

for _ in range(T):
    nums = sorted(list(map(int,input().split())), reverse=True)
    print(nums[2])