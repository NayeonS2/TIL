# 엘유플 4번

# 사람n + 식인종m = 최대p
# 섬2 배2 항상 식인종<사람
# 섬(사람,식인종)
# 사람1 식인종2
n = 2
m = 2
p = 2


min_res = 987654321



def dfs(res,cnt, island, boat, target):
    global min_res

    n = 2
    m = 2
    p = 2

    visited = [0] * (n + m)
    new_ = visited[:]

    if len(target) == n+m:
        min_res = min(min_res, res)



    if ((island.count("1")>0 and island.count("2")>0) and (island.count("1") < island.count("2"))) or ((target.count("1")>0 and target.count("2")>0) and (target.count("1") < target.count("2"))):
        return

    if cnt == p and (boat.count("1") >= boat.count("2")):
        res += 1
        cnt = 0
        target += boat
        boat = []
        visited = new_

    for idx, n in enumerate(island):
        if visited[idx] == 0:
            boat.append(n)
            island.remove(n)
            visited[idx] = 1

            dfs(res,cnt + 1, island, boat, target)

            boat.remove(n)
            island.append(n)
            visited[idx] = 0


dfs(0,0, ["1","1","2","2"], [], [])
print(min_res)

