import sys

sys.stdin = open('input.txt')


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
d = {'t': 0, 'b': 1, 'l': 2, 'r': 3}    # 상하좌우 방향 벡터


# 터널별로 연결 가능한 방향을 딕셔너리로 생성
types = {'1': ['t', 'b', 'l', 'r'], '2': ['t', 'b'], '3': ['l', 'r'], '4': ['t', 'r'], '5': ['b', 'r'], '6': ['b', 'l'],
         '7': ['t', 'l']}


def bfs(i,j,N,M,L):
    global result
    q = [(i, j)]

    visited[i][j] = 1


    while q:
        i,j = q.pop(0)

        if visited[i][j] <= L:  # 탈출소요시간 이하의 값들만 리스트에 담아줌
            result.append(((i, j), visited[i][j]))


        for pos in types[str(arr[i][j])]:   # 해당위치의 터널에서 연결 가능한 방향의 좌표들을 돌려서
            nr = i + dr[d[pos]]
            nc = j + dc[d[pos]]
            if 0<=nr<N and 0<=nc<M and arr[nr][nc] != 0 and visited[nr][nc] == 0:   # 해당 좌표가 구간안에있고 0이아니고 방문한적이없을때
                if pos == 't':  # 움직일 좌표랑 현재 좌표의 연결 가능 방향들을 조건으로 맞춰줌
                    if 'b' in types[str(arr[nr][nc])]:
                        q.append((nr, nc))
                        visited[nr][nc] = visited[i][j] + 1
                elif pos == 'b':
                    if 't' in types[str(arr[nr][nc])]:
                        q.append((nr, nc))
                        visited[nr][nc] = visited[i][j] + 1
                elif pos == 'l':
                    if 'r' in types[str(arr[nr][nc])]:
                        q.append((nr, nc))
                        visited[nr][nc] = visited[i][j] + 1

                elif pos == 'r':
                    if 'l' in types[str(arr[nr][nc])]:
                        q.append((nr, nc))
                        visited[nr][nc] = visited[i][j] + 1




T = int(input())


for tc in range(1, 1 + T):
    N, M, R, C, L = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * M for _ in range(N)]

    result = []

    bfs(R,C,N,M,L)

    print(f'#{tc} {len(result)}')