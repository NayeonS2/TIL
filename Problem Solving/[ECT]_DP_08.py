# 병사 배치하기
# 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치
# 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외해야 하는 병사의 수

# Longest Increasing Subsequence (LIS) - 가장 긴 증가하는 부분 수열 문제 응용
# dp[i]는 arr[i]를 마지막 원소로 갖는 부분 수열의 최대 길이!
# dp[i]의 값을 1로 초기화
# 현재 위치(i)보다 이전에 있는 원소(j)가 작은지 확인한다. (크거나 같으면 가장 긴 증가하는 부분 수열이 될 수 없음)
# 작다면, 현재 위치의 이전 숫자 중, dp 최댓값을 구하고 그 길이에 1을 더해주면 된다.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
power = list(map(int,input().split()))[::-1]    # 이 문제는 감소하는 부분 수열 찾아야하기에 LIS로직 그대로 적용하기 위해 순서 뒤집어줌

d = [1] * N

for i in range(1,N):
    for j in range(i):
        if power[i] > power[j]:
            d[i] = max(d[i], d[j]+1)    # 현재 i 위치에서 arr[i]>arr[j] (0<=j<i)인 경우에만 갱신

print(N-max(d)) # 원래 power 리스트 길이에서 가장 긴 감소하는 부분 수열의 길이를 빼주면 열외시켜야하는 최소 인원



