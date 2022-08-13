import sys
sys.stdin = open('input.txt')

T = 10

dr = [-1,0,0]
dc = [0,1,-1]

for tc in range(1,T+1):
    n = int(input())

    arr = [[0]+list(map(int,input().split()))+[0] for _ in range(100)]

    for j in range(102):
        if arr[99][j] == 2:
            goal_j = j

    r = 99
    d = 0

    while True:
        if r == 0:
            break

        if arr[r][goal_j+1] == 1:
            d = 1
            while True:
                r += dr[d]
                goal_j += dc[d]
                if arr[r][goal_j+1] == 0:
                    break

        elif arr[r][goal_j-1] == 1:
            d = 2
            while True:
                r += dr[d]
                goal_j += dc[d]
                if arr[r][goal_j-1] == 0:
                    break

        d = 0
        r += dr[d]
        goal_j += dc[d]
    print(f'#{tc} {goal_j-1}')
