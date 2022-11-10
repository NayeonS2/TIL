# 보물상자 비밀번호

import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    nums = list(input())

    turns = N//4
    res = []
    for _ in range(turns):
        for i in range(0,len(nums),turns):
            tmp = int(''.join(nums[i:i+turns]),16)
            if tmp not in res:
                res.append(tmp)
        nums = [nums[-1]] + nums[:-1]



    res = sorted(res,reverse=True)

    print(f'#{tc} {res[K-1]}')


