citations =  [25, 8, 5, 3, 3]
def solution(citations):

    answer = 0
    citations.sort(reverse=True)

    for j in range(len(citations)):
        if citations[j] >= j+1:
           answer = j+1

    return answer

print(solution(citations))