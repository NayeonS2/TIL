today = "2020.01.01"
terms = ["Z 3", "D 5"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]

from datetime import datetime
def time_chk(now,mth):
    y,m,d = map(int,now.split("."))

    yr = mth//12
    mn = mth%12

    y -= yr

    if m-mn < 1:
        y -= 1
        m = 12-(mn-m)
    else:
        m -= mn

    dt = datetime(y ,m, d)
    return dt


def solution(today, terms, privacies):
    answer = []

    dic = dict()
    for term in terms:
        alph,num = term.split(" ")
        dic[alph] = num

    chk = dict()
    for k,v in dic.items():
        chk[k] = time_chk(today,int(v))

    for i in range(len(privacies)):
        priv = privacies[i]
        dat,typ = priv.split(" ")
        y,m,d = map(int,dat.split("."))
        print(chk[typ])
        print(datetime(y,m,d))
        if (chk[typ] >= datetime(y,m,d)):
            answer.append(i+1)


    return answer
print(solution(today,terms,privacies))