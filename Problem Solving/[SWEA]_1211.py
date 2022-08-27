import sys
sys.stdin = open('input.txt')

dr = [-1,0,0]
dc = [0,1,-1]

def find_route(arr,c):
    d = 0
    r = 99
    go = 0

    while True:

        if r == 0:
            break


        if arr[r][c+1] == 1:
            d = 1
            while True:
                r += dr[d]
                c += dc[d]
                go += 1
                if arr[r][c+1] == 0:
                    break
        elif arr[r][c-1] == 1:
            d = 2
            while True:
                r += dr[d]
                c += dc[d]
                go += 1
                if arr[r][c-1] == 0:
                    break

        d = 0
        r += dr[d]
        c += dc[d]
        go += 1
    return go, c-1





T = 10
for tc in range(1,1+T):
    t = int(input())
    arr = [[0] + list(map(int,input().split())) + [0] for _ in range(100)]


    start_point = []
    for j in range(102):
        if arr[99][j] == 1:
            goal_j = j
            start_point.append(goal_j)

    go_lst = []
    result = []
    for p in start_point:
        go_lst.append(find_route(arr,p)[0])
        result.append(find_route(arr,p))
    for go, arrive in result:
        if go == min(go_lst):
            print(f'#{tc} {arrive}')