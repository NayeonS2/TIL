#import sys
#sys.stdin = open('input.txt')
N, K = map(int, input().split())
table = [[0]*6 for _ in range(2)]
room = 0
for _ in range(N):
    S, Y = map(int,input().split())
    table[S][Y-1] += 1

for i in range(2):
    for j in range(6):

        if table[i][j] and table[i][j] > K:
            if table[i][j] % K == 0:
                room += table[i][j] // K
            elif table[i][j] % K != 0:
                room += table[i][j] // K + 1
        elif table[i][j] and table[i][j] <= K:
            room += 1

print(room)





