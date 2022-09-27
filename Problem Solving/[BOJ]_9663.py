# N-Queen

# 우측 대각선 (r_diag) 의 i+j는 항상 같음
# 좌측 대각선 (l_diag) 의 i-j는 항상 같음

N = int(input())

def dfs(i):
    global cnt

    if i == N:  # 행 인덱스
        cnt += 1
        return

    else:
        for j in range(N):  # 열 인덱스
            if j in col or i+j in r_diag or i-j in l_diag:  # j가 col안에 있거나, i+j가 r_diag에 있거나, i-j가 l_diag에 있으면 continue
                continue
            col.add(j)
            r_diag.add(i+j)
            l_diag.add(i-j)

            dfs(i+1)

            col.remove(j)           # 백트래킹
            r_diag.remove(i + j)
            l_diag.remove(i - j)



col = set()     # 셋을 써서 중복 방지
l_diag = set()
r_diag = set()

cnt = 0

dfs(0)

print(cnt)

