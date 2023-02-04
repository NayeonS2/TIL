# 스도쿠
import copy, sys
nums = [x for x in range(1,10)]

sys.stdin = open('input.txt')
arr = [list(map(int,input().split())) for _ in range(9)]
new = copy.deepcopy(arr)
visited = [0]*9
print(arr)

def square(n,arr):
    visited = [0]*10
    for i in range(3):
        for j in range(3):
            visited[arr[i][j]] = 1

    if visited[n] == 0:
        return True
    else:
        return False



def dfs(i):
    if i == 9:
        return





