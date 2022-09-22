import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,1+T):
    binar = list(input())
    trinar = list(input())

    i = 0
    binar_list = []
    new_binar = binar[:]
    while True:
        if i == len(binar):
            break

        if binar[i] == '0':
            new_binar[i] = '1'
            binar_list.append(new_binar)

        elif binar[i] == '1':
            new_binar[i] = '0'
            binar_list.append(new_binar)
        new_binar = binar[:]
        i += 1

    j = 0
    trinar_list = []
    new_trinar1 = trinar[:]
    new_trinar2 = trinar[:]

    while True:
        if j == len(trinar):
            break

        if trinar[j] == '0':
            new_trinar1[j] = '1'
            new_trinar2[j] = '2'
            trinar_list.append(new_trinar1)
            trinar_list.append(new_trinar2)

        elif trinar[j] == '1':
            new_trinar1[j] = '0'
            new_trinar2[j] = '2'
            trinar_list.append(new_trinar1)
            trinar_list.append(new_trinar2)

        elif trinar[j] == '2':
            new_trinar1[j] = '0'
            new_trinar2[j] = '1'
            trinar_list.append(new_trinar1)
            trinar_list.append(new_trinar2)

        new_trinar1 = trinar[:]
        new_trinar2 = trinar[:]
        j += 1

    bin_dec_list = []
    for i in range(len(binar_list)):
        bin_num = ''.join(binar_list[i])
        bin_dec_list.append(int(bin_num,2))

    tri_dec_list = []
    for j in range(len(trinar_list)):
        tri_num = ''.join(trinar_list[j])
        tri_dec_list.append(int(tri_num, 3))

    for b in bin_dec_list:
        for t in tri_dec_list:
            if b == t:
                print(f'#{tc} {b}')