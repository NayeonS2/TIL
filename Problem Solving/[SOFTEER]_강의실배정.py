# 김교수는 강의실 1개에 최대한 많은 강의를 배정하려고 한다.
# 배정된 강의는 서로 겹치지 않아야 하며 수업시간의 길이와 상관없이 최대한 강의를 많이 배정하라.
# 단, 두 강의의 시작시간과 종료시간은 겹쳐도 된다.

# 1 ≤ N ≤ 106 인 정수
# 1 ≤ Si ＜ Fi ≤ 109

# 첫 번째 줄에 강의 개수 N이 주어진다.
# i + 1 (1 ≤ i ≤ N)번째 줄에는 i번째 강의의 시작 시간 Si와 종료 시간 Fi가 주어진다.

# 첫 번째 줄에 최대 강의 수를 출력하라.

# 5
# 1 3
# 2 4
# 3 5

# 2

# 6
# 3 5
# 1 3
# 1 2
# 1 4
# 2 4
# 2 3

import heapq
import sys

q = []

N = int(sys.stdin.readline())

# for _ in range(N):
#     s,e = map(int,input().split())
#     lst.append((s,e))
#
# lst.sort()
#
# for s,e in lst:
#     heapq.heappush(q, (e-s, (s,e)))

for _ in range(N):
    s,e = map(int,sys.stdin.readline().split())
    heapq.heappush(q, (e, s))

cnt = 0
last_e = 0
while q:
    now = heapq.heappop(q)
    now_s, now_e = now[1], now[0]

    if now_s >= last_e:
        cnt += 1
        last_e = now_e

print(cnt)
