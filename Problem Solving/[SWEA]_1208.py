import sys

sys.stdin = open('input.txt')

def max_v(lst):
    max_val = 0
    for x in range(len(lst)):
        if lst[x] > lst[max_val]:
            max_val = x
    return max_val

def min_v(lst):
    min_val = 0
    for x in range(len(lst)):
        if lst[x] < lst[min_val]:
            min_val = x
    return min_val




T = 10

for tc in range(1,T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    new_ = boxes[:]

    cnt = 0
    while cnt < dump and  max(boxes) - min(boxes) > 1:

        boxes[max_v(boxes)] -= 1
        boxes[min_v(boxes)] += 1


        cnt+=1

    print(f'#{tc} {max(boxes)-min(boxes)}')