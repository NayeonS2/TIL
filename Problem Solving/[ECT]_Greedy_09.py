# 무지의 먹방 라이브

food_times = [4,2,3,6,7,1,5,8]
k = 27

import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    ate_time = 0
    prev = 0
    remain = len(food_times)

    while True:
        if ate_time + (q[0][0] - prev) * remain > k:
            break

        now = heapq.heappop(q)[0]
        ate_time += (now - prev) * remain
        remain -= 1
        prev = now

    answer = sorted(q, key=lambda x:x[1])
    return answer[(k-ate_time) % remain][1]


print(solution(food_times,k))