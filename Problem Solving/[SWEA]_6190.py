import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    nums = list(map(int,input().split()))

    multip = []
    for i in range(N-1):
        multip.append(nums[i]*nums[i+1])

    result = []
    for mult in multip:
        num = str(mult)

        for n in range(len(num)-1):
            if int(num[n]) <= int(num[n+1]):
                result.append(int(num))
    if len(result) == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(result)}')

