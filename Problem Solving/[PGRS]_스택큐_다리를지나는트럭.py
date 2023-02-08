truck_weights = [7,4,5,6]
bridge_length = 2
weight = 10

from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    cnt = 0
    bridge = deque([0]*bridge_length)
    q = deque(truck_weights)
    on_truck_weight = 0
    while q:
        cnt += 1
        on_truck_weight -= bridge.popleft()

        if on_truck_weight + q[0] > weight:
            bridge.append(0)

        else:
            now = q.popleft()
            on_truck_weight += now
            bridge.append(now)
    answer = cnt + bridge_length

    return answer
print(solution(bridge_length,weight,truck_weights))