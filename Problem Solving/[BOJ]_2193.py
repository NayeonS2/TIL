N = int(input())

d = [0] * (N+1)

d[0] = 0    # 1 <= N <= 90 이기때문에 d[0] 값 설정안해주면 런타임에러!
d[1] = 1


for i in range(2,N+1):
    d[i] = d[i-1] + d[i-2]

print(d[N])