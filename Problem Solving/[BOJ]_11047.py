# 동전 0
import sys
sys.stdin = open('input.txt')

N,K = map(int,input().split())

money = []
for _ in range(N):
    n = int(input())
    if n <= K:
        money.append(n)

money.sort(reverse=True)

res = 0
i = 0
cnt = 0
while True:
    if res == K:
        break
    else:
        if res + money[i] > K:
            i += 1
        else:
            res += money[i]
            cnt += 1
print(cnt)