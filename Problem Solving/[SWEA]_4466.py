def sorting(arr):
    N = len(arr)
    for i in range(N-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, K = map(int,input().split())
    submit = list(map(int,input().split()))

    students = [x for x in range(1,N+1)]

    ans = ''
    for n in set(submit)^set(students):
        ans = ans + str(n) + ' '
    print(f'#{tc} {ans}')




