D, K = map(int,input().split())

# n : 첫날 준 떡의 수 / m : 둘쨋날 준 떡의 수
# 첫쨋날 : 1n + 0m / 둘쨋날 : 0n + 1m / 셋쨋날 : 1n + 1m / 넷쨋날 : 1n + 2m / 다섯쨋날 : 2n + 3m / 여섯쨋날 : 3n + 5m


d = [0] * 31    # 계수를 담을 dp 테이블

d[1] = (1,0)
d[2] = (0,1)

for i in range(3,D+1):
    d[i] = (d[i-2][0] + d[i-1][0], d[i-2][1] + d[i-1][1])

a = d[D][0]
b = d[D][1]

n, m = 1, 1

while True:
    if a*n + b*m == K:
        print(n)
        print(m)
        break
    elif a*n + b*m < K:
        m += 1
    elif a*n + b*m > K:
        n += 1
        m = n
