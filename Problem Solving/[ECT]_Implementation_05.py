# 문자열 압축

s = "acdhdh"

def make_res(s,i):
    res = ''
    find = s[:i]
    tmp = s[i:]
    cnt = 1
    while tmp:
        if find == tmp[:i]:
            cnt += 1
            tmp = tmp[i:]

        if find != tmp[:i]:
            if cnt == 1:
                res += str(find)
            elif cnt > 1:
                res += str(cnt) + str(find)
            cnt = 0
            find = tmp[:i]

    return res


def solution(s):
    min_len = len(s)
    answer = 0
    for j in range(1,len(s)):
        if len(s) != len(set(list(s))):
            min_len = min(min_len,len(make_res(s,j)))

    answer += min_len

    return answer

print(solution(s))
