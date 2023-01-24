k = 4
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

from collections import deque
def solution(k, tangerine):
    answer = 0
    pick = len(tangerine) - k
    temp = sorted(tangerine,key=lambda x:tangerine.count(x))

    q = deque(temp)

    i = 0
    while i<pick:
        q.popleft()
        i += 1

    answer = len(set(q))

    return q



print(solution(k,tangerine))