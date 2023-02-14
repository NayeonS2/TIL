n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def solution(n, computers):

    def dfs(i):
        visited[i] = 1
        for next in range(n):
            if computers[i][next] == 1 and visited[next] == 0:
                dfs(next)

    answer = 0
    visited = [0]*n

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer

print(solution(n,computers))