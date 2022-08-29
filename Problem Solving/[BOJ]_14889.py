import sys
from itertools import combinations
sys.stdin = open('input.txt')



N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

nums = [x for x in range(1,N+1)] #1,2,3,   4, 5 6

comb = list(combinations(nums,N//2))
#print(comb)


counter_lst = []
for com in comb:
    counter = list(set(nums) - set(com))

    counter_lst.append(counter)

min_diff = 100


for i in range(len(comb)):
    team1 = comb[i]
    team2 = counter_lst[i]

    team1_sum = 0
    team2_sum = 0
    for j in range(N//2-1):

        for k in range(j+1, N//2):


            team1_sum += arr[team1[j] - 1][team1[k] - 1] + arr[team1[k] - 1][team1[j] - 1]
            team2_sum += arr[team2[j] - 1][team2[k] - 1] + arr[team2[k] - 1][team2[j] - 1]


    if abs(team1_sum-team2_sum) < min_diff:
        min_diff = abs(team1_sum-team2_sum)



print(min_diff)