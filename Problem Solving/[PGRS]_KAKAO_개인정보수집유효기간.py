today = "2022.05.19"
terms = ["A 6", "B 12", "C 3"]
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]




def solution(today, terms, privacies):
    answer = []

    dic = dict()
    for term in terms:
        alph,num = term.split(" ")
        dic[alph] = num




    return dic
print(solution(today,terms,privacies))