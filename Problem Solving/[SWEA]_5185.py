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

T = int(input())

for tc in range(1,1+T):
    N, hec = input().split()

    N = int(N)

    print(f'#{tc} {hec_to_bin(hec)}')
