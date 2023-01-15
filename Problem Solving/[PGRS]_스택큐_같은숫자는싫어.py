
arr = [4,4,4,3,3]

from collections import deque
def solution(arr):
    answer = []
    arr = deque(arr)
    while arr:
        tmp = arr.popleft()
        if len(answer) == 0:
            answer.append(tmp)
        else:
            if answer[-1] != tmp:
                answer.append(tmp)
    return answer

print(solution(arr))