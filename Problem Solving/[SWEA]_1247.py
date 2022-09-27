import sys
sys.stdin = open('input.txt')

def f(i,k,dis):
    global min_dis

    if dis >= min_dis:
        return

    if i == k:
        dis += abs(p[-1][0]-home[0])+abs(p[-1][1]-home[1])
        if dis < min_dis:
            min_dis = dis

    else:
        for j in range(k):
            if used[j] == 0:    # a[j]가 아직 사용되지 않았으면
                used[j] = 1     # a[j] 사용됨으로  표시
                p[i] = a[j]     # p[i]는 a[j]로 결정
                if i == 0:
                    f(i + 1, k, dis+abs(company[0]-a[j][0])+abs(company[1]-a[j][1]))  # p[i+1] 값을 결정하러 이동
                else:

                    f(i+1, k, dis+abs(p[i-1][0]-a[j][0])+abs(p[i-1][1]-a[j][1]))       # p[i+1] 값을 결정하러 이동
                used[j] = 0     # a[j]를 다른 자리에서 쓸 수 있도록 해제


T = int(input())

for tc in range(1,1+T):
    N = int(input())    # 고객의 수

    info = list(map(int,input().split()))

    company, home = info[:2], info[2:4]

    client = []
    for i in range(0,len(info[4:]),2):
        client.append(info[4:][i:i+2])

    a = client
    used = [0] * N
    p = [0] * N

    min_dis = 987654321
    f(0, N, 0)
    print(f'#{tc} {min_dis}')


