import sys
sys.stdin = open('input.txt')

# 7자리 배열이 숫자 하나 -> 숫자 8개가 암호를 구성 -> 검사를 위해 56 길이의 문자열이 필요함

code = {'0001101':'0', '0011001':'1', '0010011':'2', '0111101':'3', '0100011':'4',
        '0110001':'5', '0101111':'6', '0111011':'7', '0110111':'8', '0001011':'9'}


T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split())


    arr = [input() for _ in range(N)]   # N개 줄에 걸쳐 0,1 배열을 받음
    text = ""
    i = 0
    while True:
        if i >= N:  # N개줄을 돌면서
            break

        line = arr[i][::-1] # 해당 줄을 끝에서 부터 검사

        j = 0
        while True:
            if not '1' in line: # 해당 라인에 1이 없으면 넘김
                break
            j += 1
            if line[j] == '1':  # 1을 발견하면 56 길이만큼 잘라서 text 에 할당
                text = line[j:j+56]

                i = N   # text 찾았으면 i=N으로 보내서 while문 break
                break
        i += 1

    find_sum = 0    # 암호코드에 포함된 숫자 합
    password_code = ""  # 암호코드


    text = text[::-1]   # 거꾸로 돌린 문자열을 다시 복구
    for i in range(0,len(text),7):

        find_sum += int(code[text[i:i+7]])
        password_code += code[text[i:i+7]]

    check_sum = 0   # 올바른 암호인지 체크 (홀짝 인덱스 나눠서)
    for i in range(1, len(password_code) + 1):
        if i % 2 == 1:
            check_sum += int(password_code[i - 1]) * 3
        elif i % 2 == 0:
            check_sum += int(password_code[i - 1])

    if check_sum % 10 == 0:
        print(f'#{tc} {find_sum}')
    else:
        print(f'#{tc} 0')