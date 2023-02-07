clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

def solution(clothes):

    dic = dict()

    for cloth in clothes:
        dic[cloth[1]] = []

    for cloth in clothes:
        dic[cloth[1]].append(cloth[0])


    answer = 1
    for com in dic.values():
        answer *= (len(com)+1)

    answer -= 1


    return answer

print(solution(clothes))