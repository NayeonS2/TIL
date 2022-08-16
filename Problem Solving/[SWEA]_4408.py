import sys
sys.stdin = open('input.txt')

T = int(input())


def max_time(lst):
    max_t = 0
    for t in lst:
        if t > max_t:
            max_t = t
    return max_t


for tc in range(1,T+1):
    corr = [0] * 200
    N = int(input())
    for n in range(N):
        now, goal = map(int, input().split())
        now_idx = (now-1)//2
        goal_idx = (goal-1)//2
        if now<=goal:

            for i in range(now_idx,goal_idx+1):
                corr[i] += 1
        else:
            for i in range(goal_idx,now_idx+1):
                corr[i] += 1

    print(f'#{tc} {max_time(corr)}')
