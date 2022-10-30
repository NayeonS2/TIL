import sys
import time
import datetime
input = sys.stdin.readline

start = time.time()

N = int(input())

d = [0] * (N+1)
d[1] = 1

i1,i2,i3 = 1,1,1
mlt1,mlt2,mlt3 = 2,3,5
for i in range(2,N+1):
    d[i] = min(mlt1,mlt2,mlt3)
    if d[i] == mlt1:
        i1 += 1
        mlt1 = d[i1] * 2
    if d[i] == mlt2:
        i2 += 1
        mlt2 = d[i2] * 3
    if d[i] == mlt3:
        i3 += 1
        mlt3 = d[i3] * 5


print(d[N])
sec = time.time()-start
times = str(datetime.timedelta(seconds=sec)).split(".")
times = times[0]
print(times)
