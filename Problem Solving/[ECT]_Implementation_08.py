# 프로그래머스 기둥과 보 설치
# 이중배열, deepcopy 이용했으나 실패!

# 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽 방향으로 설치 또는 삭제

# build_frame의 원소는 [x, y, a, b]형태
# x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
# return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고있어야 합니다.
# return 하는 배열의 원소는 [x, y, a] 형식입니다.
# x, y는 기둥, 보의 교차점 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
# x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.


# 기둥 2 / 보 3
n = 5
build_frame = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
               [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

# 올바른 구조인지 체크
def check(answer):
    for x, y, a in answer:
        # 기둥이면
        if a == 0:
            # 바닥 위 or 보 한쪽 끝 위 or 다른 기둥 위
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            else:
                return False
        # 보면
        if a == 1:
            # 한쪽 끝부분이 기둥위 or 양쪽 끝부분이 다른 보와 동시에 연결
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            else:
                return False
    return True

def solution(n, build_frame):
    answer = []
    for info in build_frame:
        x, y, a, b = info

        # 삭제
        if b == 0:
            # 삭제 후 check해서 불가능하면 다시 설치
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
        # 설치
        if b == 1:
            # 설치 후 check해서 불가능하면 다시 제거
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
    # 정렬 후 출력
    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))
    return answer

print(solution(n,build_frame))
