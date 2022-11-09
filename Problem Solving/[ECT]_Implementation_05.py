# 문자열 압축

s = "acdhdh"

# i는 단위 개수
def make_res(s,i):
    res = ''
    find = s[:i]    # 찾을 문자열
    tmp = s[i:]     # 나머지 문자열
    cnt = 1         # 자기자신은 먼저 세고 시작
    while tmp:
        if find == tmp[:i]: # 바로 뒤에 같은 문자열이있으면
            cnt += 1        # 카운팅해주고
            tmp = tmp[i:]   # 문자열에서 제외

        if find != tmp[:i]: # 같은 문자열이 아니면
            if cnt == 1:    # 숫자랑 문자열을 str으로 붙여줌 (cnt 1일때는 생략)
                res += str(find)
            elif cnt > 1:
                res += str(cnt) + str(find)
            cnt = 0         # cnt 초기화
            find = tmp[:i]  # 다음 단위개수 만큼의 문자열을 탐색 시작

    return res


def solution(s):
    min_len = len(s)    # 최소길이
    answer = 0
    for j in range(1,len(s)):   # 몇개단위로 나눌건지
        if len(s) != len(set(list(s))): # 중복되는 문자가 존재할 경우에만 함수 실행
            min_len = min(min_len,len(make_res(s,j)))   # 단위 바꿔가며 최소길이 갱신

    answer += min_len

    return answer

print(solution(s))
