users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]

def solution(users, emoticons):
    answer = []

    max_users = 0
    max_profit = 0


    discount = [10,20,30,40]
    visited = [0] * len(discount)
    disc_comb = []
    def dfs(cnt):
        global max_users, max_profit


        if cnt == len(emoticons):
            tmp_users = 0
            tmp_pay_sum = 0
            for user in users:
                discount_std = user[0]
                paying_limit = user[1]

                tmp_paying = 0


                if tmp_paying > paying_limit:
                    tmp_users += 1
                    tmp_paying = 0

                else:

                    for i in range(len(emoticons)):

                        now_disc = disc_comb[i]
                        now_price = emoticons[i]

                        if discount_std <= now_disc:
                            tmp_paying += now_price*(1-now_disc//100)

                tmp_pay_sum += tmp_paying


        for idx, disc in enumerate(discount):
            if visited[idx] == 0:
                disc_comb.append(disc)
                visited[idx] = 1

                dfs(cnt+1)

                visited[idx] = 0
                disc_comb.remove(disc)


    dfs(0)

    answer = [max_users,max_profit]

    return answer

print(solution(users,emoticons))
