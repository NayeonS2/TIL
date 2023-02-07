priorities = [1,1,9,1,1,1]
location = 0

from collections import deque

def check(q):
    max_ = 0
    for v,k in q:
        max_ = max(max_,v)
    return max_


def solution(priorities, location):
    answer = 0


    q = deque()



    for i in range(len(priorities)):
        q.append((priorities[i],i))

    ans = []
    while q:
        now = q.popleft()
        if check(q)>now[0]:
            q.append(now)
        else:
            ans.append(now)

    for i in range(len(ans)):
        if ans[i][1] == location:
            answer = i+1


    return answer

print(solution(priorities,location))