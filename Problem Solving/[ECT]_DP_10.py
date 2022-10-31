# 편집 거리
# 최소 편집 거리 알고리즘

import sys
#sys.stdin = open('input.txt')

def dist(word1,word2):
    n,m = len(word1), len(word2)

    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][0] = i #첫행 초기화
    for j in range(1, m + 1):
        d[0][j] = j #첫열 초기화

    for i in range(1, n + 1):
        for j in range(1, m + 1):
     #문자가 같다면 왼쪽 위에 해당하는 수를 그대로 대입
            if word1[i - 1] == word2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
     #문자가 다르다면, 3가지 경우 중에서 최솟값 찾기
            else: #삽입(왼쪽), 삭제(위쪽), 교체 (왼쪽 위) 중에서 최소 비용
                d[i][j] = 1 + min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1])
    return d[n][m]
word1 = 'sunday'
word2 = 'saturday'

print(dist(word1,word2))

# https://joyjangs.tistory.com/38
# A의 경우를 보면 'PH'에서 'PYT'로 2번의 연산으로 변환이 되었다고 생각한다.
# 다음 줄로 오면서 'O'가 더해지고 'PYTO'가 된 상황이다. 이 때는 'O'를 'H'로 수정 연산을 하면 된다.
# B의 경우 'PH'를 'PYTH'로 2번의 연산으로 변환이 되었다고 생각한다.
# 마찬가지로 다음 줄로 넘어가면서 'O'가 더해지고 'PYTHO'가 된 상황이다. 이 경우에는 'O'를 삭제 연산을 하게 되면 'PYTH'로 만들 수 있다.
# C의 경우 'PHO'를 'PYT'로 2번의 연산으로 변환이 되었다고 생각한다.
# 이 경우에는 다음 줄이 되는 것이 아니므로 'O'가 더해지는 것은 아니다. 'PYT'에서 'H'를 삽입하는 연산을 하게 되면 'PYTH'로 만들 수 있다.