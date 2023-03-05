# 수영장
# 각 달 이용계획을 바탕으로 가장 적은 비용으로 수영장 이용
# 이용계획에 나타나는 숫자는 해당 달에 수영장을 이용할 날의 수
# 이용권 : 1일 / 1달 / 3달 (11월, 12월에도 사용은 가능하나 다음 해로 넘어가는 건 불가능) / 1년

# 각 달 최소 누적 금액 구하기위해 dp 사용

import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1,1+T):
    d, m, thr_m, y = map(int,input().split())   # 1일 : 10원, 1달: 40원, 3달: 100원, 1년: 300원
    plan = [0] + list(map(int,input().split()))   # 0 0 2 9 1 5 0 0 0 0 0 0

    result = [0] * 13   #

    for i in range(1,13):
        chrg = [0,0,1095000,1095000]    # 3달권, 1년권은 해당 안되는 달도 있으니 MAX로 설정해둠 3000*365

        chrg[0] = result[i-1] + (d * plan[i])   # 1일권 (전달까지 금액 + 일일권 * 날짜수)

        chrg[1] = result[i-1] + m   # 1달권 (전달까지 금액 + 한달권)

        if i > 2:
            chrg[2] = result[i-3] + thr_m   # 3달권  (3달전까지 금액 + 3달권)

        if i == 12:
            chrg[3] = y     # 1년권

        result[i] = min(chrg)   # 이용권 중 가장 가격이 적은 것을 결과 리스트에 넣어줌

    #print(result)
    print(f'#{tc} {result[-1]}')    # 최소금액 누적이기때문에 마지막 값을 출력