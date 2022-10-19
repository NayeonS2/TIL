# 쉽게 푸는 문제

a,b = map(int,input().split())

d = [0]*1001

d[1] = 1

i = 2
k = 2
while True:
    if i >= 1000:
        break
    else:
        for k_i in range(i,i+k):
            try:
                d[k_i] = k
            except:
                break

    i += k
    k += 1
print(sum(d[a:b+1]))







