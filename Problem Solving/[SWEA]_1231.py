import sys
sys.stdin = open('input.txt')

def inorder(n):
    if n:
        inorder(ch1[n])
        print(char[n], end = '')
        inorder(ch2[n])



T = 10
for tc in range(1,T+1):
    V = int(input())
    root = 1

    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)

    char = dict()

    for _ in range(V):
        info = list(input().split())
        char[int(info[0])] = info[1]
        if len(info) == 4:
            ch1[int(info[0])] = int(info[2])
            ch2[int(info[0])] = int(info[3])
        elif len(info) == 3:
            ch1[int(info[0])] = int(info[2])

    print(f'#{tc}', end = ' ')
    inorder(root)
    print()





