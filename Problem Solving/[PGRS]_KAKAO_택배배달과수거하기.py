cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]

# 한번에 최대한 먼 곳의 작업을 끝내야함 -> 이동횟수 최소화
# 배달 or 수거할게 있으면 해당 위치로 이동 -> 왕복해야하므로 거리는 * 2

def solution(cap, n, deliveries, pickups):
    answer = 0

    deliv = 0
    pick = 0

    for i in range(n-1,-1,-1):
        deliv += deliveries[i]      # 가장 먼 곳부터 배달, 수거할 양 체크
        pick += pickups[i]

        while deliv>0 or pick>0:    # 배달 or 수거 해야할 것 있으면 그 위치로 이동
            deliv -= cap            # cap을 뺀 값이 모두 음수면, 해당 배달 or 수거할 양이 한번에 옮길 수 있는 양보다 적은것
            pick -= cap             # -> 왕복 도중에 추가적 배달 or 수거 가능
            answer += (i+1)*2

    return answer

print(solution(cap,n,deliveries,pickups))