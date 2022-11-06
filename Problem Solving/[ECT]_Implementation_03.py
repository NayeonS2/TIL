# 럭키 스트레이트

num = input()
n = len(num)//2

if sum(map(int,list(num[:n]))) == sum(map(int,list(num[n:]))):
    print('LUCKY')
else:
    print('READY')
