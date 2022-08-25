import sys
sys.stdin = open('input.txt')

def sorting(arr):
    N = len(arr)
    for i in range(N-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr



T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())

    arrive = list(map(int,input().split()))
    arrive = sorting(arrive)

    seconds = [0]*11112



    for i in range(len(seconds)):
        seconds[i] = (i // M)*K


    err = 0
    for x in range(len(arrive)):
        if seconds[arrive[x]] < x+1:
           err += 1

    if err>0:
        print(f'#{tc} Impossible')
    else:
        print(f'#{tc} Possible')