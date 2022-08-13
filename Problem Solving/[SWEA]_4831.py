import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    K, N, M = map(int, input().split())
    nums = list(map(int,input().split()))

    start = 0
    charge = 0
    err = 0

    while start + K < N:
        for i in range(K, 0, -1):
            if start + i in nums:
                charge +=1
                start += i
                break
        else:
            err +=1
            break
    if err > 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {charge}')