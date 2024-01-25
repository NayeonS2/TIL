# 헬스장에서 N명의 회원이 운동을 하고 있다.
# 각 회원은 1에서 N사이의 번호가 부여되어 있고, i번 회원이 들 수 있는 역기의 무게는 Wi이다.
# 회원들 사이에는 M개의 친분관계 (Aj, Bj)가 있다.
# (Aj, Bj)는 Aj번 회원과 Bj번 회원이 친분 관계가 있다는 것을 의미한다.
# i번 회원은 자신과 친분 관계가 있는 다른 회원보다 들 수 있는 역기의 무게가 무거우면 자신이 최고라고 생각한다.
# 단, 누구와도 친분이 없는 멤버는 본인이 최고라고 생각한다.
# 이 헬스장에서 자신이 최고라고 생각하는 회원은 몇 명인가?

# 2 ≤ N ≤ 105
# 1 ≤ M ≤ 105
# 1 ≤ Wi ≤ 109
# 1 ≤ Aj, Bj ≤ N
# Aj ≠ Bj

# 첫 번째 줄에 두 정수 N, M이 주어진다.
# 두 번째 줄에 N개의 정수 W1, W2, ... , WN 이 주어진다.
# 다음 M개의 줄의 j번째 줄에는 두 정수 Aj, Bj 가 주어진다.

# 첫 번째 줄에 자신이 최고라고 생각하는 회원 수를 출력한다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

weight = list(map(int, input().split()))

friends = dict()

for i in range(1, N + 1):
    friends[i] = []

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)


def im_best(n):
    best = 1
    me = weight[n - 1]

    if len(friends[n]) == 0:
        return best
    else:
        for f in friends[n]:
            if weight[f - 1] >= me:
                best = 0
        return best


cnt = 0
for i in range(1, N + 1):
    if im_best(i) == 1:
        cnt += 1

print(cnt)
