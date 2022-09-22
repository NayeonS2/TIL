import sys

sys.stdin = open('input.txt')



def hec_to_bin(nums):
    n_range = [str(x) for x in range(0, 10)]

    chr_range = {'A': '1010', 'B': '1011',
                 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

    binar_num = ""
    for i in range(len(nums)):
        if nums[i] in n_range:
            binar = format(int(nums[i]), 'b')

            if len(binar) < 4:
                binar = '0' * (4 - len(binar)) + str(binar)

            binar_num += binar
        elif nums[i] in chr_range.keys():
            binar = chr_range[nums[i]]
            binar_num += binar
    return binar_num


def check_code(code_list):  # 올바른 코드인지 검사

    check_sum = 0
    for i in range(len(code_list)):
        if i % 2 == 1:
            check_sum += int(code_list[i]) * 3
        elif i % 2 == 0:
            check_sum += int(code_list[i])

    if check_sum % 10 == 0:
        return True
    else:
        return False



code_dic = {
    (2,1,1):0,
    (2,2,1):1,
    (1,2,2):2,
    (4,1,1):3,
    (1,3,2):4,
    (2,3,1):5,
    (1,1,4):6,
    (3,1,2):7,
    (2,1,3):8,
    (1,1,2):9
}

T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]

    arr = sorted(list(set(arr)))  # 중복행제거

    arr.pop(0)  # 0만있는 행 제거

    total_sum = 0
    visited = []

    for i in range(len(arr)):
        line = hec_to_bin(arr[i])  # 이진수 변환
        line = line.rstrip('0')  # 오른쪽 0 제거

        pwd_list = []

        n1 = n2 = n3 = n4 = 0
        for j in range(len(line)-1,-1,-1):  # 행 끝부터
            if line[j] == '1' and n3 == 0:
                n4 += 1
            elif line[j] == '0' and n2 == 0:
                n3 += 1
            elif line[j] == '1' and n1 == 0:
                n2 += 1
            elif line[j] == '0':
                if line[j-1] == '1':
                    min_n = min(n2,n3,n4)
                    pwd_list.append((code_dic[n2//min_n,n3//min_n,n4//min_n]))

                    n2 = n3 = n4 = 0

                    if len(pwd_list) == 8:  # 암호코드 8자리 완성되면
                        if check_code(pwd_list):
                            if pwd_list not in visited:  # 더해준적 없는 애들만
                                total_sum += sum(pwd_list)
                                visited.append(pwd_list)
                        pwd_list = []

    print(f'#{tc} {total_sum}')