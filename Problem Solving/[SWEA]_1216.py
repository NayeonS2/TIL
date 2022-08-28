import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,1+T):
    t = int(input())
    arr = [list(input()) for _ in range(100)]
    rev_arr = list(zip(*arr))


    ans = []
    for k in range(100,0,-1):
        for i in range(100):
            for j in range(100-k+1):
                if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                    if len(ans) == 0:
                        ans.append(k)
                    else:
                        if ans[-1] < k:
                            ans.append(k)

    for k in range(100,0,-1):
        for i in range(100):
            for j in range(100 - k + 1):
                if rev_arr[i][j:j + k] == rev_arr[i][j:j + k][::-1]:
                    if len(ans) == 0:
                        ans.append(k)
                    else:
                        if ans[-1] < k:
                            ans.append(k)


    print(f'#{tc} {ans[-1]}')