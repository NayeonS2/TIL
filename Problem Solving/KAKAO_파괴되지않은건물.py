# 파괴되지 않은 건물
# 누적합

board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]

def solution(board, skill):
    answer = 0

    N = len(board)
    M = len(board[0])
    K = len(skill)
    sum_arr = [[0] * (M+1) for _ in range(N+1)]

    for i in range(K):
        type, r1, c1, r2, c2, degree = skill[i][0], skill[i][1], skill[i][2], skill[i][3], skill[i][4], skill[i][5]

        if type == 1:
            sum_arr[r1][c1] += -degree
            sum_arr[r1][c2+1] += degree
            sum_arr[r2+1][c1] += degree
            sum_arr[r2+1][c2+1] += -degree
        elif type == 2:
            sum_arr[r1][c1] += degree
            sum_arr[r1][c2 + 1] += -degree
            sum_arr[r2 + 1][c1] += -degree
            sum_arr[r2 + 1][c2 + 1] += degree

    for i in range(len(sum_arr)-1):
        for j in range(len(sum_arr[0])-1):
            sum_arr[i][j+1] += sum_arr[i][j]

    for j in range(len(sum_arr[0])-1):
        for i in range(len(sum_arr)-1):
            sum_arr[i+1][j] += sum_arr[i][j]

    for i in range(N):
        for j in range(M):
            board[i][j] += sum_arr[i][j]

            if board[i][j] > 0:
                answer += 1


    return answer


print(solution(board,skill))