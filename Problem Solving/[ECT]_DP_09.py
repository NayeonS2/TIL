# 못생긴 수
# 2,3,5 만을 약수로 가지는 합성수
# 못생긴 수에 2,3,5 를 곱한 수 또한 못생긴 수임!

# 1,2,3,4,5,6,8,9,10,12,15 ...

import sys
import time
import datetime
input = sys.stdin.readline

start = time.time()
N = int(input())

d = [0] * (N+1)
d[1] = 1    # 1은 못생긴 수

lst = set()
# [2,3,5] -> [3,5,4,6,10] -> [5,4,6,10,9,15] ...
for i in range(2,N+1):
    lst.update([d[i-1]*2, d[i-1]*3, d[i-1]*5])
    d[i] = min(lst)
    lst.remove(d[i])


print(d[N])

sec = time.time()-start
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)

# N = 1000
# d[N] = 51200000
# times = 0:00:01