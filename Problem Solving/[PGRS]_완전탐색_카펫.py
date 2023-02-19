brown = 10
yellow = 2


def solution(brown, yellow):
    answer = []

    all_ = brown+yellow

    x = (2*all_ - brown)//8
    y = all_//x

    answer = [x,y]

    return answer
print(solution(brown,yellow))

