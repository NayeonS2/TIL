# 감소하는 수 (백트래킹)

N = int(input())
from itertools import combinations

nums = [9,8,7,6,5,4,3,2,1,0]
all_ = []
for i in range(1,11):
    combs = list(combinations(nums,i))

    for com in combs:
        com = sorted(com,reverse=True)
        str_ = list(map(str,com))
        all_.append(int(''.join(str_)))

all_.sort()

if N > 1022:
    print(-1)
else:
    print(all_[N])


