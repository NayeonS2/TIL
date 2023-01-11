# 정확한 순위

import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1


for g in graph:
    print(*g)

# n행에서 0 값을 가지지 않은 학생은 n의 성적보다 높은 학생
# n열은 n보다 성적이 낮은 학생
# 따라서 n행과 n열에 연결되어 있는 학생의 수가 N - 1이면 순위를 정확히 알 수 있다!

result = 0
count = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if (graph[i][j] != 0) or (graph[j][i] != 0):
            count += 1
    if count == N - 1:
        result += 1
    count = 0

print(result)


