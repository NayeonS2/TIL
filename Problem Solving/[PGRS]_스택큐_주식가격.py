prices = [1, 2, 3, 2, 3]

from collections import deque
def solution(prices):
    answer = []

    q = deque(prices)

    while q:

        now = q.popleft()
        cnt = 0
        for other_price in q:
            cnt += 1
            if other_price < now:
                break
        answer.append(cnt)

    return answer
print(solution(prices))