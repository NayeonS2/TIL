import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())

def bfs(s,e):
    global min_cnt
    q = deque()
    cnt = 0
    q.append((s,cnt))
    visited[s] = 1


    while q:
        now,cnt = q.popleft()

        if now == e:
            min_cnt = min(min_cnt,cnt)
            return

        for next in [now+1, now-1, now*2, now-10]:
            if next in range(1,1000001) and visited[next]==0:
                q.append((next,cnt+1))
                visited[next] = 1

for tc in range(1,T+1):
    N,M = map(int,input().split())
    visited = [0] * 1000001
    min_cnt = 987654321
    bfs(N,M)
    print(f'#{tc} {min_cnt}')





