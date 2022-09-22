import sys

sys.stdin = open('input.txt')



T = int(input())

for tc in range(1,1+T):
    hec_float = float(input())


    float_n = []
    binar = ""
    while True:
        if hec_float == 0 or int(str(hec_float*2).split('.')[1]) in float_n:
            if len(binar) <= 12:
                print(f'#{tc} {binar}')
            else:
                print(f'#{tc} overflow')

            break

        binar += str(str(hec_float * 2).split('.')[0])
        float_n.append(int(str(hec_float * 2).split('.')[1]))
        hec_float = (hec_float * 2) - int(str(hec_float*2).split('.')[0])