numbers = "17"

def check(num):
    if num < 2:
        return False

    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

from itertools import permutations
def solution(numbers):

    tmp = list(numbers)
    all_ =[]
    for i in range(1,len(tmp)+1):
        all_ += list(permutations(tmp,i))

    all_ = list(set(all_))

    ans = []

    for comb in all_:
        tmp_ = int(''.join(comb))
        if check(tmp_) == True and tmp_ not in ans:
            ans.append(tmp_)

    return len(ans)

print(solution(numbers))