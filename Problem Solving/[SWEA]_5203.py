import sys
sys.stdin = open('input.txt')


def babygin(p):

    for i in range(10): # tri
        if p[i] >= 3:   # 3장 이상인 숫자가 있으면
            return True

    for j in range(8):  # run # 7,8,9 가 마지막 케이스이므로
        if p[j] and p[j+1] and p[j+2]:  # 이어지는 숫자가 3개인 경우가 있으면
            return True

    return False


T = int(input())

for tc in range(1,1+T):
    cards = list(map(int,input().split()))

    p1 = [0] * 10   # 카운팅 배열
    p2 = [0] * 10



    win = 0
    for i in range(6):
        p1[cards[i*2]] += 1 # 홀짝 순서 나눠서 cnt += 1
        p2[cards[i*2+1]] += 1

        if babygin(p1): # player1이 이기면 win = 1하고 break
            win = 1
            break
        if babygin(p2): # player2이 이기면 win = 2하고 break
            win = 2
            break

    print(f'#{tc} {win}')