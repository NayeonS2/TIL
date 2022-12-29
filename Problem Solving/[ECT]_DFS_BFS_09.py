# 인구 이동

# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.
#
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

N,L,R = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
people = 0
union = []
cnt = 0
def bfs(i,j):
    global people, cnt

    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    people += arr[i][j]
    union.append((i,j))
    while q:
        i,j = q.popleft()

        for di,dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni,nj = i+di,j+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj]==0 and L<=abs(arr[i][j]-arr[ni][nj])<=R:
                union.append((ni,nj))
                people+=arr[ni][nj]
                visited[ni][nj] = 1
                q.append((ni,nj))
    for i,j in union:
        arr[i][j] = people//len(union)
    else:
        cnt+=1

result = 0

while True:
    visited = [[0] * N for _ in range(N)]
    done = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                bfs(i,j)
                done+=1
                union = []
                people = 0

    if done == N*N:
        break
    result += 1

#print(arr)
print(result)
