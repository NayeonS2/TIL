# A -> B
# visited 쓰면 메모리 초과!

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
A,B = map(int,input().split())

def bfs(s,e,cnt):
    q = deque()
    q.append((s,cnt))

    while q:
        s,cnt = q.popleft()

        if s == e:
            return cnt+1

        for oper in [s*2, int(str(s)+'1')]:
            if oper <= e:
                q.append((oper,cnt+1))
    return -1

print(bfs(A,B,0))




