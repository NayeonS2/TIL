import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    N = int(input())

    time = [list(map(int,input().split())) for _ in range(N)]

    for i in range(N-1):
        min_idx = i
        for j in range(i+1,N):  # 종료 시간 빠른 순으로 정렬
            if time[min_idx][1] > time[j][1]:
                min_idx = j
        time[i], time[min_idx] = time[min_idx], time[i]


    cnt = 1 # 첫 활동은 미리 카운팅
    i = 0   # 첫 활동 부터 선택하여 검사 시작
    j = 1   # 비교 시작할 인덱스

    while True:
        if j == N:
            break

        if time[i][1] <= time[j][0]:    # 선택한 활동의 종료시간보다 같거나 큰 시작시간을 가지는 활동 체크해서 카운팅
            cnt += 1
            i = j   # 해당 활동 부터 다시 검사

        else:
            j += 1

    print(f'#{tc} {cnt}')