import sys
sys.stdin = open('input.txt')

T = int(input())

def dfs(idx):
    visited[idx] = 1

    num = nums[idx]

    if not visited[num]:
        dfs(num)


for tc in range(1,T+1):
    N = int(input())
    nums = [0] + list(map(int,input().split()))

    visited = [1] + [0] * N

    ans = 0

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            ans += 1
    print(ans)
