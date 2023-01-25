k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]

from collections import Counter

def solution(k,tangerine):

    counter = Counter(tangerine)

    temp = sorted(counter,key=counter.get,reverse=True)

    answer = 0
    for tmp in temp:

        k -= counter[tmp]
        answer += 1

        if k <= 0:
            return answer


print(solution(k,tangerine))