# 이진수
# 규칙찾아서 DP로 풀기!

N = int(input())

d = [0] * (N+1)
d[0] = 0
d[1] = 0

for i in range(1,N):
    if i%2==0:
        d[i+1] = d[i]*2 - 1
    elif i%2==1:
        d[i + 1] = d[i] * 2 + 1

print(d[N])


# import sys
# sys.stdin = open('input.txt')
#
# def binar(start):
#     global new, cnt, temp
#
#     if cnt == N:
#         return
#     else:
#
#         for k in range(len(start)):
#             if start[k] == '1':
#                 new += '01'
#             elif start[k] == '0':
#                 new += '10'
#
#         temp = new
#         cnt += 1
#         new = ''
#         binar(temp)
#
#
# T = int(input())
# for _ in range(T):
#     N = int(input())
#
#     start = '1'
#     new = ''
#     temp = ''
#     cnt = 1
#     binar(start)
#     total = temp.split('1')
#     ans = 0
#     for i in range(len(total)):
#         if '0' in total[i]:
#            ans += 1
#     print(N,ans)
