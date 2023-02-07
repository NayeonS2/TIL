progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

import math
from collections import deque
def solution(progresses, speeds):
    answer = []

    q = deque()

    for i in range(len(progresses)):
        days = math.ceil((100-progresses[i])/speeds[i])
        q.append(days)

    preans = []
    while q:
        if len(preans)>0:
            if max(preans) >= q[0]:
                answer[-1] += 1
                preans.append(q.popleft())
            else:
                answer.append(1)
                preans.append(q.popleft())
        else:
            preans.append(q.popleft())
            answer.append(1)

    return answer

print(solution(progresses,speeds))