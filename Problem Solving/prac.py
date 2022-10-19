N = int(input())

d = [0] * (N+1)

d[1] = 0
d[2] = 1
d[3] = 1
d[4] = 3
for i in range(4,N):
    if i%2==0:
        d[i+1] = d[i]*2 - 1
    elif i%2==1:
        d[i + 1] = d[i] * 2 + 1

print(d[N])






