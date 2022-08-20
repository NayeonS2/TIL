N = int(input())
pick = list(map(int,input().split()))

wait_line = [1]


for i in range(1,N):

    after_jump = i - pick[i]
    push_behind = wait_line[after_jump:]

    for _ in range(pick[i]):
        wait_line.pop()
    wait_line.append(i+1)
    wait_line += push_behind



print(*wait_line)