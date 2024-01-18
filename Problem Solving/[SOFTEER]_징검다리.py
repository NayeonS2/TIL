# 남북으로 흐르는 개울에 동서로 징검다리가 놓여져 있다.
# 이 징검다리의 돌은 들쑥날쑥하여 높이가 모두 다르다. 철수는 개울의 서쪽에서 동쪽으로 높이가 점점 높은 돌을 밟으면서 개울을 지나가려고 한다.
# 돌의 높이가 서쪽의 돌부터 동쪽방향으로 주어졌을 때 철수가 밟을 수 있는 돌의 최대 개수는?

# 1 ≤ N ≤ 3×103 인 정수
# 1 ≤ Ai ≤ 108 인 정수

# 첫 번째 줄에 돌의 개수 N이 주어진다.
# 두 번째 줄에 돌의 높이 Ai (1 ≤ i ≤ N)가 서쪽부터 동쪽으로 차례로 주어진다.
# 돌은 연속으로 안밟아도됨!

# 5
# 3 2 1 4 5


N = int(input())
lst = list(map(int,input().split()))

dp = [1]*N

for i in range(N):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))



# max_ = 0
#
# i = 0
# while i<N:
#     cnt = 1
#     j = i+1
#     now_j = j
#     while j<N:
#         if lst[i]<lst[j]:
#             if j!=now_j and lst[j] < lst[now_j]:
#                 now_j = j
#                 j += 1
#             else:
#                 cnt += 1
#                 now_j = j
#                 j += 1
#         else:
#             j += 1
#     max_ = max(max_,cnt)
#
#     i += 1
#
# print(max_)

