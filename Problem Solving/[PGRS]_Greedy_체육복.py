lost = [2,4]
reserve = [3]
n = 5

def solution(n, lost, reserve):
    answer = 0

    lost.sort()

    reserve.sort()

    for resv in reserve[:]:
        if resv in lost:
            reserve.remove(resv)
            lost.remove(resv)


    for resv in reserve:
        if resv-1 in lost:
            lost.remove(resv-1)
        elif resv+1 in lost:
            lost.remove(resv + 1)


    answer = n-len(lost)
    return answer

print(solution(n,lost,reserve))
