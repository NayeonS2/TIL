genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

def solution(genres, plays):
    answer = []

    dic = dict()
    cnt_dic = dict()

    for genre in genres:
        dic[genre] = []
    for i in range(len(genres)):
        dic[genres[i]].append((i,plays[i]))
    for elem in dic.values():
        elem.sort(key=lambda x: (-x[1],x[0]))

    for genre in genres:
        cnt_dic[genre] = 0
    for i in range(len(genres)):
        cnt_dic[genres[i]] += plays[i]

    new_cnt = sorted(cnt_dic.items(), key=lambda x:x[1], reverse=True)


    for sortt in new_cnt:
        cnt = 0
        for elem in dic[sortt[0]]:
            if cnt < 2:
                answer.append(elem[0])
                cnt += 1


    return answer

print(solution(genres,plays))