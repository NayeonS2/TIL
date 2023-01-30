numbers = [1, 1, 1, 1, 1]
target = 3

cnt = 0
def dfs(i,res,numbers,target):
    global cnt

    import sys
    sys.setrecursionlimit(5000)


    if i == len(numbers):
        if res == target:
            cnt += 1
        return


    for next in [-numbers[i],numbers[i]]:
        dfs(i+1,res+next,numbers,target)


    return cnt


def solution(numbers, target):

    answer = dfs(0,0,numbers,target)

    return answer

print(solution(numbers,target))