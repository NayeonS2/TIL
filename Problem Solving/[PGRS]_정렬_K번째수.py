array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def res(array, command):
    s,e,n = command
    temp = array[s-1:e]
    temp.sort()
    result = temp[n-1]
    return result


def solution(array, commands):
    answer = []
    for command in commands:
        answer.append(res(array,command))
    return answer

print(solution(array,commands))