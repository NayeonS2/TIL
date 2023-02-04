ldiag = set()
rdiag = set()
col = set()
N = int(input())
cnt = 0
def dfs(i):
    global cnt
    if i == N:
        cnt += 1
        return

    else:
        for j in range(N):
            if j in col or i+j in rdiag or i-j in ldiag:
                continue

            col.add(j)
            rdiag.add(i+j)
            ldiag.add(i-j)

            dfs(i+1)

            col.remove(j)
            rdiag.remove(i+j)
            ldiag.remove(i-j)

dfs(0)
print(cnt)
