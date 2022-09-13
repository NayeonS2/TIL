import sys
sys.stdin = open('input.txt')

def dfs(x,y):
    global cnt
    if x < 0 or x >= N or y < 0 or y >= N:
        return False

    if arr[x][y] == 1:
        arr[x][y] = 0
        cnt += 1

        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)

        return True
    return False



N = int(input())

arr = [list(map(int,input())) for _ in range(N)]

ans = 0
cnt = 0
cnt_lst = []
for i in range(N):
    for j in range(N):
        if dfs(i,j) == True:

            cnt_lst.append(cnt)
            cnt = 0
            ans += 1

print(ans)
for x in sorted(cnt_lst):
    print(x)
