# 가운데를 말해요
# 1 5 2 10 -99 7 5
# 1 1 2 2 2 2 5
# 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다
# 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다

# left_heap(중간값보다 작은 힙 - 최대힙) & right_heap(중간값보다 큰 힙 - 최소힙) 사용!

import sys, heapq
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

left_heap = []
right_heap = []
for i in range(N):
    value = int(sys.stdin.readline())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -value)
    else:
        heapq.heappush(right_heap, value)

    if (left_heap and right_heap) and (-left_heap[0] > right_heap[0]):
        left_root = heapq.heappop(left_heap)
        heapq.heappush(right_heap,-left_root)

        right_root = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -right_root)

    print(-left_heap[0])


