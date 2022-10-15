import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    N, K = map(int,input().split())
    nums = input()
    rot = N//4
    nums += nums[:rot]

    poss = []
    for i in range(len(nums)-2):
        if int(nums[i:i+rot],16) not in poss:
            poss.append(int(nums[i:i+rot],16))
    print(f'#{tc} {sorted(poss,reverse=True)[K-1]}')