# 치킨 배달

# N×N인 도시
# 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나
# 0은 빈 칸, 1은 집, 2는 치킨집
# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리 (치킨 거리는 집을 기준으로 정해짐)
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합
# 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|

# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
# 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구해라

import sys
from itertools import combinations
sys.stdin = open('input.txt')
input = sys.stdin.readline

def calcul_dis(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def chicken_dis(chickens):
    chicken_dis = 0
    for house in houses:
        min_dis = 987654321
        for chicken in chickens:
            min_dis = min(min_dis, calcul_dis(chicken, house))
        chicken_dis+=min_dis
    return chicken_dis

N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]

chickens = []
houses = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i,j))
        if arr[i][j] == 2:
            chickens.append((i,j))

chicken_comb = list(combinations(chickens,M))

res = 987654321
for comb in chicken_comb:
    res=min(res,chicken_dis(comb))
print(res)

