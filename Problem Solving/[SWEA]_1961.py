import sys
sys.stdin = open('input.txt')
T = int(input())


def rot(arr):
    rotation = []
    for j in range(N):
        col = []
        for i in range(N - 1, -1, -1):
            col.append(arr[i][j])
        rotation.append(col)

    answer = []
    for res in rotation:
        ans = ''.join(map(str, res))
        answer.append(ans)
    return answer



for tc in range(1,1+T):
    N = int(input())

    arr = [list(map(int,input().split())) for _ in range(N)]



    rot_90 = rot(arr)
    rot_180 = rot(rot_90)
    rot_270 = rot(rot_180)

    print(f'#{tc}')
    for k in range(N):
        print(rot_90[k], rot_180[k], rot_270[k])

