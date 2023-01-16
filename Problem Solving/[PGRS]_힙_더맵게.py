scoville = [1, 2, 3, 9, 10, 12]
K = 7

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        else:
            now = heapq.heappop(scoville)
            next = heapq.heappop(scoville)
            heapq.heappush(scoville,now+(next*2))
            answer += 1
    return answer


print(solution(scoville,K))