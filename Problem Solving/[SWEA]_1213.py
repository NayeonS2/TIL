import sys
sys.stdin = open('1213.txt', encoding='UTF-8')

T = 10

def BruteForce(p,t):
    M = len(p)
    N = len(t)

    i = 0   # t인덱스
    j = 0   # p인덱스


    while j < M and i < N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    if j == M:

        return i
    else:
        return -1



for tc in range(1,T+1):
    n = int(input())
    goal = input()
    text = input()
    cnt = 0
    while goal in text:
        idx = BruteForce(goal,text)
        cnt +=1
        text = text[idx+len(goal):]
    print(f'#{tc} {cnt}')
