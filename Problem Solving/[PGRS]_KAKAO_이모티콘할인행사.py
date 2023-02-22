users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]

def solution(users, emoticons):
    answer = []

    max_user = 0
    max_profit = 0


    discount = [10,20,30,40]

    disc_combs = []

    def dfs(cnt,poss_comb):
        if cnt == len(emoticons):
            disc_combs.append(poss_comb[:])
            return

        for disc in discount:
                poss_comb[cnt] += disc
                dfs(cnt + 1,poss_comb)
                poss_comb[cnt] -= disc

    dfs(0,[0]*len(emoticons))

    for i in range(len(disc_combs)):
            user_cnt = 0
            profit = [0]*len(users)

            for j in range(len(emoticons)):
                for k in range(len(users)):
                    if users[k][0] <= disc_combs[i][j]:
                        profit[k] += emoticons[j]*(100-disc_combs[i][j])//100


            for k in range(len(users)):
                if profit[k] >= users[k][1]:
                    user_cnt += 1
                    profit[k] = 0

            if user_cnt >= max_user:
                if user_cnt == max_user:
                    max_profit = max(sum(profit),max_profit)
                else:
                    max_profit = sum(profit)

                max_user = user_cnt

    answer = [max_user,max_profit]
    return answer

print(solution(users,emoticons))
