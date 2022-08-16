import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    sticks_list = list(input())
    length = len(sticks_list)

    i = 0
    cut_stick = 0   # 쇠막대기 조각 수
    stick_num = 0   # 누적 쇠막대기 수


    while i < length:
        if sticks_list[i] == '(':
            if sticks_list[i+1] == ')': # 레이저인 경우
                cut_stick += stick_num  # 누적된 막대 수를 막대기 조각 수에 더해줌
                i += 2
            else:
                stick_num += 1  # 레이저가 아닌 막대 시작부분인 경우 막대 누적 +1
                i += 1
        else:                   # 레이저가 아닌 막대 끝 부분인 경우 막대 누적 -1, 막대 조각 수 +1
            stick_num -= 1
            cut_stick += 1
            i += 1
    print(f'#{tc} {cut_stick}')

