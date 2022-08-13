def max_v(lst):
    max_val = lst[0]
    for i in range(len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val


import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, list(input())))    # 숫자들을 리스트로 변환 [4,9,6,7,9]


    C = [0]*10  # 카운팅 위해 빈 리스트 생성

    for i in range(N):
        C[nums[i]] += 1 # 숫자별 카운팅
    idxs = []   # max count를 가진 idx들을 저장하기위한 리스트
    for idx, val in enumerate(C):

        if val == max_v(C):
            idxs.append(idx)    # max count가 복수일경우 idx값들중 가장 큰 값을 반환
    print(f'#{tc} {max_v(idxs)} {C[max_v(idxs)]}')  # max count를 갖는 max idx와 그 count값을 출력