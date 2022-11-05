import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

def bfs(s,e,cnt):
    q = deque()
    q.append((s,cnt))
    visited[s] = 1

    while q:
        s,cnt = q.popleft()

        if s == e:
            return cnt

        else:
            for pos in [s-1,s+1,s*2]:
                if 0<=pos<100001 and visited[pos] == 0:
                    if pos == s*2:
                        q.appendleft((pos,cnt))
                        visited[pos] = 1
                    else:
                        q.append((pos,cnt+1))
                        visited[pos] = 1


N,K = map(int,input().split())

visited = [0] * 100001

print(bfs(N,K,0))