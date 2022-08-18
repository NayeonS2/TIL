import sys
sys.stdin = open('input.txt')

square = [[0]*100 for _ in range(100)]



for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1,y2):
        for j in range(x1, x2):
            square[i][j] = 1

def count_(lst,p):
    cnt = 0
    for x in lst:
        if x == p:
            cnt+=1
    return cnt




ans = 0
for row in square:
    ans += count_(row,1)
print(ans)
