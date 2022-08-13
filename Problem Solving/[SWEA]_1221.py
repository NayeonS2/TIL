import sys

sys.stdin = open('input.txt', encoding='UTF-8')


inp_str = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}



T = int(input())

for tc in range(1, T + 1):
    case, lng = input().split()
    text = input().split()
    result = []
    for x in text:
        if x in inp_str.keys():
            result.append(x)






    for i in range(len(result) - 1, 0, -1):
        for j in range(0, i):

            if inp_str[result[j]] > inp_str[result[j + 1]]:
                result[j], result[j + 1] = result[j + 1], result[j]
    ans = ' '.join(result)
    print(f'{case} {ans}')