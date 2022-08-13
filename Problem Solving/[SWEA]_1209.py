import sys
sys.stdin = open('input.txt')

def max_v(lst):
    max_val = 0
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val


T = 10
for tc in range(1, T+1):
    test_n = int(input())
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))



    sum_ = []
    for i in range(100):
        each_row = 0
        for j in range(100):
            each_row += arr[i][j]
        sum_.append(each_row)

    for j in range(100):
        each_col = 0
        for i in range(100):
            each_col += arr[i][j]
        sum_.append(each_col)


    for i in range(100):
        l_diag = 0
        l_diag += arr[i][i]
        sum_.append(l_diag)

    for i in range(100):
        r_diag = 0
        r_diag += arr[i][100-1-i]
        sum_.append(r_diag)
    print(f'#{test_n} {max_v(sum_)}')