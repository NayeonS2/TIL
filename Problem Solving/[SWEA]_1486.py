import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    N, B = map(int,input().split())
    tall = list(map(int,input().split()))

    result = []

    min_h = 5005000
    for i in range(1<<len(tall)):
        subset = []
        for j in range(len(tall)):
            if i & (1<<j):
                subset.append(tall[j])
        if sum(subset) >= B and sum(subset) < min_h:
            min_h = sum(subset)



    print(f'#{tc} {min_h-B}')