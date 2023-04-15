import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
nums = [x for x in range(1,N+1)]
visited = [-1]*N

def dfs(cnt,lst):

    if cnt == M:
        print(*lst)

    else:
        for i,n in enumerate(nums):
            if visited[i] == -1:
                lst.append(n)
                visited[i] = 1
                dfs(cnt+1,lst)
                visited[i] = -1
                lst.pop()

dfs(0,[])








