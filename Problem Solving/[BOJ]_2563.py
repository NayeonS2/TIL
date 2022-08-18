#import sys
#sys.stdin = open('input.txt')

N = int(input())

square = [[0]*100 for _ in range(100)]
for _ in range(N):
    x, y = map(int,input().split())
    for i in range(y,y+10):
        for j in range(x, x+10):
            square[i][j] = 1

def count_(lst,p):
    cnt = 0
    for x in lst:
        if x == p:
            cnt += 1
    return cnt

ans = 0
for row in square:
    ans += count_(row,1)
print(ans)

