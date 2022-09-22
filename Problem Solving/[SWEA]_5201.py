import sys
sys.stdin = open('input.txt')

# N개의 컨테이터 M대의 트럭
# 트럭당 한개의 컨테이너 운반 가능 ( 적재용량 초과 컨테이너는 운반 불가 )
# w : 컨테이너 마다 실린 N개의 화물의 무게
# t : M대 트럭의 각 적재용량
# 결국 t 적재용량을 가진 트럭 한대는 w 무게를 가진 화물이 실린 컨테이너 한개를 운반
# 이동한 화물 총 중량이 최대가 되도록 했을때, 옮겨진 화물 전체 무게는 얼마인가
# 컨테이너 한 개도 옮길 수 없는 경우 0 출력

T = int(input())

for tc in range(1,1+T):
    N, M = map(int,input().split())

    w = list(map(int,input().split()))  # 5 3 1 화물 무게
    t = list(map(int,input().split()))  # 8 3   적재용량

    w = sorted(w)
    t = sorted(t)

    sum_w = 0

    while w and t:
        trck = t.pop()
        while w:
            cont = w.pop()

            if trck >= cont:
                sum_w += cont
                break


    print(f'#{tc} {sum_w}')