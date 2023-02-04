from itertools import combinations

weight = [100, 50, 50, 80, 40, 40]


def check(weight,lst):
    global visited
    if len(lst) > 0:
        rest = []
        for i in range(len(weight)):
            if visited[i] == 0:
                rest.append(weight[i])
        poss = []
        for i in range(1, len(rest) + 1):
            poss += list(combinations(rest, i))

        for pos in poss:
            if sum(lst) == sum(pos):
                return len(lst) + len(pos)
    return -1


def dfs(weight,cnt, sum_, lst):
    global max_sum, max_len, visited


    if cnt == len(weight):
        return

    if check(weight,lst) != -1:
        max_sum = max(sum_, max_sum)
        max_len = max(check(weight,lst), max_len)


    for i, n in enumerate(weight):
        if visited[i] == 0:
            lst.append(n)
            visited[i] = 1
            sum_ += n

            dfs(weight,cnt + 1, sum_, lst)

            lst.pop()
            visited[i] = 0
            sum_ -= n
    return [max_len, max_sum]


max_sum = 0
max_len = 0
def solution(weight):
    global max_sum,max_len,visited
    visited = [0] * (len(weight))

    answer = dfs(weight,0,0,[])
    return answer

print(solution(weight))