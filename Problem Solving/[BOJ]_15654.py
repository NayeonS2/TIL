# N과 M

import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())

nums = sorted(list(map(int,input().split())))

visited = [0]*(max(nums)+1)
def dfs(cnt,lst):

    if cnt == M:

        print(*lst)

    else:
        for i,n in enumerate(nums):
            if visited[n] == 0:
                    lst.append(n)
                    visited[n] = 1
                    dfs(cnt+1,lst)
                    visited[n] = 0
                    lst.pop()

dfs(0,[])

