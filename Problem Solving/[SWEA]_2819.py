import sys
sys.stdin = open('input.txt')

def move(i, j, m, nums, N):
    global num_list

    if m == 7:
        if nums not in num_list:
            num_list.append(nums)
        return
    else:
        for di, dj in [[1,0],[-1,0],[0,-1],[0,1]]:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N:
                move(ni, nj, m + 1, nums + str(arr[ni][nj]) ,N)

T = int(input())

for tc in range(1,1+T):
    arr = [list(map(int,input().split())) for _ in range(4)]
    num_list = []
    nums = ''
    N = 4

    for i in range(N):
        for j in range(N):
            move(i,j,0,'',N)

    print(f'#{tc} {len(num_list)}')
