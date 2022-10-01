# 벌꿀 채취
from itertools import combinations
import sys
sys.stdin = open('input.txt')

T = int(input())

def find_max_honey(honey):
    find_max = 0
    for i in range(1,len(honey)+1):
        honey_combs = list(combinations(honey,i))
        for comb in honey_combs:
            if sum(comb) <= C:
                temp = 0
                for x in comb:
                    temp += x**2
                if temp > find_max:
                    find_max = temp
    return find_max


for tc in range(1,1+T):
    N, M, C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    poss_profits = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N-M+1):
            poss_profits[i][j] = find_max_honey(arr[i][j:j+M])

    max_profits = []
    for prof in poss_profits:
        max_profits.append(max(prof))

    print(f'#{tc} {sorted(max_profits,reverse=True)[0]+sorted(max_profits,reverse=True)[1]}')