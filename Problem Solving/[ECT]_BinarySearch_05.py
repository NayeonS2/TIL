# 공유기 설치
# 집 N개가 수직선 위에 x1, x2, ... xN 좌표를 가짐
# 공유기 C개 설치
# 한집에는 공유기 하나만, 가장 인접한 두 공유기 사이의 거리를 가능한 크게하여 설치

import sys
input = sys.stdin.readline

def binary_search(min_gap,max_gap):
    ans = 0

    while min_gap <= max_gap:
        mid_gap = (min_gap + max_gap) // 2      # 가장 인접한 두 공유기 사이의 거리를 이진탐색으로 조절해나가며 가능한한 가장 큰값 찾기
        cnt = 1                                 # 설치된 공유기 수
        position = houses[0]                    # 지금 설치한 공유기 위치
        for j in range(1, N):
            if houses[j] >= position + mid_gap: # 해당 집 위치가 (현재 집 위치 + 설정해놓은 가장 인접한 두 공유기 사이의 거리) 이상이면
                position = houses[j]            # 해당 집에 공유기 설치하고 다음 집 탐색
                cnt += 1
        if cnt >= C:                            # 설치할 공유기 수 이상 설치되면
            min_gap = mid_gap + 1               # 가장 인접한 두 공유기 사이의 거리를 증가시켜 재탐색
            ans = max(ans,mid_gap)
        else:
            max_gap = mid_gap - 1               # 공유기 수 충족 못시키면 거리 감소시켜 재탐색
    return ans


N,C = map(int,input().split())
houses = [0]*N
for i in range(N):
    houses[i] = int(input())
houses.sort()

max_gap = houses[-1] - houses[0]
min_gap = 1     # houses[1] - houses[0] 하면 틀림! 왜?

print(binary_search(min_gap,max_gap))



