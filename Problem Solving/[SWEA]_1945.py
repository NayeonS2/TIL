import sys

sys.stdin = open('input.txt')

T = int(input())
elm = [2, 3, 5, 7, 11]
for tc in range(1, T+1):
   num = int(input())

   ans = ''
   for n in range(len(elm)):
       mult = 0
       while num % elm[n] == 0:
           num = num//elm[n]
           mult += 1
       ans = ans + str(mult) + ' '

   print(f'#{tc} {ans}')