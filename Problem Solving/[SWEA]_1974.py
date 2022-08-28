import sys

sys.stdin = open('input.txt')

T = int(input())


def is_dup(lst):
    blk = []
    for x in lst:
        if x not in blk:
            blk.append(x)
    if len(blk) < len(lst):
        return True
    return False


for tc in range(1, 1 + T):
    arr = [list(map(int, input().split())) for _ in range(9)]
    rev_arr = list(zip(*arr))

    err = 0
    for i in range(9):
        if is_dup(arr[i]):
            err += 1

    for i in range(9):
        if is_dup(rev_arr[i]):
            err += 1

    square_lst = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for k in range(3):
                square.append(arr[i + k][j:j + 3])
            square_lst.append(square)
    for sqr in square_lst:
        nums = []
        for n in sqr:
            for n_ in n:
                nums.append(n_)

        if is_dup(nums):
            err += 1

    if err > 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} 1')