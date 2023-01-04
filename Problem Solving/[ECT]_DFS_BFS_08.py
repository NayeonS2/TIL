# 감시피하기
# 장애물을 정확히 3개 설치하여 모든 학생들이 선생님들의 감시를 피하도록 할 수 있는지 출력
# 선생님이 존재하는 칸은 T, 학생이 존재하는 칸은 S, 장애물이 존재하는 칸은 O로 표시
# 선생님은 상, 하, 좌, 우 4가지 방향에 대하여, 아무리 멀리 있더라도 장애물로 막히기 전까지의 학생들은 모두 볼 수 있다

import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [list(input().split()) for _ in range(N)]

teacher = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]=='T':
            teacher+=1

def up(i, j, arr):
    while i>=0:

        if arr[i][j] == 'O':
            break

        if arr[i][j] == 'S':
            return True
        i -= 1
    return False


def down(i, j, arr):
    while i<N:
        if arr[i][j] == 'O':
            break

        if arr[i][j] == 'S':
            return True

        i += 1
    return False

def left(i, j, arr):

    while j>=0:

        if arr[i][j] == 'O':
            break


        if arr[i][j] == 'S':
            return True
        j -= 1
    return False

def right(i, j, arr):
    while j<N:

        if arr[i][j] == 'O':
            break


        if arr[i][j] == 'S':
            return True
        j += 1
    return False



result = False
def obstacle(obs):
    global result
    if obs == 3:
        not_find = 0
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 'T':
                    if (up(i, j, arr) == False) and (down(i, j, arr) == False) and (left(i, j, arr) == False) and (
                            right(i, j, arr) == False):
                        not_find += 1
        if not_find == teacher:
            result = True
        return

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                obstacle(obs + 1)
                arr[i][j] = 'X'


obstacle(0)
if result == True:
    print('YES')
elif result == False:
    print('NO')
