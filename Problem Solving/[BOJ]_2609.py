# 최대공약수와 최소공배수
# a*b = 최대공약수 * 최소공배수

a,b = map(int,input().split())

gcd = 0
for i in range(1,min(a,b)+1):
    if a%i == 0 and b%i == 0:
        if i>gcd:
            gcd = i

lcm = a*b // gcd

print(gcd)
print(lcm)

