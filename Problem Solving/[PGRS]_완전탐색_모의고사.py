answers = [1,3,2,4,2]

def solution(answers):
    answer = []

    ans1 = [1,2,3,4,5]
    ans2 = [2,1,2,3,2,4,2,5]
    ans3 = [3,3,1,1,2,2,4,4,5,5]

    res = [0]*3

    for i in range(1,len(answers)+1):
        temp1 = i%len(ans1)
        temp2 = i%len(ans2)
        temp3 = i%len(ans3)

        if ans1[temp1-1] == answers[i-1]:
            res[0] += 1
        if ans2[temp2-1] == answers[i-1]:
            res[1] += 1
        if ans3[temp3-1] == answers[i-1]:
            res[2] += 1

    winner = max(res)
    for i in range(3):
        if res[i] == winner:
            answer.append(i+1)


    return answer

solution(answers)