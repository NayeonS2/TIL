sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]


def dfs(sizes,idx,tmp1,visited):
    global min_,max_1,max_2

    if len(tmp1) == len(sizes):

        for i in range(len(sizes)):

            max_1 = max(max_1,tmp1[i][0])
            max_2 = max(max_2, tmp1[i][1])

        tmp_res = max_1 * max_2
        max_1 = 0
        max_2 = 0

        min_ = min(min_,tmp_res)


    else:

        for wallet in [sizes[idx],sizes[idx][::-1]]:
            if wallet not in visited:
                dfs(sizes,idx+1,tmp1 + [wallet], visited + [wallet])

    return min_


def solution(sizes):
    tmp1 = []
    tmp2 = []
    for i in range(len(sizes)):
        tmp1.append(max(sizes[i]))
        tmp2.append(min(sizes[i]))
    answer = max(tmp1)*max(tmp2)

    return answer

print(solution(sizes))




