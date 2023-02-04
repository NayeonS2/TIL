# N과 M (1),(2),(3),(4)

N,M = map(int,input().split())

nums = [x for x in range(1,N+1)]
answer = []

def dfs(cnt,lst):

    if cnt == M:
        print(*lst)


    else:
        for i,n in enumerate(nums):
            if len(lst) == 0:
                lst.append(n)

                dfs(cnt + 1, lst)

                lst.pop()
            else:
                if lst[-1] <= n:
                    lst.append(n)

                    dfs(cnt + 1, lst)

                    lst.pop()


dfs(0,[])
