# 소수

M = int(input())
N = int(input())

def prim(n):
    flag = 1
    if n == 1:
        flag = 0
    else:
        for i in range(2,n):
            if n%i == 0:
                flag = 0
                break
    if flag == 1:
        return True
    else:
        return False

sum_=0
cnt=0
min_ = 987654321
for n in range(M,N+1):
    if prim(n):
        cnt+=1
        sum_+=n
        if n<min_:
            min_=n
if cnt == 0:
    print(-1)
else:
    print(sum_)
    print(min_)



# M = int(input())
# N = int(input())
#
# def min_v(lst):
#     min_val = lst[0]
#     for x in lst:
#         if x < min_val:
#             min_val = x
#     return min_val
#
#
#
# sum_x = 0
# result = []
# for x in range(M,N+1):
#     possible = 0
#
#     for i in range(1,x+1):
#         if x % i == 0:
#             possible += 1
#     if possible == 2:
#         sum_x += x
#         result.append(x)
#
# if len(result) == 0:
#     print(-1)
# else:
#
#     print(sum_x)
#     print(min_v(result))