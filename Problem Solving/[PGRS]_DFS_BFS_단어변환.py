begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

from collections import deque

def solution(begin, target, words):

    def check(w1,w2):
        l1 = len(w1)
        cnt = 0
        for i in range(l1):
            if w1[i] != w2[i]:
                cnt += 1
        return cnt


    global min_
    min_ = 987654321
    def bfs(start, end):
        global min_
        q = deque()
        visited = [0]*len(words)
        q.append((start,0))

        while q:
            now, cnt = q.popleft()

            if now == end:
                min_ = min(min_, cnt)

            for i,next in enumerate(words):
                if check(now,next)==1 and visited[i] == 0:
                    q.append((next,cnt+1))
                    visited[i] = 1

    bfs(begin, target)

    if min_ == 987654321:
        return 0
    else:
        return min_


print(solution(begin, target, words))
