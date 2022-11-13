# 프로그래머스 자물쇠와 열쇠

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rot_90(arr):    # 시계방향 90도 회전함수
    N = len(arr[0])
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res[j][N-1-i] = arr[i][j]
    return res

def matched(expanded_lock):     # 자물쇠 홈(0부분)과 키 돌기(1부분)가 맞는지 검사 (자물쇠 영역과 키영역을 합해서 모두 1이되면 들어맞는것!)
    M = len(expanded_lock[0]) // 3

    for i in range(M,2*M):
        for j in range(M,2*M):
            if expanded_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):

    N = len(key[0])
    M = len(lock[0])
    expanded_lock = [[0]*(3*M) for _ in range(3*M)]     # 자물쇠 영역을 3배만큼 확장 (키를 자물쇠영역 전반에 걸쳐가며 맞춰보기위해)

    for i in range(M):
        for j in range(M):
            expanded_lock[i+M][j+M] = lock[i][j]        # 확장 자물쇠 영역 중앙에 자물쇠 위치시킴

    for i in range(1,2*M):                              # 확장 자물쇠 영역에서 키를 이동시켜가며 체크
        for j in range(1,2*M):
            for now_key in [key, rot_90(key), rot_90(rot_90(key)), rot_90(rot_90(rot_90(key)))]:    # 해당 위치에서 0~270도까지 돌려보며 검사
                for r in range(N):
                    for c in range(N):
                        expanded_lock[i+r][j+c] += now_key[r][c]

                if matched(expanded_lock):
                    return True

                for r in range(N):
                    for c in range(N):
                        expanded_lock[i+r][j+c] -= now_key[r][c]    # 안맞으면 키 제거

    return False

