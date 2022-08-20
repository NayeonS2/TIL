import sys
sys.stdin = open('input.txt')



T = 10

for tc in range(1, 1+T):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(100)]

    resid = 0                       # 교착상태 수

    for i in range(100):
        status = 0                  # 상태 변수 설정
        for j in range(100):

            if table[j][i] == 1:    # N극 자성체를 만나면
                status = 1          # 상태 변수 활성화
            elif table[j][i] == 2:  # 상태 변수가 활성화 된 상태로 (N극을 거친 이후)
                if status:          # S극 자성체를 만나면
                    status = 0      # 상태 변수는 초기화하고
                    resid += 1      # 교착 상태 수 + 1



    print(f'#{tc} {resid}')