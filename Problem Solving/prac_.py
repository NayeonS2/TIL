from itertools import combinations

weight = [100, 50, 50, 80, 40, 40]

max_sum = 0
max_len = 0
visited = [0] * (len(weight))

def check(lst):
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


def dfs(cnt, sum_, lst):
    global max_sum, max_len

    if cnt == len(weight):
        return

    if check(lst) != -1:
        max_sum = max(sum_, max_sum)
        max_len = max(check(lst), max_len)


    for i, n in enumerate(weight):
        if visited[i] == 0:
            lst.append(n)
            visited[i] = 1
            sum_ += n

            dfs(cnt + 1, sum_, lst)

            lst.pop()
            visited[i] = 0
            sum_ -= n
    return [max_len, max_sum]

dfs(0,0,[])
print(max_len,max_sum)