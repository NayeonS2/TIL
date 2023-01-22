s = "(())()"
from collections import deque
def solution(s):
    answer = True

    q = deque()

    for char in s:
        q.append(char)
    temp = 0
    while q:

        if temp < 0:
            answer = False
            break
        now = q.popleft()
        if now == ")":
            temp -= 1
        else:
            temp += 1

    if temp == 0:
        answer = True
    else:
        answer = False

    return answer

print(solution(s))