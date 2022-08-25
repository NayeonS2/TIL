import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split())

    org_chz = list(map(int,input().split()))
    chz = []



    for idx, val in enumerate(org_chz):
        chz.append((idx+1,val))             # (피자번호, 치즈양) 튜플 리스트


    chz_set = chz[:N]                       # 한번에(N개) 들어갈 피자 리스트
    remain_chz = chz[N:]                    # N개넣고 남은 피자 리스트


    while True:
        if len(chz_set) == 1:               # 피자가 하나만 남으면 해당 번호 출력
            print(f'#{tc} {chz_set[0][0]}')
            break

        while chz_set:                      # 피자가 화덕에 있을 동안

                temp = chz_set.pop(0)       # 1번자리 직전에서 확인한다고 생각해야함! //2 한값이 0이면 빼고, 아니면 다시 뒤로 append
                melted = temp[1] //2
                if melted != 0:
                    chz_set.append((temp[0],temp[1]//2))
                else:
                    if remain_chz:          # //2 한 값이 0이면 뺀 후, 남은 피자 리스트에서 pop해서 append
                        chz_set.append(remain_chz.pop(0))
                break