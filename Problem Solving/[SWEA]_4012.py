import sys
from itertools import combinations
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]

    elem = [x for x in range(1,N+1)]

    combs = list(combinations(elem,N//2))

    min_diff = 19999
    for comb in combs:
        counter = tuple(set(elem) - set(comb))

        sum_subcomb = 0
        sum_subcounter = 0
        for subcom in list(combinations(comb, 2)):
            sum_subcomb += (arr[subcom[0]-1][subcom[1]-1] + arr[subcom[1]-1][subcom[0]-1])
        for subcounter in list(combinations(counter, 2)):
            sum_subcounter += (arr[subcounter[0]-1][subcounter[1]-1] + arr[subcounter[1]-1][subcounter[0]-1])

        if abs(sum_subcomb - sum_subcounter) < min_diff:
            min_diff = abs(sum_subcomb - sum_subcounter)
    print(f'#{tc} {min_diff}')