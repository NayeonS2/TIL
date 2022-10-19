# 일곱 난쟁이

from itertools import combinations

h = []
for _ in range(9):
    h.append(int(input()))

poss = list(combinations(h,7))

for pos in poss:
    if sum(pos) == 100:
        for n in sorted(pos):
            print(n)
        break
