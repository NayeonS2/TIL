participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

# 해시 (검색에 효율적!)

def solution(participant, completion):
    answer = ''
    temp = {}
    for part in participant:
        if part not in temp:
            temp[part] = 1
        else:
            temp[part] += 1

    for comp in completion:
        if comp in temp.keys():
            temp[comp] -= 1

    for k,v in temp.items():
        if v != 0:
            answer += k

    return answer

print(solution(participant,completion))